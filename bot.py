import os
import telebot
import menu
import security
import db

bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])


# -----------------------------------------Main menu messages handlers------------------------------
@bot.message_handler(commands=['start'])
def start_message(message):
    message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'start'")
    bot.send_message(message.chat.id, message_menu)


@bot.message_handler(commands=['tsn'])
def tsn_message(message):
    if security.check_user_id(message.from_user.id):
        message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'tsn'")
    else:
        message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'access_denied'")
    bot.send_message(message.chat.id, message_menu)


@bot.message_handler(commands=['id'])
def id_message(message):
    bot.send_message(message.chat.id, "Ваш Telegram ID: {}".format(message.from_user.id))


@bot.message_handler(commands=['admin'])
def admin_message(message):
    if security.check_user_id(message.from_user.id):
        if security.check_admin_id(message.from_user.id):
            message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'admin'")
        else:
            message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'admin_access_denied'")
    else:
        message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'access_denied'")
    bot.send_message(message.chat.id, message_menu.format(message.from_user.first_name, message.from_user.id))


@bot.message_handler(commands=['add'])
def add_message(message):
    bot.send_message(message.chat.id, "Введите Telegram ID")
    db.set_job_status("add_condition", message.chat.id, "tg_id")


@bot.message_handler(func=lambda message: db.get_job_status(message.chat.id, 'add_condition') == 'tg_id')
def telegram_id_message(message):
    bot.send_message(message.chat.id, "Введите номер л\с")
    db.set_job_status("add_condition", message.chat.id, "finish")
    db.data_base_update("UPDATE add_tmp SET telegram_id = '{}'".format(message.text))


# --------------------------------------main___________________________________
if __name__ == '__main__':
    bot.infinity_polling()
