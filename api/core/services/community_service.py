from core.db.community_repository import CommunityRepository
from os import environ as env
import json
import sys
sys.path.append("..")


class CommunityService:
    def __init__(self, config=None):
        env_config = env.get("DB_CONFIG", "")
        _config = json.loads(env_config) if env_config else config
        self.community_repository = CommunityRepository(_config)

    def get_all_communities(self):
        return self.community_repository.get_all_communities()

    def get_community_by_slug(self, slug):
        return self.community_repository.get_community_by_slug(slug = slug)

    def create_community(self, user_id, data):
        new_community = self.community_repository.create_community(
            owner_id=user_id, data=data)
        return self.community_repository.get_community_by_slug(slug=data['urlSlug'])

    def update_community(self, slug, data):
        update = self.community_repository.update_community(slug=slug, data=data)
        return self.community_repository.get_community_by_slug(slug=slug)
