from fastmcp import FastMCP
from typing import Any
from client import CodePushClient
import os

SERVER_URL = "https://codepush.pro"

mcp = FastMCP(name="Codemagic Codepush MCP Server")


def _get_client() -> CodePushClient:
    access_key = os.environ.get("CODEPUSH_ACCESS_KEY")
    if not access_key:
        raise ValueError("CODEPUSH_ACCESS_KEY environment variable is not set")
    return CodePushClient(server_url=SERVER_URL, access_key=access_key)


@mcp.tool(description="Verify access key validity")
def auth() -> dict[str, Any]:
    """Verify that the configured access key is valid."""
    client = _get_client()
    return client.authenticate()


@mcp.tool(description="Get current user information")
def whoami() -> dict[str, Any]:
    """Get information about the current authenticated user."""
    client = _get_client()
    return client.get_account_info()


@mcp.tool(description="List all CodePush apps")
def listApps() -> dict[str, Any]:
    """List all CodePush apps available to the authenticated user."""
    client = _get_client()
    return client.list_apps()


@mcp.tool(description="List deployments for an app")
def listDeployments(appName: str) -> dict[str, Any]:
    """List all deployments for a specific app.

    Args:
        appName: The name of the app to list deployments for
    """
    client = _get_client()
    return client.list_deployments(appName)


@mcp.tool(description="Get release history for a deployment")
def getDeploymentHistory(appName: str, deploymentName: str) -> dict[str, Any]:
    """Get the release history for a specific deployment.

    Args:
        appName: The name of the app
        deploymentName: The name of the deployment
    """
    client = _get_client()
    return client.get_deployment_history(appName, deploymentName)
