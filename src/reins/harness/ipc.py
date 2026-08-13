"""
Same-node IPC fast path for the data_rein harness (amdy-local only).

Two primitives:
- `SharedState`: a seqlock mmap segment the coordinator broadcasts its state
  snapshot to. Readers never poll the coordinator object directly — they read
  this segment, which is updated on every state transition (FBE).
- `IPCServer`/`IPCClient`: a Unix domain socket with a small binary frame
  protocol, for request/response and streamed generation between same-node
  processes without going through HTTP.

Cross-node coordination stays on MQTT (`config/mqtt_topics.json`) — UDS and
mmap do not cross the amdy/tell boundary, and mmap here carries JSON state
snapshots only, never tensors (cross-process tensor sharing through Ollama
is not possible; the harness never claims otherwise).
"""

from __future__ import annotations
from reins.services.logger import log_degradation

import json
import mmap
import os
import selectors
import socket
import struct
import threading
from pathlib import Path
from typing import Iterator, Optional

from reins.harness import external_io, paths

_HEADER = struct.Struct("!II")  # seq, payload_len
FRAME_HEADER = struct.Struct("!2sBBI")  # magic, version, msg_type, length
MAGIC = b"DR"
VERSION = 1

REQ_JSON = 0x01
RESP_JSON = 0x02
STREAM_CHUNK = 0x03
STREAM_END = 0x04
ERR_JSON = 0x7F


def frame(msg_type: int, payload: bytes) -> bytes:
    return FRAME_HEADER.pack(MAGIC, VERSION, msg_type, len(payload)) + payload


def read_frame(sock: socket.socket) -> Optional[tuple[int, bytes]]:
    """Read one framed message. Returns None on clean EOF or a malformed header."""
    header = _recv_exact(sock, FRAME_HEADER.size)
    if header is None:
        return None
    magic, version, msg_type, length = FRAME_HEADER.unpack(header)
    if magic != MAGIC or version != VERSION:
        return None
    payload = _recv_exact(sock, length) if length else b""
    if payload is None:
        return None
    return msg_type, payload


def _recv_exact(sock: socket.socket, n: int) -> Optional[bytes]:
    if n == 0:
        return b""
    chunks = []
    received = 0
    while received < n:
        chunk = sock.recv(n - received)
        if not chunk:
            return None
        chunks.append(chunk)
        received += len(chunk)
    return b"".join(chunks)


class SharedState:
    """Seqlock-protected mmap segment carrying a JSON state snapshot."""

    def __init__(self, path: Optional[Path] = None, size: int = 4096) -> None:
        self.path = path or paths.shared_state()
        self.size = size
        self.disabled = False
        self._mm: Optional[mmap.mmap] = None
        self._open()

    def _open(self) -> None:
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            if not self.path.exists() or self.path.stat().st_size < self.size:
                with open(self.path, "wb") as f:
                    f.write(b"\x00" * self.size)
            fd = os.open(self.path, os.O_RDWR)
            try:
                self._mm = mmap.mmap(fd, self.size)
            finally:
                os.close(fd)
        except Exception:
            log_degradation(__name__)
            self.disabled = True
            self._mm = None

    def write(self, state: dict) -> bool:
        if self.disabled or self._mm is None:
            return False
        try:
            payload = json.dumps(state).encode("utf-8")
            if _HEADER.size + len(payload) > self.size:
                payload = payload[: self.size - _HEADER.size]
            self._mm.seek(0)
            seq = self._read_seq()
            self._write_seq(seq + 1)  # odd = write in progress
            self._mm.seek(_HEADER.size)
            self._mm.write(payload)
            self._mm.flush()
            self._write_header_len(len(payload))
            self._write_seq(seq + 2)  # even = stable
            return True
        except Exception:
            log_degradation(__name__)
            return False

    def read(self) -> Optional[dict]:
        if self.disabled or self._mm is None:
            return None
        for _ in range(3):
            try:
                seq1, length = self._read_header()
                if seq1 % 2 == 1:
                    continue  # write in progress
                self._mm.seek(_HEADER.size)
                payload = self._mm.read(length)
                seq2, _ = self._read_header()
                if seq1 != seq2:
                    continue  # torn read
                return json.loads(payload.decode("utf-8"))
            except Exception:
                log_degradation(__name__)
                continue
        return None

    def _read_header(self) -> tuple[int, int]:
        self._mm.seek(0)
        return _HEADER.unpack(self._mm.read(_HEADER.size))

    def _read_seq(self) -> int:
        return self._read_header()[0]

    def _write_seq(self, seq: int) -> None:
        _, length = self._read_header()
        self._mm.seek(0)
        self._mm.write(_HEADER.pack(seq, length))

    def _write_header_len(self, length: int) -> None:
        seq, _ = self._read_header()
        self._mm.seek(0)
        self._mm.write(_HEADER.pack(seq, length))


