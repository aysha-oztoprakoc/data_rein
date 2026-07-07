"""
Tests for `reins.harness.ipc`: the same-node IPC fast path (binary UDS framing +
seqlock mmap SharedState). Cross-node coordination stays on MQTT; this module
never touches the network.
"""

import socket
import threading

from reins.harness import ipc


def test_frame_round_trip():
    payload = b'{"hello": "world"}'
    data = ipc.frame(ipc.REQ_JSON, payload)

    a, b = socket.socketpair()
    try:
        a.sendall(data)
        got = ipc.read_frame(b)
        assert got == (ipc.REQ_JSON, payload)
    finally:
        a.close()
        b.close()


def test_read_frame_truncated_header_returns_none():
    a, b = socket.socketpair()
    try:
        a.sendall(b"\x00\x01")  # shorter than FRAME_HEADER.size
        a.close()
        assert ipc.read_frame(b) is None
    finally:
        b.close()


def test_shared_state_write_read_round_trip(tmp_path):
    state = ipc.SharedState(path=tmp_path / "shared_state.mmap")
    assert state.write({"slots": {"m": {"state": "ready"}}})
    assert state.read() == {"slots": {"m": {"state": "ready"}}}


def test_shared_state_torn_read_returns_none(tmp_path):
    state = ipc.SharedState(path=tmp_path / "shared_state.mmap")
    state.write({"a": 1})
    seq, length = state._read_header()
    state._write_seq(seq + 1)  # force an odd (write-in-progress) seq
    assert state.read() is None


def test_ipc_server_status_round_trip_and_stop(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "reins.harness.coordinator.get_coordinator",
        lambda: type("C", (), {"status": lambda self: {"ok": True}})(),
    )
    sock_path = tmp_path / "reins_ipc.sock"
    server = ipc.IPCServer(socket_path=sock_path)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()

    try:
        for _ in range(100):
            if sock_path.exists():
                break
            threading.Event().wait(0.05)
        client = ipc.IPCClient(socket_path=sock_path)
        resp = client.request({"op": "status"}, timeout=5.0)
        assert resp == {"ok": True}
    finally:
        server.stop()
        t.join(timeout=5.0)
        assert not t.is_alive()
