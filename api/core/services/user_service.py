from core.db.user_repository import UserRepository
from core.external.authorization_factory import auth_factory
from typing import Tuple
from os import environ as env
import json
import sys
from .exceptions import ResourceExistedException, ResourceNotFoundException
sys.path.append("..")


class UserService:
    def __init__(self, config=None):
        env_config = env.get("DB_CONFIG", "")
        _config = json.loads(env_config) if env_config else config
        self.user_repository = UserRepository(_config)

    def get_user_by_id(self, user_id, external_included):
        return self.user_repository.get_user_by_id(id=user_id, external_included=external_included)

    def update_user(self, user_id, user):
        self.user_repository.update_user(user_id=user_id, user=user)

        return self.user_repository.get_user_by_id(id=user_id, external_included=True)

    def bind_external_account(self, user_id, type, code, external_id, extra):

        authorizer = auth_factory.create(type)
        authorization_response = authorizer.authorize(
            {"type": type, "code": code, "external_id": external_id, "extra": extra})

        account = authorization_response["account"]

        user = self.user_repository.get_user_by_external_id(
            external_id=account["external_id"], type=type.value)

        if user and not user["id"] == user_id:
            raise ResourceExistedException()

        self.user_repository.upsert_external_account(
            user_id=user_id, 
            type=type.value, 
            external_id=account["external_id"], 
            name=account["external_name"],
            url=account["external_url"],
            username=account["external_username"],
            extra=authorization_response["extra"])

    def unbind_external_account(self, user_id, type):
        row_count = self.user_repository.remove_external_account(
            user_id, type)
        if row_count <1 :
            raise ResourceNotFoundException()

    def authorize_by_external(self, type, external_id, args):
        authorizer = auth_factory.create(type)
        extra = authorizer.authorize(args)

        user = self.user_repository.get_user_by_external_id(
            external_id=external_id, type=type.value)

        if (user):
            return user

        self.user_repository.create_user_by_external(
            type.value, external_id, extra)

        return self.user_repository.get_user_by_external_id(
            external_id=external_id, type=type.value)

    def prepare_auth(self, type, args):
        authorizer = auth_factory.create(type)
        return authorizer.prepare(args)
