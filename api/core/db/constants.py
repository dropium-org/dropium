from enum import Enum


class TaskType(Enum):
    # discord
    DISCORD_JOIN_SERVER = "0"

    # twitter
    TWITTER_LIKE_POST = "10"
    TWITTER_SHARE_POST = "11"
    TWITTER_FOLLOW = "12"

    # telegram

    #onchain
    SOL_BALANCE = "20"
    TOKEN_BALANCE = "21"

    # others

    # methods

    def is_discord_task(self) -> bool:
        return self == self.DISCORD_JOIN_SERVER

    def is_twitter_task(self) -> bool:
        return self == self.TWITTER_LIKE_POST or self == self.TWITTER_SHARE_POST or self == self.TWITTER_FOLLOW

    def is_onchain_task(self) -> bool:
        return self == self.SOL_BALANCE or self == self.TOKEN_BALANCE

    # method that return TaskType Enum from value   
    @classmethod
    def from_str(self, label):
        if label in ('0', 0):
            return self.DISCORD_JOIN_SERVER
        elif label in ('10', 10):
            return self.TWITTER_LIKE_POST
        elif label in ('11', 11):
            return self.TWITTER_SHARE_POST
        elif label in ('12', 12):
            return self.TWITTER_FOLLOW
        elif label in ('20', 20):
            return self.SOL_BALANCE
        elif label in ('21', 21):
            return self.TOKEN_BALANCE
        else:
            raise NotImplementedError()

class AuthorizeType(Enum):
    SOLANA_WALLET = "100"

    DISCORD = "200"

    TWITTER = "300"

    def direct_authorize_allowed(self) -> bool:
        return self == self.SOLANA_WALLET

    def connect_account_authorize_allowed(self) -> bool:
        return self == self.TWITTER or self == self.DISCORD
    
    @classmethod
    def from_str(self, label):
        if label in ('100', 100):
            return self.SOLANA_WALLET
        elif label in ('200', 200):
            return self.DISCORD
        elif label in ('300', 300):
            return self.TWITTER
        else:
            raise NotImplementedError()



class RewardType(Enum):
    TOKENS = "0"
    NFT = "1"
    WHITELIST = "2"

class Eligibility(Enum):
    ALL = "0"

class QuestStatus(Enum):
    DRAFT = "0"
    SCHEDULED = "1"
    ONGOING = "2"
    COMPLETED = "3"

class SolanaCluster(Enum):
    MAINNET = "mainnet-beta"
    DEVNET = "devnet"
    TESTNET = "testnet"