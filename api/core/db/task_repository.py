from .base_repository import BaseRepository
import datetime


class TaskRepository(BaseRepository):
    def __init__(self, config):
        super().__init__(config)

    _get_task_by_task_id_script = '''
        SELECT id, `type`, extra, quest_id
        FROM quest_task 
        WHERE id = %s;
    '''

    def get_task_by_task_id(self, id: int):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._get_task_by_task_id_script), (id,))
                return cursor.fetchall()

    _get_all_tasks_of_quest_script = '''
        SELECT id, `type`, extra, quest_id
        FROM quest_task 
        WHERE quest_id = %s;
    '''

    def get_all_tasks_of_quest(self, id: int):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._get_all_tasks_of_quest_script), (id,))
                return cursor.fetchall()

    _create_task_script = f'''
        INSERT INTO quest_task (`type`, extra, quest_id, created_at, updated_at) VALUES (%s,%s,%s,%s,%s); 
    '''

    def create_task(self, request):
        time = datetime.datetime.now()
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._create_task_script), (request['type'], request['extra'], request['quest_id'], time, time))
                connection.commit()
                return cursor.lastrowid

    _create_task_script = f'''
        INSERT INTO quest_task (`type`, extra, quest_id, created_at, updated_at) VALUES (%s,%s,%s,%s,%s); 
    '''

    def create_tasks(self, tasks):
        time = datetime.datetime.now()
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                for task in tasks:
                    cursor.execute(
                    (self._create_task_script), (task['type'], task['extra'], task['quest_id'], time, time))
                connection.commit()
                return cursor.lastrowid

    _update_task_script = f"""
        UPDATE quest_task 
        SET `type`= %s,extra= %s,quest_id= %s 
        WHERE id = %s;
    """

    def update_task(self, request):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._update_task_script), (request['type'], request['extra'], request['quest_id'], request['id']))
                connection.commit()

    _insert_user_tasks_of_quest_script = f"""
        INSERT INTO user_task_entry (quest_id,quest_entry_id,task_id,status,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s)
    """

    def insert_user_tasks_of_quest(self, request):  # thiếu user_id
        time = datetime.datetime.now()
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._insert_user_tasks_of_quest_script), (request['quest_id'], request['quest_entry_id'], request['task_id'], request['status'], time, time))
                connection.commit()
                return cursor.lastrowid

    _update_user_task_entry_script = f"""
        UPDATE user_task_entry
        SET status=%s,updated_at =%s
        WHERE user_id = %s AND task_id = %s;
    """

    def update_user_task_entry(self, request):
        time = datetime.datetime.now()
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._update_user_task_entry_script), (request['status'], time, request['user_id'], request['task_id']))
                connection.commit()

    _get_user_task_entries_script = f"""
        SELECT quest_id,quest_entry_id,task_id,status
        FROM user_task_entry
        WHERE user_id = %s and quest_id = %s
    """

    def get_user_task_entries(self, user_id, quest_id):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._update_user_task_entry_script), (user_id, quest_id))
                connection.fetchall()

