from .base import TaskVerifier, TaskVerifyException
from ..twitter import TwitterUser, TwitterTweet
from ..models import TwitterCredentials
import json

from os import environ as env

class TwitterVerifier(TaskVerifier):
    def __init__(self):
        super().__init__()

        env_config = env.get("TWITTER_CONFIG", "")
        _config = json.loads(env_config) 

        self._redirect_uri = _config["redirect_uri"]
        self._client_id = _config["client_id"]
        self._client_secret = _config["client_secret"]
        self._scopes = _config["scopes"]
        

        self._twt_tweet = TwitterTweet(
            client_id=self._client_id,
            client_secret=self._client_secret,
            redirect_uri=self._redirect_uri)

        self._twt_user = TwitterUser(
            client_id=self._client_id,
            client_secret=self._client_secret,
            redirect_uri=self._redirect_uri)

    def populate_default_params(self, **kwargs) -> dict:
        return {
            "account": kwargs["account"],
            "task": kwargs["task"]
        }

class TwitterLikeTweetVerifier(TwitterVerifier):
    def __init__(self):
        super().__init__()

    def handle_verify(self, **kwargs) -> bool:
        tweet_id = self._parameters['task']['tweet_id']
        user_id = self._parameters['account']['external_id']
        
        credentials = TwitterCredentials.from_dict(kwargs['account']["extra"])


        json_response = self._twt_tweet.get_liked_tweet_by_user_id(
                user_id=tweet_id)

        for tweet in json_response['data']:
            if tweet['id'] == tweet_id:
                return True
        return False



class TwitterLikeTweetVerifier(TwitterVerifier):

    def handle_verify(self, **kwargs) -> bool:
        tweet_id = self._parameters['task']['tweet_id']
        user_id = self._parameters['account']['external_id']
        
        credentials = TwitterCredentials.from_dict(kwargs['account']["extra"])


        json_response = self._twt_tweet.get_liked_tweet_by_user_id(
                user_id=tweet_id)

        for tweet in json_response['data']:
            if tweet['id'] == tweet_id:
                return True
        return False

class TwitterLikeTweetVerifier(TwitterVerifier):

    def handle_verify(self, **kwargs) -> bool:
        twu = TwitterUser(bearer_token="")
        twt = TwitterTweet(bearer_token="")
        if kwargs['type'] == 10:
            json_response = twu.get_liked_tweet_by_user_id(
                user_id=kwargs['user_twitter_id'])
            for tweet in json_response['data']:
                if tweet['id'] == kwargs['id']:
                    return True
            return False
        if kwargs['type'] == 11:
            json_response = twt.get_retweeted_tweet_by_tweet_id(
                tweet_id=kwargs['tweet_id'])
            for tweet in json_response['data']:
                if tweet['id'] == kwargs['user_twitter_id']:
                    return True
            return False
        if kwargs['type'] == 12:
            json_response = twu.get_following_list_by_user_id(
                user_id=kwargs['user_twitter_id'])
            for twit in json_response['data']:
                if twit['id'] == kwargs['follow_user']:
                    return True
            return False

        # if fail
        raise NotImplementedError()
class TwitterLikeTweetVerifier(TaskVerifier):

    def handle_verify(self, **kwargs) -> bool:
        twu = TwitterUser(bearer_token="")
        twt = TwitterTweet(bearer_token="")
        if kwargs['type'] == 10:
            json_response = twu.get_liked_tweet_by_user_id(
                user_id=kwargs['user_twitter_id'])
            for tweet in json_response['data']:
                if tweet['id'] == kwargs['id']:
                    return True
            return False
        if kwargs['type'] == 11:
            json_response = twt.get_retweeted_tweet_by_tweet_id(
                tweet_id=kwargs['tweet_id'])
            for tweet in json_response['data']:
                if tweet['id'] == kwargs['user_twitter_id']:
                    return True
            return False
        if kwargs['type'] == 12:
            json_response = twu.get_following_list_by_user_id(
                user_id=kwargs['user_twitter_id'])
            for twit in json_response['data']:
                if twit['id'] == kwargs['follow_user']:
                    return True
            return False

        # if fail
        raise NotImplementedError()