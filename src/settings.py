import os


class CodepushSettings:
    def __init__(self):
        self.codepush_api_url = os.environ.get(
            "CODEPUSH_API_URL", "https://codepush.pro"
        )
        self.access_key = os.environ.get("CODEPUSH_ACCESS_KEY")

    @property
    def access_key_configured(self) -> bool:
        return self.access_key is not None

    def get_access_key(self) -> str:
        if not self.access_key:
            raise ValueError("CODEPUSH_ACCESS_KEY environment variable is not set")
        return self.access_key
