from .base_repository import BaseRepository
import datetime
import json

class QuestRepository(BaseRepository):
    def __init__(self, config):
        super().__init__(config)

    _get_all_quests_script = f"""
        SELECT q.id as quest_id, title, q.description as description, start_at, end_at, reward_type,
            reward_slots, network, eligibility, status,q.logo as quest_logo , c.url_slug as community_slug, c.name as community_name, c.logo as community_logo
        FROM quest q
            INNER JOIN community c
            ON q.community_slug = community_slug
    """

    def get_all_quests(self):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._get_all_quests_script))

                items = cursor.fetchall()
                if (len(items) == 0):
                    return []

                data = []
                for item in items:
                    data.append({
                    "id": item["quest_id"],
                    "title": item["title"],
                    "description": item["description"],
                    "start_at": item["start_at"],
                    "end_at": item["end_at"],
                    "reward_type": item["reward_type"],
                    "reward_slots": item["reward_slots"],
                    "network": item["network"],
                    "eligibility": item["eligibility"],
                    "community": {
                        "name": item["community_name"],
                        "logo": item["community_logo"]
                    },
                    "status": item["status"],
                    "logo": item["quest_logo"]
                })

                return data

    _get_quest_by_id_script = '''
        SELECT q.id as quest_id, title, q.description, start_at, end_at, reward_type,
            reward_slots, network, eligibility, status,q.logo , c.url_slug as community_slug, c.name as community_name, c.logo as community_logo
        FROM quest q
            INNER JOIN community c
            ON q.community_slug = community_slug


        WHERE q.id = %s;
    '''

    _get_all_tasks_of_quest_script = '''
        SELECT id, `type`, extra
        FROM quest_task 
        WHERE quest_id = %s;
    '''

    def get_quest_by_id(self, id: int):  # thiếu task
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True,buffered=True) as cursor:
                cursor.execute(
                    (self._get_all_tasks_of_quest_script), (id,))
                tasks = cursor.fetchall()

                cursor.execute(
                    (self._get_quest_by_id_script), (id,))
                data = cursor.fetchone()
                # print(id,data)
                quest = {}
                quest["id"] = data["quest_id"]
                quest["title"] = data["title"]
                quest["description"] = data["description"]
                quest["start_at"] = data["start_at"]
                quest["end_at"] = data["end_at"]
                quest["reward_type"] = data["reward_type"]
                quest["reward_slots"] = data["reward_slots"]
                quest["network"] = data["network"]
                quest["eligibility"] = data["eligibility"]
                quest["community"] = {}
                quest["community"]["url_slug"] = data["community_slug"]
                quest["community"]["name"] = data["community_name"]
                quest["community"]["logo"] = data["community_logo"]
                quest["status"] = data["status"]
                quest["logo"] = data["logo"]
                quest["tasks"] = tasks

                print(quest,123)
                return quest

    _create_quest_script = f'''
        INSERT INTO quest (title, description,start_at,
        end_at, reward_type, reward_slots, network, eligibility,
        community_slug, status, created_at, updated_at,logo)

         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
    '''
    _create_quest_task_script = f'''
        INSERT INTO quest_task (`type`, extra, quest_id, created_at, updated_at) 
        VALUES (%s,%s,%s,%s,%s);
    '''

    def create_quest(self, slug, data):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:

                now = datetime.datetime.now()
                print(data)
                cursor.execute(
                    (self._create_quest_script),
                    (
                        data['title'],
                        data['description'],
                        data['startAt'],
                        data['endAt'],
                        data['rewardType'],
                        data['rewardSlots'],
                        data['network'],
                        data['eligibility'],
                        slug,
                        0,
                        now,
                        now,
                        data['logo']
                    ))

                tasks = data["tasks"]
                quest_id = cursor.lastrowid
                for task in tasks:
                    cursor.execute(
                        (self._create_quest_task_script),
                        (
                            task['type'],
                            json.dumps(task['extra']),
                            quest_id,
                            now,
                            now
                        ))

                connection.commit()

                return quest_id

    _update_quest_script=f"""
        UPDATE quest
        SET title= %s,description= %s,start_at= %s, end_at= %s,
            reward_type= %s, reward_slots= %s, network= %s, eligibility= %s, status= %s, logo=%s
        WHERE id = %s;
    """
    #add delete or insert task
    _update_quest_task_script = f"""
        UPDATE quest_task
        SET `type` = %s, extra = %s, quest_id = %s, updated_at = %s
        WHERE task_id = %s
    """

    def update_quest(self, id, slug,update_data):
        print(update_data)
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._update_quest_script),
                    (
                        update_data['title'],
                        update_data['description'],
                        update_data['startAt'],
                        update_data['endAt'],
                        update_data['rewardType'],
                        update_data['rewardSlots'],
                        update_data['network'],
                        update_data['eligibility'],
                        update_data['status'],
                        update_data['logo'],
                        id
                    )
                )
                connection.commit()

    _insert_quest_entry_script=f"""
        INSERT INTO user_quest_entry (quest_id,user_id,status,created_at,update_at) VALUES(%s,%s,%s,%s,%s);
    """

    def insert_quest_entry(self, request):
        now=datetime.datetime.now()
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._create_quest_script), (request['quest_id'], request['user_id'], request['status'], now, now))
                connection.commit()
                return cursor.lastrowid

    _update_quest_entry_script=f"""
        UPDATE user_quest_entry
        SET status=%s, updated_at =%s
        WHERE quest_id = %s AND user_id = %s;
    """

    def update_quest_entry(self, request):
        now=datetime.datetime.now()
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._create_quest_script), (request['status'], now, request['quest_id'], request['user_id']))
                connection.commit()
                return cursor.lastrowid


    #change to select where user_id
    _get_quests_by_user_script = f""" 
        SELECT id, title, description, start_at, end_at, reward_type,
            reward_slots, network, eligibility, community_id, status,logo
        FROM quest
        WHERE community_id = %s
    """

    def get_quest_by_user(self,user_id):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._get_quests_by_user_script), (user_id,))
                return cursor.fetchall()

    _get_status_of_quest_id_by_user_script=f"""
        SELECT status FROM user_quest_entry WHERE quest_id = %s and user_id = %s;
    """

    def get_status_of_quest_id_by_user(self,quest_id,user_id):
        with self._init_connection() as connection:
            with self.create_cursor(connection, dictionary=True) as cursor:
                cursor.execute(
                    (self._get_status_of_quest_id_by_user_script), (quest_id,user_id))
                return cursor.fetchone()

