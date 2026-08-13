from __future__ import annotations

import argparse
import sys
from pathlib import Path

import anyio
import httpx
import pytest
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.server.auth.settings import AuthSettings
from mcp.server.fastmcp import FastMCP
from pydantic import AnyHttpUrl

sys.path.insert(0, str(Path(__file__).parents[1]))
from reins.harness import cli, mcp_server
from reins.harness.mcp_security import (
    BearerTokenVerifier,
    McpHttpConfigurationError,
    configure_http_security,
)


def test_bearer_verifier_uses_constant_time_comparison(monkeypatch: pytest.MonkeyPatch) -> None:
    # Given
    compared: list[tuple[str, str]] = []

    def record_compare(candidate: str, expected: str) -> bool:
        compared.append((candidate, expected))
        return candidate == expected

    monkeypatch.setattr("reins.harness.mcp_security.hmac.compare_digest", record_compare)
    verifier = BearerTokenVerifier("vault-token")

    # When
    access = anyio.run(verifier.verify_token, "vault-token")

    # Then
    assert access is not None
    assert compared == [("vault-token", "vault-token")]


def test_http_server_rejects_missing_vault_token_before_transport(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given
    run_calls: list[str] = []
    monkeypatch.setattr(mcp_server.mcp, "run", lambda transport="stdio": run_calls.append(transport))

    # When / Then
    with pytest.raises(McpHttpConfigurationError, match="REINS_MCP_HTTP_TOKEN"):
        mcp_server.main(http=True, secret_loader=lambda _name: None)
    assert run_calls == []


def test_http_server_rejects_remote_bind_without_explicit_permission(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given
    run_calls: list[str] = []
    monkeypatch.setattr(mcp_server.mcp, "run", lambda transport="stdio": run_calls.append(transport))

    # When / Then
    with pytest.raises(McpHttpConfigurationError, match="allow-remote-http"):
        mcp_server.main(
            http=True,
            host="0.0.0.0",
            secret_loader=lambda _name: "vault-token",
        )
    assert run_calls == []


def test_http_server_returns_cleanly_on_operator_interrupt(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given
    def interrupt_server(*, transport: str) -> None:
        assert transport == "streamable-http"
        raise KeyboardInterrupt

    monkeypatch.setattr(mcp_server.mcp, "run", interrupt_server)

    # When
    result = mcp_server.main(
        http=True,
        secret_loader=lambda _name: "vault-token",
    )

    # Then
    assert result is None


def test_http_server_runtime_failure_still_propagates(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given
    class ServerRuntimeError(RuntimeError):
        pass

    def fail_server(*, transport: str) -> None:
        assert transport == "streamable-http"
        raise ServerRuntimeError("runtime failed")

    monkeypatch.setattr(mcp_server.mcp, "run", fail_server)

    # When / Then
    with pytest.raises(ServerRuntimeError, match="runtime failed"):
        mcp_server.main(
            http=True,
            secret_loader=lambda _name: "vault-token",
        )


def test_stdio_server_never_reads_http_token(monkeypatch: pytest.MonkeyPatch) -> None:
    # Given
    run_calls: list[str] = []

    def fail_if_read(_name: str) -> str | None:
        raise AssertionError("stdio attempted to read the HTTP credential")

    monkeypatch.setattr(mcp_server.mcp, "run", lambda transport="stdio": run_calls.append(transport))

    # When
    mcp_server.main(http=False, secret_loader=fail_if_read)

    # Then
    assert run_calls == ["stdio"]


def test_http_security_retains_dns_rebinding_protection() -> None:
    # Given
    # When
    settings = configure_http_security(mcp_server.mcp, "127.0.0.1")

    # Then
    assert settings.enable_dns_rebinding_protection is True
    assert "127.0.0.1:*" in settings.allowed_hosts


def test_mcp_cli_dispatches_explicit_remote_http_permission(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    _ = cli.register(subparsers)
    args = parser.parse_args(["mcp", "--http", "--host", "192.0.2.10", "--allow-remote-http"])
    calls: list[tuple[bool, str, int, bool]] = []
    def record_main(*, http: bool, host: str, port: int, allow_remote_http: bool) -> None:
        calls.append((http, host, port, allow_remote_http))

    monkeypatch.setattr(mcp_server, "main", record_main)

    # When
    handled = cli.handle(args)

    # Then
    assert handled is True
    assert calls == [(True, "192.0.2.10", 8765, True)]


def test_mcp_cli_translates_http_configuration_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given
    args = argparse.Namespace(
        command="mcp",
        http=True,
        host="0.0.0.0",
        port=8765,
        allow_remote_http=False,
    )

    def reject_http(**_kwargs: bool | str | int) -> None:
        raise McpHttpConfigurationError("remote bind rejected")

    monkeypatch.setattr(mcp_server, "main", reject_http)

    # When / Then
    with pytest.raises(SystemExit, match="remote bind rejected"):
        _ = cli.handle(args)


def test_streamable_http_requires_bearer_for_initialize_and_tool_list() -> None:
    async def scenario() -> None:
        # Given
        verifier = BearerTokenVerifier("vault-token")
        server = FastMCP(
            "authenticated-test-server",
            token_verifier=verifier,
            auth=AuthSettings(
                issuer_url=AnyHttpUrl("http://testserver"),
                resource_server_url=None,
            ),
        )

        def secured_tool() -> str:
            return "ok"

        _ = server.tool()(secured_tool)
        _ = configure_http_security(server, "testserver")
        app = server.streamable_http_app()
        transport = httpx.ASGITransport(app=app)

        async with app.router.lifespan_context(app):
            async with httpx.AsyncClient(
                transport=transport,
                base_url="http://testserver",
            ) as unauthenticated_client:
                # When
                response = await unauthenticated_client.post(
                    "/mcp",
                    json={
                        "jsonrpc": "2.0",
                        "id": 1,
                        "method": "initialize",
                        "params": {
                            "protocolVersion": "2025-06-18",
                            "capabilities": {},
                            "clientInfo": {"name": "qa", "version": "1"},
                        },
                    },
                    headers={"accept": "application/json, text/event-stream"},
                )

                # Then
                assert response.status_code == 401

            async with httpx.AsyncClient(
                transport=transport,
                base_url="http://testserver",
                headers={"Authorization": "Bearer vault-token"},
            ) as authenticated_client:
                # When
                async with streamable_http_client(
                    "http://testserver/mcp",
                    http_client=authenticated_client,
                ) as (read, write, _):
                    async with ClientSession(read, write) as session:
                        initialized = await session.initialize()
                        tools = await session.list_tools()

                # Then
                assert initialized.serverInfo.name == "authenticated-test-server"
                assert [tool.name for tool in tools.tools] == ["secured_tool"]

    anyio.run(scenario)


def test_stdio_tool_registration_keeps_action_gated_tool_names() -> None:
    # Given / When
    tools = anyio.run(mcp_server.mcp.list_tools)

    # Then
    names = {tool.name for tool in tools}
    assert {"route_local", "escalate_cloud", "compile_prompt_remote", "run_prompt_local"} <= names
