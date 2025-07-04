from typing import Any
from urllib.parse import urljoin
import requests


class CodePushClient:
    def __init__(self, server_url: str, access_key: str):
        self.base_url = server_url
        self.access_key = access_key

    def _get_headers(self) -> dict[str, str]:
        """Get the authorization headers."""
        return {"Authorization": f"Bearer {self.access_key}"}

    def authenticate(self) -> dict[str, Any]:
        """Verify access key validity."""
        url = urljoin(self.base_url, "/authenticated")
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_account_info(self) -> dict[str, Any]:
        """Get current user information."""
        url = urljoin(self.base_url, "/account")
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def list_apps(self) -> dict[str, Any]:
        """List all CodePush apps."""
        url = urljoin(self.base_url, "/apps")
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def list_deployments(self, app_name: str) -> dict[str, Any]:
        """List deployments for an app."""
        url = urljoin(self.base_url, f"/apps/{app_name}/deployments")
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_deployment_history(
        self, app_name: str, deployment_name: str
    ) -> dict[str, Any]:
        """Get release history for a deployment."""
        url = urljoin(
            self.base_url, f"/apps/{app_name}/deployments/{deployment_name}/history"
        )
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()
