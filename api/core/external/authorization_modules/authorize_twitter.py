from .authorize_base import AuthorizeBase, AuthorizationException, NonceGenerator
from ..twitter.utils import TwitterUtils
from ..twitter import TwitterAuth,TwitterUser
import json

from os import environ as env

class AuthorizeTwitter(AuthorizeBase):
    def __init__(self):
        super(AuthorizeBase).__init__()
        env_config = env.get("TWITTER_CONFIG", "")
        _config = json.loads(env_config) 

        self._redirect_uri = _config["redirect_uri"]
        self._client_id = _config["client_id"]
        self._client_secret = _config["client_secret"]
        self._scopes = _config["scopes"]
        
        self._state = NonceGenerator.generate_nonce()

        self._auth = TwitterAuth(
            self._client_id, self._client_secret, self._redirect_uri, self._scopes)
    def prepare(self, *kwargs) -> str:

        return TwitterUtils.generate_auth_url(
            self._client_id,
            self._client_secret,
            self._redirect_uri,
            scopes=self._scopes,
            state=self._state
        )

    def authorize(self, *kwargs) -> dict:
        data = kwargs[0]
        code = data["code"]
        try:
            token = self._auth.exchange_code(code)
            account = TwitterUser(token["access_token"]).get_current_user()
            account_data = account["data"]
            return {"extra": token, "account": {
                "external_id": account_data["id"],
                "external_username": account_data["username"],
                "external_name": account_data["name"],
                "external_url": account_data["profile_image_url"]
            }}
        except Exception as e:
            raise AuthorizationException(str(e))
