import os
import telebot
from telebot import types
import keyboards


bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])

def news(message):
    news_keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboards.main_menu_key(news_keyboard)
    bot.send_message(message.chat.id, 'К сожалению в данный момент раздел в разработке', reply_markup=news_keyboard)
