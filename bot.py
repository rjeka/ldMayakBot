import os
import telebot
from telebot import types

import menu
import keyboards



bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])


# -----------------------------------------Main menu messages handlers------------------------------
@bot.message_handler(commands=['start'])
def start_message(message):
    message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'start'") \
        .format(message.from_user.first_name)
    start_keyboard = types.InlineKeyboardMarkup(row_width=1)
    guest_button = types.InlineKeyboardButton(text="Получить код для гостевого проезда" , callback_data="/guest")
    tsn_button = types.InlineKeyboardButton(text="Получить информацию о ТСН", callback_data="/tsn")
    id_button = types.InlineKeyboardButton(text="Узнать свой Telegram ID", callback_data="/id")
    start_keyboard.add(guest_button, tsn_button, id_button)
    bot.send_message(message.chat.id, message_menu, reply_markup=start_keyboard)

# help menu
@bot.message_handler(commands=['help', 'menu'])
def help_message(message):
    message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'help'")
    help_keyboard = types.InlineKeyboardMarkup(row_width=1)
    start_button = types.InlineKeyboardButton(text="/start - показать приветствие", callback_data="/start")
    help_button = types.InlineKeyboardButton(text="/help -  показать список всех команд", callback_data="/menu")
    tsn_button = types.InlineKeyboardButton(text="/tsn - показать информацию о ТСН", callback_data='/tsn')

    help_keyboard.add(start_button, help_button, tsn_button)
    bot.send_message(message.chat.id, message_menu, reply_markup=help_keyboard)


@bot.message_handler(commands=['tsn'])
def tsn_message(message):
    message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'tsn'")
    bot.send_message(message.chat.id, message_menu)


@bot.message_handler(commands=['id'])
def id_message(message):
    bot.send_message(message.chat.id, "Ваш Telegram ID: {}".format(message.from_user.id))

# -----------------------------------------------Keyboard handlers----------------------------------

# main menu keyboard handler
@bot.callback_query_handler(
    func=lambda call: call.data in ["/start", "/menu", "/tsn", "/id"])
def callback_main_command(call):
    if call.data == "/start":
        start_message(call.message)
    elif call.data == "/menu":
        help_message(call.message)
    elif call.data == "/tsn":
        tsn_message(call.message)
    elif call.data == "/id":
        id_message(call.message)


# --------------------------------------main___________________________________
if __name__ == '__main__':
    bot.infinity_polling()
