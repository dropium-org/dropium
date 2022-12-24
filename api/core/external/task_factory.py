from .object_factory import ObjectFactory
from .task_verifiers import DiscordVerifier, TwitterVerifier, TaskVerifier,OnChainVerifier

import sys
sys.path.append("..")
from core.db.constants import TaskType

class TaskFactory(ObjectFactory):
    def __init__(self):
        super().__init__()

    def register_tasks(self):

        self.register(TaskType.DISCORD_JOIN_SERVER, DiscordVerifier)
        self.register(TaskType.TWITTER_SHARE_POST, TwitterVerifier)
        self.register(TaskType.TWITTER_FOLLOW, TwitterVerifier)
        self.register(TaskType.TWITTER_LIKE_POST, TwitterVerifier)
        self.register(TaskType.SOL_BALANCE, OnChainVerifier)
        self.register(TaskType.TOKEN_BALANCE, OnChainVerifier)

    def create(self, key, **kwargs) -> TaskVerifier:
        return super().create(key, **kwargs)


task_factory: TaskFactory = TaskFactory()
task_factory.register_tasks()
