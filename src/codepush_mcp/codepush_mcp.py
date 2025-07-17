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


@mcp.tool(
    description="Verify that the CodePush access key is valid and the service is accessible"
)
def auth() -> dict[str, Any]:
    """Verify that the configured access key is valid."""
    client = _get_client()
    return client.authenticate()


@mcp.tool(
    description="Get information about the currently authenticated CodePush user account"
)
def whoami() -> dict[str, Any]:
    """Get information about the current authenticated user."""
    client = _get_client()
    return client.get_account_info()


@mcp.tool(
    description="List all CodePush applications available to the authenticated user with their collaborators and deployment names"
)
def listApps() -> dict[str, Any]:
    """List all CodePush apps available to the authenticated user."""
    client = _get_client()
    return client.list_apps()


@mcp.tool(
    description="List all deployments for a specific app, showing deployment names, keys, IDs, and current package information including metrics (active users, downloads, failures), app version, package size, upload time, and release label"
)
def listDeployments(appName: str) -> dict[str, Any]:
    """List all deployments for a specific app.

    Args:
        appName: The name of the app to list deployments for
    """
    client = _get_client()
    return client.list_deployments(appName)


@mcp.tool(
    description="Get detailed information about the current active package in a deployment, including metrics like active users, downloads, failures, app version, and rollout status"
)
def getDeploymentInfo(appName: str, deploymentName: str) -> dict[str, Any]:
    """Get a detailed summary of the latest package in a deployment.

    Args:
        appName: The name of the app
        deploymentName: The name of the deployment
    """
    client = _get_client()
    response = client.list_deployments(appName)
    deployments = response.get("deployments", [])

    for deployment in deployments:
        if deployment["name"] == deploymentName:
            return deployment

    return {"error": f"Deployment '{deploymentName}' not found in app '{appName}'"}


@mcp.tool(
    description="Compare two deployments within the same app side-by-side, showing differences in metrics, package versions, sizes, and deployment status"
)
def compareDeployments(
    appName: str, deployment1: str, deployment2: str
) -> dict[str, Any]:
    """Compare two deployments of an app.

    Args:
        appName: The name of the app
        deployment1: The first deployment to compare
        deployment2: The second deployment to compare
    """
    client = _get_client()
    response = client.list_deployments(appName)
    deployments = response.get("deployments", [])

    dep1_data = None
    dep2_data = None

    for deployment in deployments:
        if deployment["name"] == deployment1:
            dep1_data = deployment
        elif deployment["name"] == deployment2:
            dep2_data = deployment

    if not dep1_data:
        return {"error": f"Deployment '{deployment1}' not found"}
    if not dep2_data:
        return {"error": f"Deployment '{deployment2}' not found"}

    return {"comparison": {deployment1: dep1_data, deployment2: dep2_data}}


@mcp.tool(
    description="Get the complete release history for a specific deployment, showing all previous versions with upload times, metrics, and package details"
)
def getDeploymentHistory(appName: str, deploymentName: str) -> dict[str, Any]:
    """Get the release history for a specific deployment.

    Args:
        appName: The name of the app
        deploymentName: The name of the deployment
    """
    client = _get_client()
    return client.get_deployment_history(appName, deploymentName)


@mcp.tool(
    description="Get the list of releases within a deployment sorted by active users."
)
def getTopActiveReleases(appName: str, deploymentName: str) -> dict[str, Any]:
    """Get releases in a deployment sorted by active users.

    Args:
        appName: The name of the app
        deploymentName: The name of the deployment
    """
    client = _get_client()
    response = client.get_deployment_history(appName, deploymentName)
    history = response.get("history", []) if isinstance(response, dict) else response

    # Sort by active users (descending)
    sorted_releases = sorted(
        history, key=lambda x: x.get("metrics", {}).get("active", 0), reverse=True
    )

    return {"topActiveReleases": sorted_releases, "deploymentName": deploymentName}
