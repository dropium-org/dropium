from .base import TaskVerifier, TaskVerifyException
from ..discord import DiscordConnector
from ..models.discord_credentials import DiscordCredentials

from os import environ as env
import json


class DiscordVerifier(TaskVerifier):
    def __init__(self):
        super().__init__()

        env_config = env.get("DISCORD_CONFIG", "")
        _config = json.loads(env_config)

        self._redirect_uri = _config["redirect_uri"]
        self._client_id = _config["client_id"]
        self._client_secret = _config["client_secret"]
        self._scopes = _config["scopes"]

        self._connector = DiscordConnector(
            client_id=self._client_id,
            client_secret=self._client_secret,
            redirect_uri=self._redirect_uri)

    def populate_default_params(self, **kwargs) -> dict:
        return {
            "account": kwargs["account"],
            "task": kwargs["task"]
        }


class DiscordJoinServerTaskVerifier(DiscordVerifier):
    def __init__(self):
        super().__init__()


    def handle_verify(self, **kwargs) -> bool:
        credentials = DiscordCredentials.from_dict(kwargs['account']["extra"])

        guild_id = kwargs["task"]["guild_id"]

        verified = self._connector.is_guild_joined_by_user(
            bearer_token=credentials.access_token,
            guild_id=guild_id
        )

        if not verified:
            raise TaskVerifyException("Verify Join Discord failed")

        return verified
