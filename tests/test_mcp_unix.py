import json
import socket
import threading

from reins.harness.mcp_unix import serve_once


def test_unix_transport_round_trip_and_cleanup(tmp_path):
    path = tmp_path / "mcp.sock"
    ready = threading.Event()

    def handler(request):
        return {"id": request["id"], "result": "ok"}

    # PON: the test waits on an event signalled by serve_once when the socket is
    # bound and listening — no active polling / sleep loop.
    thread = threading.Thread(target=serve_once, args=(path, handler), kwargs={"on_ready": ready.set})
    thread.start()
    assert ready.wait(2.0), "MCP socket never became ready"
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client:
        client.connect(str(path))
        client.sendall(json.dumps({"id": 1}).encode() + b"\n")
        assert json.loads(client.makefile("rb").readline()) == {"id": 1, "result": "ok"}
    thread.join()
    assert not path.exists()
