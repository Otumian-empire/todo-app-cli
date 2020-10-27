import os

from db import DB


def clear_screen():
    _ = os.system('cls' if os.name == 'nt' else 'clear')


def print_activity(activity):
    id, task, created_at, updated_at = activity

    row = f"{id} - {task} - ({created_at} - {updated_at if updated_at else 'not updated'})"
    print(row)


def do_check_table(sql_query, error_message="error", success_message="success"):
    try:
        db = DB()

        conn = db.get_db_conn()
        cur = db.get_cursor(conn)

        cur.execute(sql_query)

        if not cur:
            raise Exception(error_message)
        else:
            print(success_message)

    except Exception as e:
        print(str(e))
