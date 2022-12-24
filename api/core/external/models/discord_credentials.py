from .base import OAuthCredential

class DiscordCredentials(OAuthCredential):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

