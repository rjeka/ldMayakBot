import os
import telebot
from telebot import types
import keyboards

bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])


def get_id(message, user_info):
    get_id_keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboards.main_menu_key(get_id_keyboard)
    bot.send_message(message.chat.id, "Ваш telegram ID: " + str(user_info), reply_markup=get_id_keyboard)
