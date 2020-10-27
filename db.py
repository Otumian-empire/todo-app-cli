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