import hashlib
from datetime import datetime

class AuthorizationException(Exception):
    def __init__(self, *args) :
        super().__init__(*args)
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"AuthorizationException - {self.message}"
        else:
            return "AuthorizationException."

class AuthorizeBase:
    
    def __init__(self):
        pass

    def prepare(self, *kwargs) -> str:
        raise NotImplemented()

    def authorize(self, *kwargs) -> dict:
        raise NotImplemented()


class NonceGenerator:
    @staticmethod
    def generate_nonce() -> str:

        now = datetime.now()
        now_date = now.date()
        now_time = now.time()

        (quotient ,remainder) = divmod(now_time.minute, 15)

        new_datetime = datetime(
            now_date.year, now_date.month, now_date.day, now_time.hour, quotient * 15, 0)

        timestamp = str(new_datetime.timestamp())
        hash = hashlib.sha1(f"secret - {timestamp})".encode("utf8"))
        return hash.hexdigest()