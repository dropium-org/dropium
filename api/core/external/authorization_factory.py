
from .object_factory import ObjectFactory
from .authorization_modules import AuthorizeDiscord, AuthorizeTwitter, AuthorizeSolanaWallet, AuthorizeBase

import sys
sys.path.append("..")
from core.db.constants import AuthorizeType

class AuthorizationFactory(ObjectFactory):
    def __init__(self):
        super().__init__()

    def register_tasks(self):

        self.register(AuthorizeType.SOLANA_WALLET, AuthorizeSolanaWallet)
        self.register(AuthorizeType.DISCORD, AuthorizeDiscord)
        self.register(AuthorizeType.TWITTER, AuthorizeTwitter)

    def create(self, key, **kwargs) -> AuthorizeBase:
        return super().create(key, **kwargs)


auth_factory: AuthorizationFactory = AuthorizationFactory()
auth_factory.register_tasks()
