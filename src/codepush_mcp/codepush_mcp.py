from fastmcp import FastMCP
from typing import Any
import subprocess
import os
import json

SERVER_URL = os.environ.get("CODEPUSH_SERVER_URL", "https://codepush.pro")

mcp = FastMCP(name="Codemagic Codepush MCP Server")


def _run_codepush_cli(args: list[str]) -> dict[str, Any]:
    try:
        result = subprocess.run(
            ["npx", "--yes", "@codemagic/code-push-cli"] + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True,
        )

        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"error: {e.stderr.strip() or str(e)}")


def show_codepush_cli_version() -> dict[str, Any]:
    return _run_codepush_cli(["whoami"])


@mcp.tool(description="Login to CodePush with access key")
def login() -> dict[str, Any]:
    """
    Login to CodePush server using the access key from CODEPUSH_ACCESS_KEY environment variable.
    This tool should be run first before using other tools.
    """
    access_key = os.environ.get("CODEPUSH_ACCESS_KEY")
    if not access_key:
        raise ValueError("CODEPUSH_ACCESS_KEY environment variable is not set")

    return _run_codepush_cli(["login", SERVER_URL, "--access-key", access_key])


@mcp.tool(description="Logout from CodePush")
def logout() -> dict[str, Any]:
    """
    Logout from CodePush server.
    This tool should be run to clear the authentication state.
    """
    return _run_codepush_cli(["logout"])


@mcp.tool(description="Get current user information")
def whoami() -> dict[str, Any]:
    """Get information about the current authenticated user."""
    return _run_codepush_cli(["whoami"])


@mcp.tool(description="List all CodePush apps")
def listApps() -> dict[str, Any]:
    """List all CodePush apps available to the authenticated user."""
    return _run_codepush_cli(["app", "ls", "--format", "json"])


@mcp.tool(description="List deployments for an app")
def listDeployments(appName: str) -> dict[str, Any]:
    """List all deployments for a specific app.

    Args:
        appName: The name of the app to list deployments for
    """
    return _run_codepush_cli(["deployment", "ls", appName, "--format", "json"])


@mcp.tool(description="Get release history for a deployment")
def getDeploymentHistory(appName: str, deploymentName: str) -> dict[str, Any]:
    """Get the release history for a specific deployment.

    Args:
        appName: The name of the app
        deploymentName: The name of the deployment
    """
    return _run_codepush_cli(
        ["deployment", "history", appName, deploymentName, "--format", "json"]
    )
