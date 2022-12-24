from urllib.parse import urlencode,quote


class DiscordUtils:
    OAUTH_BASE_URL = "https://discord.com/api/oauth2/authorize"

    @staticmethod
    def generate_auth_url(client_id, redirect_uri, response_type="code", scopes: list[str] = []):
        scope_str = " ".join(scopes)
        params = {
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "response_type": response_type,
            "scope": scope_str

        }
        encoded_params = urlencode(params, quote_via=quote)
        return DiscordUtils.OAUTH_BASE_URL + f"?{encoded_params}"
