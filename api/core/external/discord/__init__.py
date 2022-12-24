import requests
from .utils import DiscordUtils


class DiscordConnector:
    API_ENDPOINT = 'https://discord.com/api/v10'

    def __init__(self, redirect_uri, client_id, client_secret):
        self.redirect_uri = redirect_uri
        self.client_id = client_id
        self.client_secret = client_secret
    '''
    Response
    {
        "access_token": "f9A1dqGvjYT0YYFTA4Vp1WHZeGKbGs",
        "expires_in": 604800,
        "refresh_token": "RzU1RR6OGWQeGGEJR8KzB3lWA9HFe1",
        "scope": "guilds.members.read identify guilds email",
        "token_type": "Bearer"
    }
    '''

    def exchange_code(self, code):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        r = requests.post('%s/oauth2/token' %
                          self.API_ENDPOINT, data=data, headers=headers)
        return r.json()

    '''
    Response
    {
        "id": "394377155762716673",
        "username": "ravi",
        "avatar": "63a3356c5e88e1b34acf20006e02a5db",
        "avatar_decoration": None,
        "discriminator": "3934",
        "public_flags": 0,
        "flags": 0,
        "banner": "a_0c48bc88080eb5f6afb753c550dec3c9",
        "banner_color": "#000000",
        "accent_color": 0,
        "locale": "en-US",
        "mfa_enabled": False,
        "premium_type": 2,
        "email": "voasd123@gmail.com",
        "verified": True
    }
    '''

    def get_current_user(self, bearer_token=None):
        headers = {
            "Authorization": f"Bearer {bearer_token}"
        }
        r = requests.get(f'{self.API_ENDPOINT}/users/@me', headers=headers)
        return r.json()

    def get_guild_by_id(self, guild_id, bearer_token=None):
        headers = {
            "Authorization": f"Bearer {bearer_token}"
        }
        r = requests.get(
            f'{self.API_ENDPOINT}/guilds/{guild_id}', headers=headers)
        r.raise_for_status()
        return r.json()

    '''
    [
        {
            "id": "219564597349318656",
            "name": "ChillZone | Social • Egirls • Gaming • Fun • Emotes & Emojis • Anime • Nitro",
            "icon": "a_4d7cbd8bfd343055921cd3c5889ba65a",
            "owner": False,
            "permissions": "554154659329",
            "features": [
                "DISCOVERABLE",
                "COMMUNITY",
            ]
        },
    ]
    '''

    def get_user_guilds(self, bearer_token=None):
        headers = {
            "Authorization": f"Bearer {bearer_token}"
        }
        r = requests.get(
            f'{self.API_ENDPOINT}/users/@me/guilds', headers=headers)
        r.raise_for_status()
        return r.json()

    def get_guild_member(self, guild_id, member_id, bearer_token=None):
        headers = {
            "Authorization": f"Bearer {bearer_token}"
        }

        r = requests.get(
            f'{self.API_ENDPOINT}/guilds/{guild_id}/members/{member_id}', headers=headers)

        return r.json()

    def get_user_guild_member(self, guild_id, bearer_token=None):
        headers = {
            "Authorization": f"Bearer { bearer_token}"
        }
        r = requests.get(
            f'{self.API_ENDPOINT}/users/@me/guilds/{guild_id}/member', headers=headers)

        return r.json()

    def is_guild_joined_by_user(self, guild_id, bearer_token=None):
        try:
            joined_guilds = self.get_user_guilds(bearer_token)
            joined_guild_ids = [joined_guild["id"]
                                for joined_guild in joined_guilds]

            return str(guild_id) in joined_guild_ids
        except requests.exceptions.HTTPError as httpEx:
            print(httpEx)
            pass

    def if_user_has_roles_in_guild(self, guild_id, given_role_ids, bearer_token=None):
        try:
            guild_member = self.get_user_guild_member(guild_id, bearer_token)

            return all([str(given_role_id) in guild_member["roles"] for given_role_id in given_role_ids])
        except requests.exceptions.HTTPError as httpEx:
            print(httpEx)
            pass


if __name__ == "__main__":
    disc_connector = DiscordConnector(token="")

    print(disc_connector.get_current_user())
