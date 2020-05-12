import psycopg2
import os


def check_user_id():

    con: None = psycopg2.connect(
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )

    with con:
        with con.cursor() as cur:
            cur.execute("SELECT second_auto_number FROM users WHERE telegram_id=1270933806")
            rows = cur.fetchall()

    if rows:
        return True
        print("true")
    else:
        print("false")
        return False
