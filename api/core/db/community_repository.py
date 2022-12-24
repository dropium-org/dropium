from .base_repository import BaseRepository
import datetime
import json

class CommunityRepository(BaseRepository):
    def __init__(self, config):
        super().__init__(config)

    _get_all_communities_script = f"""
        SELECT url_slug, name, logo, description, cover,
            verified, owner_id
        FROM community;
    """

    def get_all_communities(self):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._get_all_communities_script))
                return cursor.fetchall()

    
    _get_community_by_id_script = f"""
        SELECT url_slug, name, logo, description, cover,
            verified, owner_id
        FROM community
        WHERE url_slug = %s;
    """

    def get_community_by_slug(self,slug):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._get_community_by_id_script),(slug,))
                return cursor.fetchone()

    
    _create_community_script = f"""
        INSERT INTO community ( url_slug, name, logo, description, cover,
            owner_id, created_at,updated_at)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
    """

    def create_community(self,owner_id,data):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:

                now = datetime.datetime.now()
                cursor.execute(
                    (self._create_community_script),
                    ( 
                        data['urlSlug'],
                        data['name'],
                        data['logo'],
                        data['description'],
                        data['cover'],
                        owner_id,
                        now,
                        now
                        ))
                community_id = cursor.lastrowid
                connection.commit()
                return community_id
    

    updated_community_script = f"""
        UPDATE community
        SET url_slug = %s, name = %s, logo = %s, description = %s, cover = %s, updated_at = %s
        WHERE url_slug = %s;
    """

    def update_community(self,slug,data):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:

                now = datetime.datetime.now()
                cursor.execute(
                    (self.updated_community_script),
                    (
                        data['urlSlug'],
                        data['name'],
                        data['logo'],
                        data['description'],
                        data['cover'],
                        now,
                        slug
                        ))
                connection.commit()