class IPCServer:
    """UDS server dispatching {status, load, unload, generate} ops.

    Event-driven via `selectors` — the accept loop blocks on `sel.select()`
    with no timeout (zero idle CPU); shutdown is a self-pipe write that wakes
    the selector instead of a timeout-based poll.
    """

    def __init__(self, socket_path: Optional[Path] = None) -> None:
        self.socket_path = socket_path or paths.ipc_socket()
        self._stop = threading.Event()
        self._sel = selectors.DefaultSelector()
        self._server_sock: Optional[socket.socket] = None
        self._wake_r, self._wake_w = os.pipe()

    def _handle_op(self, op: dict) -> dict:
        from reins.harness.coordinator import get_coordinator

        coord = get_coordinator()
        kind = op.get("op")
        try:
            if kind == "status":
                return coord.status()
            if kind == "load":
                slot = coord.load(op["model"])
                return {"state": slot.state.value, "est_gb": slot.est_gb, "error": slot.error}
            if kind == "unload":
                slot = coord.unload(op["model"])
                return {"state": slot.state.value}
            if kind == "generate":
                res = coord.generate(op["model"], op["prompt"], op.get("options"))
                return {"ok": res.ok, "text": res.text, "error": res.error}
            return {"error": f"unknown op {kind!r}"}
        except Exception as e:
            log_degradation(__name__)
            return {"error": str(e)}

    def _serve_client(self, conn: socket.socket) -> None:
        try:
            got = read_frame(conn)
            if got is None:
                return
            msg_type, payload = got
            if msg_type != REQ_JSON:
                conn.sendall(frame(ERR_JSON, json.dumps({"error": "expected REQ_JSON"}).encode()))
                return
            try:
                op = json.loads(payload.decode("utf-8"))
            except Exception:
                log_degradation(__name__)
                conn.sendall(frame(ERR_JSON, json.dumps({"error": "malformed json"}).encode()))
                return
            result = self._handle_op(op)
            conn.sendall(frame(RESP_JSON, json.dumps(result).encode("utf-8")))
        except Exception as e:
            log_degradation(__name__)
            try:
                conn.sendall(frame(ERR_JSON, json.dumps({"error": str(e)}).encode()))
            except Exception:
                log_degradation(__name__)
                pass
        finally:
            conn.close()

    def serve_forever(self) -> None:
        if self.socket_path.exists():
            self.socket_path.unlink()
        self.socket_path.parent.mkdir(parents=True, exist_ok=True)
        self._server_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._server_sock.bind(str(self.socket_path))
        os.chmod(self.socket_path, 0o600)
        self._server_sock.listen(8)
        self._server_sock.setblocking(False)

        self._sel.register(self._server_sock, selectors.EVENT_READ, data="server")
        self._sel.register(self._wake_r, selectors.EVENT_READ, data="wake")

        while not self._stop.is_set():
            events = self._sel.select(timeout=None)
            for key, _ in events:
                if key.data == "wake":
                    os.read(self._wake_r, 4096)
                    continue
                conn, _addr = self._server_sock.accept()
                self._serve_client(conn)

        self._sel.unregister(self._server_sock)
        self._sel.unregister(self._wake_r)
        self._server_sock.close()
        try:
            self.socket_path.unlink()
        except Exception:
            log_degradation(__name__)
            pass

    def stop(self) -> None:
        self._stop.set()
        os.write(self._wake_w, b"x")


class IPCClient:
    def __init__(self, socket_path: Optional[Path] = None) -> None:
        self.socket_path = socket_path or paths.ipc_socket()

    def request(self, op: dict, timeout: float = 30.0) -> dict:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            _ = external_io.call(
                f"ipc:{self.socket_path}:connect",
                lambda: sock.connect(str(self.socket_path)),
            )
            sock.sendall(frame(REQ_JSON, json.dumps(op).encode("utf-8")))
            got = read_frame(sock)
            if got is None:
                return {"error": "no response (connection closed)"}
            msg_type, payload = got
            return json.loads(payload.decode("utf-8"))
        except Exception as e:
            log_degradation(__name__)
            return {"error": str(e)}
        finally:
            sock.close()

    def stream(self, op: dict, timeout: float = 300.0) -> Iterator[bytes]:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            _ = external_io.call(
                f"ipc:{self.socket_path}:connect",
                lambda: sock.connect(str(self.socket_path)),
            )
            sock.sendall(frame(REQ_JSON, json.dumps(op).encode("utf-8")))
            done = False
            while not done:
                got = read_frame(sock)
                if got is None:
                    return
                msg_type, payload = got
                if msg_type == STREAM_END:
                    done = True
                elif msg_type in (STREAM_CHUNK, RESP_JSON):
                    yield payload
                elif msg_type == ERR_JSON:
                    done = True
        finally:
            sock.close()
