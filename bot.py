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
    bot.send_message(message.chat.id, "Ваш Telegram ID:")
    bot.send_message(message.chat.id, message.from_user.id)

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


# -----------------------------------------add tg id handlers------------------------------
@bot.message_handler(commands=['add'])
def add_message(message):
    if security.check_user_id(message.from_user.id):
        if security.check_admin_id(message.from_user.id):
            bot.send_message(message.chat.id, "Введите Telegram ID")
            db.data_base_update("INSERT INTO add_condition (user_id) VALUES('{}') ON CONFLICT (user_id) DO NOTHING".format(message.from_user.id))
            db.set_job_status("add_condition", message.chat.id, "tg_id")
        else:
            message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'admin_access_denied'")
            bot.send_message(message.chat.id, message_menu.format(message.from_user.first_name, message.from_user.id))
    else:
        message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'access_denied'")
        bot.send_message(message.chat.id, message_menu.format(message.from_user.first_name, message.from_user.id))


@bot.message_handler(func=lambda message: db.get_job_status(message.chat.id, 'add_condition') == 'tg_id')
def telegram_id_message(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Вы ввели не правильный Telegram ID")
    else:
        bot.send_message(message.chat.id, "Введите номер л\с")
        db.set_job_status("add_condition", message.chat.id, "add_personal_account")
        db.data_base_update("INSERT INTO users (telegram_id) VALUES('{}') ON CONFLICT (telegram_id) DO NOTHING".format(message.text))


@bot.message_handler(func=lambda message: db.get_job_status(message.chat.id, 'add_condition') == 'add_personal_account')
def personal_account_message(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Вы ввели не правильный Telegram ID")
    else:
        db.data_base_update("UPDATE users SET personal_account = '{}' WHERE \"personal_account\" IS NULL".format(message.text))
        bot.send_message(message.chat.id, "Пользователь добавлен в базу данных\n")
        db.set_job_status("add_condition", message.chat.id, "start")
        message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'admin'")
        bot.send_message(message.chat.id, message_menu.format(message.from_user.first_name, message.from_user.id))


# --------------------------------------main___________________________________
if __name__ == '__main__':
    bot.infinity_polling()
