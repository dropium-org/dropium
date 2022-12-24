from .authorize_base import AuthorizeBase, AuthorizationException, NonceGenerator
from base58 import b58decode
from solana.publickey import PublicKey
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

class AuthorizeSolanaWallet(AuthorizeBase):
    def __init__(self):
        super(AuthorizeBase).__init__()

    def generate_message(self, identifier):
        nonce = NonceGenerator.generate_nonce()
        return f'Sign this message for authenticating with your wallet - {identifier}. Nonce: {str(nonce)}'

    def prepare(self, *kwargs) -> str:
        data = kwargs[0]
        return self.generate_message(data["identifier"])

    def authorize(self, *kwargs) -> dict:
        data = kwargs[0]
        signature = data["signature"]
        message = data["message"]
        public_key = data["identifier"]
        if(self.generate_message(data["identifier"]) == message):
            raise AuthorizationException("Invalid message")

        try:
            verify_key = VerifyKey(bytes(PublicKey(public_key)))
            verify_message = verify_key.verify(
                smessage=bytes(message, "utf8"),
                signature=b58decode(bytes(signature, "utf8")),
            )

            if verify_message.decode("utf-8") == message:
                return {
                    "signature": signature,
                    "message": message,
                    "public_key": public_key
                }
            else:
                raise AuthorizationException("Verify message not match.")
        except (BadSignatureError, ValueError) as e:
            raise AuthorizationException(str(e))
