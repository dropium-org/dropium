from .base import OAuthCredential

class TwitterCredentials(OAuthCredential):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
