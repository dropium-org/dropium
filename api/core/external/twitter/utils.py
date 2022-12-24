from tweepy.auth import OAuth2Session


class TwitterUtils:

    @staticmethod
    def generate_auth_url(client_id, secret, redirect_url, scopes, state) -> str:
        oauth2_user_handler = OAuth2Session(
            client_id=client_id,
            redirect_uri=redirect_url,
            scope=scopes,
            state=state
        )

        authorization_url, _ = oauth2_user_handler.authorization_url(
            "https://twitter.com/i/oauth2/authorize",
            code_challenge=oauth2_user_handler._client.create_code_challenge(
                "code_verifier", "S256"
            ), code_challenge_method="S256",

        )
        return authorization_url