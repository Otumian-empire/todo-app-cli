from db import DB


class Todo:

    def __init__(self):
        db = DB()
        self.db_conn = db.get_db_conn()
        self.cur = db.get_cursor(self.db_conn)

    def create_activity(self, task):

        try:
            if not task:
                return False

            task = str(task).lower()

            sql_query = "INSERT INTO `todos`(`task`) VALUES (%s);"
            values = (task,)

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

        try:
            sql_query = "SELECT `id`, `task`, `created_at`, `update_at` FROM `todos`;"
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

        try:
            if not id:
                return []

            id = int(id)

            sql_query = f"SELECT `id`, `task`, `created_at`, `update_at` FROM `todos` WHERE `id`=%s;"
            values = (id, )

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

        try:
            if not id or not new_task:
                return False

            id = int(id)
            new_task = str(new_task).lower()

            sql_query = f"UPDATE `todos` SET `task`=%s, `update_at`=CURRENT_TIMESTAMP WHERE `id`=%s;"
            values = (new_task, id)

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

        try:
            if not id:
                return False

            id = int(id)

            sql_query = f"DELETE FROM `todos` WHERE `id`=%s;"
            values = (id, )

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

        try:
            sql_query = f"DELETE FROM `todos`;"
            self.cur.execute(sql_query)

        except (Exception, mysql.connector.Error) as e:
            print(str(e))
            return False

        if not self.cur:
            return False

        self.db_conn.commit()
        self.db_conn.close()

        return True
