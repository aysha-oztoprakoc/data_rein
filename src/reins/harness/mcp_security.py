"""Bearer authentication and bind policy for Streamable HTTP MCP."""

from __future__ import annotations

import hmac
import ipaddress
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Final, final

from mcp.server.auth.provider import AccessToken
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

MCP_HTTP_TOKEN_SECRET: Final = "REINS_MCP_HTTP_TOKEN"
SecretLoader = Callable[[str], str | None]


class McpHttpConfigurationError(RuntimeError):
    """HTTP MCP cannot start with the requested security configuration."""


@final
class BearerTokenVerifier:
    """Verify one vault-backed bearer token without ordinary equality checks."""

    def __init__(self, expected_token: str = "") -> None:
        self._expected_token: str = expected_token

    def configure(self, expected_token: str) -> None:
        self._expected_token = expected_token

    async def verify_token(self, token: str) -> AccessToken | None:
        if not self._expected_token or not hmac.compare_digest(token, self._expected_token):
            return None
        return AccessToken(token="authenticated", client_id="reins-mcp-http", scopes=[])


def load_http_token(secret_loader: SecretLoader | None = None) -> str:
    try:
        if secret_loader is None:
            repository_root = str(Path(__file__).resolve().parents[3])
            if repository_root not in sys.path:
                sys.path.insert(0, repository_root)
            from scripts.get_secrets import get_or_create_secret

            return get_or_create_secret(MCP_HTTP_TOKEN_SECRET)
        token = secret_loader(MCP_HTTP_TOKEN_SECRET)
        if not token:
            raise McpHttpConfigurationError(
                f"encrypted vault secret {MCP_HTTP_TOKEN_SECRET} is required for HTTP MCP"
            )
        return token
    except McpHttpConfigurationError:
        raise
    except (OSError, RuntimeError, ValueError) as error:
        raise McpHttpConfigurationError("encrypted vault token provisioning failed") from error


def is_loopback_host(host: str) -> bool:
    normalized = host.removeprefix("[").removesuffix("]")
    if normalized.casefold() == "localhost":
        return True
    try:
        return ipaddress.ip_address(normalized).is_loopback
    except ValueError:
        return False


def configure_http_security(
    server: FastMCP,
    host: str,
) -> TransportSecuritySettings:
    host_pattern = f"[{host}]:*" if ":" in host and not host.startswith("[") else f"{host}:*"
    allowed_hosts = [
        "127.0.0.1",
        "127.0.0.1:*",
        "localhost",
        "localhost:*",
        "[::1]",
        "[::1]:*",
    ]
    for allowed_host in (host, host_pattern):
        if allowed_host not in allowed_hosts:
            allowed_hosts.append(allowed_host)
    settings = TransportSecuritySettings(
        enable_dns_rebinding_protection=True,
        allowed_hosts=allowed_hosts,
        allowed_origins=[],
    )
    server.settings.transport_security = settings
    return settings
