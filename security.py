import psycopg2
import os


def check_user_id(user_id):

    con: None = psycopg2.connect(
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )
    if user_id:
        with con:
            with con.cursor() as cur:
                cur.execute("SELECT telegram_id FROM users WHERE telegram_id={}".format(user_id))
                rows = cur.fetchall()

        if rows:
            return True
        else:
            return False
    else:
        return False