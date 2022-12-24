from .authorize_base import AuthorizeBase, AuthorizationException
from ..discord import DiscordUtils, DiscordConnector

import json

from os import environ as env

class AuthorizeDiscord(AuthorizeBase):
    def __init__(self):
        super(AuthorizeBase).__init__()
        env_config = env.get("DISCORD_CONFIG", "")
        _config = json.loads(env_config) 
        
        self._redirect_uri = _config["redirect_uri"]
        self._client_id = _config["client_id"]
        self._client_secret = _config["client_secret"]
        self._scopes = _config["scopes"]

    def prepare(self, *kwargs) -> str:

        return DiscordUtils.generate_auth_url(
            self._client_id,
            self._redirect_uri,
            scopes=self._scopes
        )

    def authorize(self, *kwargs) -> dict:
        data = kwargs[0]
        discord = DiscordConnector(
            client_id=self._client_id,
            client_secret=self._client_secret,
            redirect_uri=self._redirect_uri)

        token = discord.exchange_code(data["code"])

        if token and 'error' in token and token["error"]=="invalid_grant":
            raise AuthorizationException(token["error_description"])
        account = discord.get_current_user(bearer_token=token["access_token"])

        external_id = account["id"]
        avatar_hash:str = account["avatar"]
        extension = "gif" if avatar_hash.startswith("a_") else "png"
        external_url =f"https://cdn.discordapp.com/avatars/{external_id}/{avatar_hash}.{extension}"
        return {"extra": token, "account": {
            "external_id": external_id,
            "external_username": account["username"],
            "external_name": account["username"],
            "external_url": external_url
        }}
