from core.external import task_factory
from core.db.task_repository import TaskRepository
from core.db.user_repository import UserRepository
from core.db.constants import TaskType
from os import environ as env
from .exceptions import ResourceNotFoundException
import json
import sys
sys.path.append("..")


class TaskService:
    def __init__(self, config=None):
        env_config = env.get("DB_CONFIG", "")
        _config = json.loads(env_config) if env_config else config
        self._task_repository = TaskRepository(env.get("DB_CONFIG", _config))
        self._user_repository = UserRepository(env.get("DB_CONFIG", _config))

    # oracle
    def verify_task(self, task_id, user_id):

        # get task by id
        task = self._task_repository.get_task_by_task_id(id=task_id)

        if not task:
            raise ResourceNotFoundException("Task not found")

        task_type: TaskType = TaskType.from_str(task['type'])

        # get external account by user_id and task type
        external_account = self._user_repository.get_external_account_by_user_id_and_type(
            user_id=user_id, type=task_type)

        if not external_account:
            raise ResourceNotFoundException("External account not found")


        task_verifier = task_factory.create(task_type)

        return task_verifier.verify({
            "task": task["extra"],
            "account": external_account
        })

    def get_task_by_task_id(self, task_id):
        return self._task_repository.get_task_by_task_id(id=task_id)

    def get_all_tasks_of_quest(self, task_id):
        return self._task_repository.get_all_tasks_of_quest(id=task_id)

    def update_task(self, request):
        self._task_repository.update_task(request=request)

        return self._task_repository.get_task_by_task_id(id=request['id'])

    def create_task(self, request):
        new_task = self._task_repository.create_task(request=request)

        return self._task_repository.get_task_by_task_id(id=new_task)
