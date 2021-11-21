import psycopg2
import os

def get_job_status(table, user_id):
    con: None = psycopg2.connect(
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )

    with con:
        with con.cursor() as cur:
            cur.execute("SELECT status FROM add_condition WHERE user_id LIKE '270933806'")
            rows = cur.fetchall()
            response: str = ';'.join(map(','.join, rows))
            con.commit()
            cur.close()
    print(response)
    return response


def set_job_status(table, user_id, status):
    con: None = psycopg2.connect(
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )

    with con:
        with con.cursor() as cur:
            response = cur.execute("UPDATE {} SET user_id = '{}', status  = '{}'".format(table, user_id, status))
            con.commit()
            cur.close()
    return response


# this function return text for menus
def data_base_update(update):
    con: None = psycopg2.connect(
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )

    with con:
        with con.cursor() as cur:
            cur.execute(update)
            con.commit()
            cur.close()
    return True
