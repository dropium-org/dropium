# Twitter API v2 calls: https://developer.twitter.com/apitools/api?endpoint=%2F2%2Ftweets%2F%7Bid%7D%2Fretweeted_by&method=get

import requests
import os
import json
from tweepy.auth import OAuth2Session


class TwitterAuth:
    def __init__(self, client_id, secret, redirect_uri, scopes):
        self.oauth2 = OAuth2Session(
            client_id=client_id,
            redirect_uri=redirect_uri,
            scope=scopes,
        )
        self._client_secret = secret
        self.base_url = "https://api.twitter.com/2/users"

    def exchange_code(self, code):
        return self.oauth2.fetch_token(
            "https://api.twitter.com/2/oauth2/token",
            code=code,
            include_client_id=True,
            code_verifier="code_verifier"
        )

from tweepy import API

class TwitterUser:
    def __init__(self):
        self.base_url = "https://api.twitter.com/2/users"

    # Returns User object of a username
    def get_current_user(self):
        url = f"{self.base_url}/me"
        params = {"user.fields": "profile_image_url"}
        return build_request("GET", url, self.headers, params)

    # Returns User object of a username
    def get_user_by_username(self, username):
        url = f"{self.base_url}/by/username/{username}"
        params = {"user.fields": "created_at"}
        return build_request("GET", url, self.headers, params)

    # Returns User object of a username
    def get_user_by_user_id(self, user_id):
        url = f"{self.base_url}/{user_id}"
        params = {"user.fields": "created_at"}
        return build_request("GET", url, self.headers, params)

    # Returns User objects that user_id are following
    def get_following_list_by_user_id(self, user_id):
        url = f"{self.base_url}/{user_id}/following"
        params = {"user.fields": "created_at"}
        return build_request("GET", url, self.headers, params)

    # Returns Tweet objects liked by user_id
    def get_liked_tweet_by_user_id(self, user_id, bearer_token):
        url = f"{self.base_url}/{user_id}/liked_tweets"
        return build_request("GET", url, {"Authorization": f"Bearer {bearer_token}"})

    # Returns User's tweet timeline. Note: RT = retweet
    def get_tweet_timeline_by_user_id(self, user_id):
        url = f"{self.base_url}/{user_id}/tweets"
        return build_request("GET", url, self.headers)


class TwitterTweet:
    def __init__(self, bearer_token):
        self.BEARER = bearer_token
        self.headers = {
            "Authorization": f"Bearer {bearer_token}"
        }
        self.base_url = "https://api.twitter.com/2/tweets"

    # Returns User objects that have liked the provided Tweet ID
    def get_liked_tweet_by_tweet_id(self, tweet_id):
        url = f"{self.base_url}/{tweet_id}/liking_users"
        return build_request("GET", url, self.headers)

    # Returns User objects that have retweeted the provided Tweet ID
    def get_retweeted_tweet_by_tweet_id(self, tweet_id):
        url = f"{self.base_url}/{tweet_id}/retweeted_by"
        return build_request("GET", url, self.headers)


def build_request(method, url, headers, params=None):
    response = requests.request(
        method=method, url=url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


if __name__ == "__main__":
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAHhJjwEAAAAA8awKSSYn%2BABD2MXeqOjefmuZzV8%3D1PCx0d0lZr6q0osuhRAKX8tMkVdY2nOBLma1Z1k6AlGVcpoWly"
    twu = TwitterTweet(bearer_token=bearer_token)
    # user_id = twu.get_user_by_username("NotoriousWicked")["data"]["id"]
    try:
        json_response = twu.get_liked_tweet_by_tweet_id('160591630799143')
    except Exception as e:
        print(e)

    with open("result.json", "w") as f:
        f.write(json.dumps(json_response, indent=4, sort_keys=True))
