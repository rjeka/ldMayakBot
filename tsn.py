import os
import telebot
from telebot import types
import keyboards

import menu
import security


bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])


def tsn(message):
    tsn_keyboard = types.InlineKeyboardMarkup(row_width=1)
    userinfo_button = types.InlineKeyboardButton(text="Ваши данные в ТСН", callback_data="/userinfo")
    requisites_button = types.InlineKeyboardButton(text="реквизиты ТСН", callback_data="/requisites")
    contacts_button = types.InlineKeyboardButton(text="полезные телефоны", callback_data="/contacts")
    street_button = types.InlineKeyboardButton(text="список улиц", callback_data="/street")
    tsn_keyboard.add(userinfo_button, requisites_button, contacts_button, street_button)
    keyboards.main_menu_key(tsn_keyboard)
    bot.send_message(message.chat.id, "Выберите раздел\n", reply_markup=tsn_keyboard)


def tsn_userinfo(message, user_info):
    if security.check_user_id(user_info):
        message_menu = menu.get_user_info("SELECT * from users;")
        tsn_keyboard = types.InlineKeyboardMarkup(row_width=1)
        tsn_button = types.InlineKeyboardButton(text="Вернуться в меню ТСН", callback_data="/tsn")
        tsn_keyboard.add(tsn_button)
        keyboards.main_menu_key(tsn_keyboard)
        bot.send_message(message.chat.id, message_menu + str(user_info), reply_markup=tsn_keyboard)
    else:
        message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'tsn_access_deny'")
        tsn_keyboard = types.InlineKeyboardMarkup(row_width=1)
        get_id_button = types.InlineKeyboardButton(text="Получить Telegram ID", callback_data="/getid")
        tsn_keyboard.add(get_id_button)
        keyboards.main_menu_key(tsn_keyboard)
        bot.send_message(message.chat.id, message_menu, reply_markup=tsn_keyboard)