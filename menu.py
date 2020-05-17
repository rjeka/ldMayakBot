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

# all street string from table street
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

def get_user_info(select):
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
            menu = 'Данная информация доступна только Вам:\n' \
                   'Другие пользователи не могут получить доступ к Вашим данным\n\n'

            for row in rows:
                menu = f"{menu}Ваше имя: {row[5]}\nВаш адрес: {row[1]} {row[2]}\n" \
                       f"Ваш номер лицевого счета: {row[0]}\nВаш email: {row[6]}\nВаш telegram_id: "

    return menu
