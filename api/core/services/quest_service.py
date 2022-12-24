from core.db.quest_repository import QuestRepository
from core.db.task_repository import TaskRepository
from enum import Enum
from os import environ as env
import json
import sys
sys.path.append("..")


class TaskStatus(Enum):
    IS_NOT_VERIFIED = 0
    IS_VERIFIED = 1


class QuestService:
    def __init__(self, config=None):
        env_config = env.get("DB_CONFIG", "")
        _config = json.loads(env_config) if env_config else config
        self.quest_repository = QuestRepository(_config)
        self.task_repository = TaskRepository(_config)

    # oracle
    def verify_quest(self, request):
        # get tasks
        tasks = self.task_repository.get_user_task_entries(
            user_id=request['user_id'], quest_id=request['quest_id'])

        # loop tasks
        for task in tasks:
            if task['status'] == TaskStatus.IS_NOT_VERIFIED:
                return False
        return True

    def get_all_quests(self):
        return self.quest_repository.get_all_quests()

    def get_quest_by_id(self, quest_id):
        return self.quest_repository.get_quest_by_id(id=quest_id)

    def update_quest(self,id, slug, update_data):
        self.quest_repository.update_quest(id=id,slug=slug, update_data=update_data)

        return self.quest_repository.get_quest_by_id(id=id)

    def create_quest(self, slug, data):
        new_id = self.quest_repository.create_quest(slug = slug, data=data)

        return self.quest_repository.get_quest_by_id(id=new_id)

    def get_quest_by_user(self,user_id):
        return self.quest_repository.get_quest_by_user(user_id=user_id)
    
    def get_status_of_quest_by_user(self,quest_id,user_id):
        return self.quest_repository.get_status_of_quest_id_by_user(quest_id=quest_id,user_id=user_id)

