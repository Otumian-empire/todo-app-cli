from os import environ

import mysql.connector
from dotenv import load_dotenv

load_dotenv('./.env.local')

USERNAME = environ.get('DB_USER')
PASSWORD = environ.get('DB_PASSWORD')
HOST = environ.get('DB_HOST')
DATABASE_NAME = environ.get('DB_NAME')


class DB:

    def get_db_conn(self):
        try:
            return mysql.connector.connect(
                host=HOST, user=USERNAME, password=PASSWORD,
                database=DATABASE_NAME, buffered=True)

        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return False

    def get_cursor(self, db_conn):
        try:
            return db_conn.cursor()
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return False


class Todo:

    def __init__(self):
        db = DB()
        self.db_conn = db.get_db_conn()
        self.cur = db.get_cursor(self.db_conn)

    def create_activity(self, task):
        if not task:
            return False

        sql_query = "INSERT INTO `todos`(`task`) VALUES (%s);"
        values = (task.lower(),)

        try:
            self.cur.execute(sql_query, values)
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return False

        if not self.cur:
            return False

        self.db_conn.commit()
        self.db_conn.close()

        return True

    def read_all_activities(self):
        sql_query = "SELECT `id`, `task`, `created_at` FROM `todos`;"

        try:
            self.cur.execute(sql_query)
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return []

        if not self.cur:
            return []

        items = self.cur.fetchall()

        self.db_conn.close()

        return items

    def read_an_activity(self, id):
        if not id:
            return False

        sql_query = f"SELECT `id`, `task`, `created_at` FROM `todos` WHERE `id`=%s;"
        values = (str(id).lower(), )

        try:
            self.cur.execute(sql_query, values)
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return []

        if not self.cur:
            return []

        item = self.cur.fetchone()

        self.db_conn.close()

        return item

    def update_an_activity(self, id, new_task):
        if not id or not new_task:
            return False

        sql_query = f"UPDATE `todos` SET `task`=%s `update_at`=CURRENT_TIMESTAMP WHERE `id`=%s;"
        values = (new_task.lower(), str(id))

        try:
            self.cur.execute(sql_query, values)
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return False

        if not self.cur:
            return False

        self.db_conn.commit()
        self.db_conn.close()

        return True

    def delete_an_activity(self, id):
        if not id:
            return False

        sql_query = f"DELETE FROM `todos` WHERE `id`=%s;"
        values = (str(item_value).lower(), )

        try:
            self.cur.execute(sql_query, values)
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return False

        if not self.cur:
            return False

        self.db_conn.commit()
        self.db_conn.close()

        return True

    def delete_all_activities(self):
        sql_query = f"DELETE FROM `todos`;"

        try:
            self.cur.execute(sql_query)
        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return False

        if not self.cur:
            return False

        self.db_conn.commit()
        self.db_conn.close()

        return True


