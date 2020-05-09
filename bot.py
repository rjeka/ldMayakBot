import config
import telebot
from telebot import types



bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, config.START_MENU)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, config.HELP_MENU )


@bot.message_handler(content_types=["text"])
def default_text(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Может быть поискать на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "К сожалению я не знаю такой команды.", reply_markup=keyboard)



if __name__ == '__main__':
    bot.infinity_polling()