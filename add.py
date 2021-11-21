import psycopg2
import os


def set_job_status(table, status):
    con: None = psycopg2.connect(
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )


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
    return 0
