from __future__ import annotations

import json
import os
import socket
from collections.abc import Callable
from pathlib import Path

import anyio
import mcp.types as types
from anyio.streams.buffered import BufferedByteReceiveStream
from mcp.server.fastmcp import FastMCP
from mcp.shared.message import SessionMessage

JsonHandler = Callable[[dict[str, object]], dict[str, object]]


def serve_once(
    path: Path,
    handler: JsonHandler,
    on_ready: Callable[[], None] | None = None,
) -> None:
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    if path.exists():
        if not path.is_socket():
            raise RuntimeError(f"unsafe MCP socket path: {path}")
        path.unlink()
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
        server.bind(str(path))
        os.chmod(path, 0o600)
        server.listen(1)
        if on_ready is not None:
            on_ready()
        try:
            conn, _ = server.accept()
            with conn:
                data = conn.makefile("rwb")
                request = json.loads(data.readline())
                response = handler(request)
                data.write(json.dumps(response).encode() + b"\n")
                data.flush()
        finally:
            if path.is_socket():
                path.unlink()



async def serve_mcp_unix(mcp: FastMCP, path: str) -> None:
    """Serve FastMCP over a UNIX domain socket. Accepts multiple connections concurrently."""
    p = Path(path)
    p.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    if p.exists():
        if not p.is_socket():
            raise RuntimeError(f"unsafe MCP socket path: {path}")
        p.unlink()

    listener = await anyio.create_unix_listener(path)
    os.chmod(path, 0o600)

    async def handle_client(client: anyio.abc.ByteStream) -> None:
        read_stream_writer, read_stream = anyio.create_memory_object_stream(0)
        write_stream, write_stream_reader = anyio.create_memory_object_stream(0)

        async def client_reader() -> None:
            try:
                async with read_stream_writer:
                    buffered = BufferedByteReceiveStream(client)
                    running = True
                    while running:
                        try:
                            line = await buffered.receive_until(b"\n", 65536)
                            message = types.JSONRPCMessage.model_validate_json(line)
                            session_message = SessionMessage(message)
                            await read_stream_writer.send(session_message)
                        except anyio.EndOfStream:
                            running = False
                        except Exception as e:
                            from reins.services.logger import log_degradation
                            log_degradation(__name__, str(e))
                            await read_stream_writer.send(e)
            except anyio.ClosedResourceError:
                pass

        async def client_writer() -> None:
            try:
                async with write_stream_reader:
                    async for session_message in write_stream_reader:
                        json_str = session_message.message.model_dump_json(
                            by_alias=True, exclude_none=True
                        )
                        await client.send((json_str + "\n").encode("utf-8"))
            except anyio.ClosedResourceError:
                pass

        async with anyio.create_task_group() as tg:
            tg.start_soon(client_reader)
            tg.start_soon(client_writer)
            await mcp._mcp_server.run(
                read_stream,
                write_stream,
                mcp._mcp_server.create_initialization_options(),
            )

    try:
        await listener.serve(handle_client)
    finally:
        if p.exists() and p.is_socket():
            p.unlink()
