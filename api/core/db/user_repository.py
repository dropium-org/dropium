from .base_repository import BaseRepository
import json
from .constants import TaskType

class UserRepository(BaseRepository):
    def __init__(self, config):
        super().__init__(config)

    _get_user_by_id_script = '''
        SELECT id, username, avatar, active 
        FROm user 
        WHERE id = %s;
    '''
    _get_user_by_id_include_externals_script = '''
        SELECT u.id, username, avatar, u.active, ca.id as connected_account_id, external_id, external_name, external_url, ca.type
        FROM user u
            INNER JOIN connect_account ca
            ON u.id = ca.user_id
        WHERE u.id = %s;
    '''

    def get_user_by_id(self, id: int, external_included: bool):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                if not external_included:
                    cursor.execute((self._get_user_by_id_script), (id,))
                    return cursor.fetchone()
                else:
                    cursor.execute(
                        (self._get_user_by_id_include_externals_script), (id,))
                    items = cursor.fetchall()
                    return self._parse_sql_rows_to_user(items)

    def _parse_sql_rows_to_user(self, rows):
        user = {}
        for index, element in enumerate(rows):
            if (index == 0):
                user["id"] = element["id"]
                user["username"] = element["username"]
                user["avatar"] = element["avatar"]
                user["connected_account"] = list()
            user["connected_account"].append({
                "type": element["type"],
                "external_id": element["external_id"],
                "external_username": element["external_name"],
                "external_avatar": element["external_url"],
            })
        return user

    _get_user_by_external_id_script = '''
        SELECT u.id, username, avatar, u.active, ca.id as connected_account_id, external_id, external_name, external_url, ca.type
        FROM user u
            INNER JOIN connect_account ca
            ON u.id = ca.user_id
        WHERE ca.external_id = %s
        AND type = %s;
    '''

    def get_user_by_external_id(self, external_id, type):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._get_user_by_external_id_script), (external_id, type))
                rows = cursor.fetchall()

                return self._parse_sql_rows_to_user(rows)

    _update_user_script = '''
        UPDATE user
        SET avatar = %s
        WHERE id = %s;
    '''

    def update_user(self, user_id: int, user: dict):
        with self._init_connection() as connection:
            with self.create_cursor(connection) as cursor:
                cursor.execute(
                    (self._update_user_script), (user["avatar"], user_id))
                connection.commit()

    _create_user_by_external_script = '''
        INSERT INTO user(username, active)
        VALUES (%s, 1);
    '''
    _create_connected_account_by_external_script = '''
        INSERT INTO connect_account(external_id, user_id, type,external_name, external_username,external_url, extra)
        VALUES  (%s,%s,%s,%s,%s,%s,%s); 
    '''

    def create_user_by_external(self, type, external_id, extra):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._create_user_by_external_script), (external_id,))

                cursor.execute(
                    (self._create_connected_account_by_external_script),
                    (
                        external_id,
                        cursor.lastrowid,
                        type,
                        external_id,
                        external_id,
                        "",
                        json.dumps(extra)
                    ))

                connection.commit()

    _upsert_connected_account_by_external_script = '''
        REPLACE INTO connect_account(external_id, user_id, type,external_name, external_username, external_url, extra)
        VALUES  (%s,%s,%s,%s,%s,%s,%s); 
    '''
    def upsert_external_account(self, user_id, type, name, username, url, external_id, extra):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._upsert_connected_account_by_external_script),
                    (
                        external_id,
                        user_id,
                        type,
                        name,
                        username,
                        url,
                        json.dumps(extra)
                    ))

                connection.commit()

    _remove_connected_account_by_external_script = '''
        DELETE FROM connect_account 
        WHERE   user_id = %s 
        AND type = %s; 
    '''

    def remove_external_account(self, user_id, type):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._remove_connected_account_by_external_script),
                    (
                        user_id,
                        type
                    ))

                connection.commit()
                return cursor.rowcount

    #get external account by user id and task type
    _get_external_account_by_user_id_and_task_type_script = '''
        SELECT external_id, external_name, external_url, extra
        FROM connect_account
        WHERE user_id = %s
        AND type = %s;
    '''

    def get_external_account_by_user_id_and_task_type(self, user_id, task_type:TaskType):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._get_external_account_by_user_id_and_task_type_script),
                    (
                        user_id,
                        task_type.value
                    ))

                data =cursor.fetchone()

                data["extra"] = json.loads(data["extra"])

                return data
        
        

