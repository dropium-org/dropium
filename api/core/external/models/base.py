from collections import namedtuple


class OAuthCredential(namedtuple('DiscordCredentials', ['scope', 'expires_in', 'token_type', 'access_token', 'refresh_token'])):
    def __new__(cls, scope, expires_in, token_type, access_token, refresh_token):
        return super(OAuthCredential, cls).__new__(cls, scope, expires_in, token_type, access_token, refresh_token)

    # method that that convert dict to DiscordCredentials

    @classmethod
    def from_dict(cls, data):
        return cls(
            scope=data['scope'],
            expires_in=data['expires_in'],
            token_type=data['token_type'],
            access_token=data['access_token'],
            refresh_token=data['refresh_token']
        )
