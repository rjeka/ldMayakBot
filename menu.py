import psycopg2
import os


# this function return text for menus
def get_menu(select):
    con: None = psycopg2.connect(
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )

    with con:
        with con.cursor() as cur:
            cur.execute(select)
            rows = cur.fetchall()
            menu: str = ';'.join(map(','.join, rows))

    return menu


def all_street(select):
    con = psycopg2.connect(
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT']
    )

    with con:
        with con.cursor() as cur:
            cur.execute(select)
            rows = cur.fetchall()
            menu = '\n'.join(map(','.join, rows))

    return menu
