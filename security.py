import os
import telebot
from telebot import types
import psycopg2


import keyboards
import menu

bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])


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


def access_deny(message):
    message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'tsn_access_deny'")
    access_keyboard = types.InlineKeyboardMarkup(row_width=1)
    get_id_button = types.InlineKeyboardButton(text="Получить Telegram ID", callback_data="/getid")
    access_keyboard.add(get_id_button)
    keyboards.main_menu_key(access_keyboard)
    bot.send_message(message.chat.id, message_menu, reply_markup=access_keyboard)
