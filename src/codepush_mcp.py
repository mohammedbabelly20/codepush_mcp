from fastmcp import FastMCP
from typing import Any
from client import CodePushClient
from settings import CodepushSettings

mcp = FastMCP(name="CodePush MCP Server")
settings = CodepushSettings()
client = CodePushClient(
    server_url=settings.codepush_api_url, access_key=settings.get_access_key()
)


@mcp.tool(description="Verify access key validity")
def auth() -> dict[str, Any]:
    """Verify that the configured access key is valid."""
    return client.authenticate()


@mcp.tool(description="Get current user information")
def whoami() -> dict[str, Any]:
    """Get information about the current authenticated user."""
    return client.get_account_info()


@mcp.tool(description="List all CodePush apps")
def listApps() -> dict[str, Any]:
    """List all CodePush apps available to the authenticated user."""
    return client.list_apps()


@mcp.tool(description="List deployments for an app")
def listDeployments(appName: str) -> dict[str, Any]:
    """List all deployments for a specific app.

    Args:
        appName: The name of the app to list deployments for
    """
    return client.list_deployments(appName)


@mcp.tool(description="Get release history for a deployment")
def getDeploymentHistory(appName: str, deploymentName: str) -> dict[str, Any]:
    """Get the release history for a specific deployment.

    Args:
        appName: The name of the app
        deploymentName: The name of the deployment
    """
    return client.get_deployment_history(appName, deploymentName)
