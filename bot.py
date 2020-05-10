import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Показать все команды", callback_data="help")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, config.START_MENU, reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, config.HELP_MENU)


@bot.message_handler(commands=['bill'])
def help_message(message):
    bot.send_message(message.chat.id, 'В данный момент раздел в разработке')


@bot.message_handler(content_types=["text"])
def default_text(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Может быть поискать на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "К сожалению я не знаю такой команды.", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "help":
        bot.send_message(chat_id=call.message.chat.id, text=config.HELP_MENU)


if __name__ == '__main__':
    bot.infinity_polling()
