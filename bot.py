import os

import telebot
from telebot import types

import keyboards
import menu
import utilities
import news
import services

import tsn

bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])


# -----------------------------------------Main menu messages handlers------------------------------
@bot.message_handler(commands=['start'])
def start_message(message):
    message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'start'") \
        .format(message.from_user.first_name)
    start_keyboard = types.InlineKeyboardMarkup(row_width=1)
    menu_button = types.InlineKeyboardButton(text="Начать работу", callback_data="/menu")
    url_button = types.InlineKeyboardButton(text="Документация проекта", url="https://github.com/rjeka/ldMayakBot")
    start_keyboard.add(menu_button, url_button)
    bot.send_message(message.chat.id, message_menu, reply_markup=start_keyboard)


# help menu
@bot.message_handler(commands=['help', 'menu'])
def help_message(message):
    message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'help'")
    help_keyboard = types.InlineKeyboardMarkup(row_width=1)
    start_button = types.InlineKeyboardButton(text="/start - показать приветствие", callback_data="/start")
    help_button = types.InlineKeyboardButton(text="/help -  показать список всех команд", callback_data="/menu")
    tsn_button = types.InlineKeyboardButton(text="/tsn - показать информацию о ТСН", callback_data='/tsn')
    government_button = types.InlineKeyboardButton(text="/government - информация о госорганах",
                                                   callback_data="/government")
    services_button = types.InlineKeyboardButton(text="/services - список услуг", callback_data='/services')
    bill_button = types.InlineKeyboardButton(text="/bill - квитанция за КУ", callback_data="/bill")
    check_button = types.InlineKeyboardButton(text="/check - проверка платежей и наличия задолженности",
                                              callback_data="/check")
    news_button = types.InlineKeyboardButton(text="/news - показать новости", callback_data="/news")

    help_keyboard.add(start_button, help_button, tsn_button, services_button, government_button, bill_button,
                      check_button, news_button)
    bot.send_message(message.chat.id, message_menu, reply_markup=help_keyboard)


@bot.message_handler(commands=['tsn'])
def tsn_message(message):
    tsn.tsn(message)


@bot.message_handler(commands=['services'])
def services_message(message):
    services.services(message)


@bot.message_handler(commands=['contacts'])
def tsn_contacts_message(message):
    message_menu = menu.get_menu("SELECT text FROM tsn_info WHERE name LIKE 'contacts'")
    tsn_keyboard = types.InlineKeyboardMarkup(row_width=1)
    tsn_button = types.InlineKeyboardButton(text="Вернуться в меню ТСН", callback_data="/tsn")
    tsn_keyboard.add(tsn_button)
    keyboards.main_menu_key(tsn_keyboard)
    bot.send_message(message.chat.id, message_menu, reply_markup=tsn_keyboard)


@bot.message_handler(commands=['government'])
def government_message(message):
    government_keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboards.main_menu_key(government_keyboard)
    bot.send_message(message.chat.id, 'К сожалению в данный момент раздел в разработке',
                     reply_markup=government_keyboard)


@bot.message_handler(commands=['bill'])
def bill_message(message):
    bot.send_message(message.chat.id, 'К сожалению в данный момент раздел в разработке')


@bot.message_handler(commands=['check'])
def check_message(message):
    check_keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboards.main_menu_key(check_keyboard)
    bot.send_message(message.chat.id, 'К сожалению в данный момент раздел в разработке', reply_markup=check_keyboard)


@bot.message_handler(commands=['news'])
def news_message(message):
    news.news(message)


@bot.message_handler(content_types=["text"])
def default_text(message):
    default_keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboards.main_menu_key(default_keyboard)
    bot.send_message(message.chat.id, 'К сожалению я не знаю такой команды', reply_markup=default_keyboard)


# -----------------------------------------------Keyboard handlers----------------------------------

# main menu keyboard handler
@bot.callback_query_handler(
    func=lambda call: call.data in ["/start", "/menu", "/tsn", "/services", "/government", "/bill",
                                    "/check", "/news"])
def callback_main_command(call):
    if call.data == "/start":
        start_message(call.message)
    elif call.data == "/menu":
        help_message(call.message)
    elif call.data == "/tsn":
        tsn_message(call.message)
    elif call.data == "/services":
        services_message(call.message)
    elif call.data == "/government":
        government_message(call.message)
    elif call.data == "/bill":
        bill_message(call.message)
    elif call.data == "/check":
        check_message(call.message)
    elif call.data == "/news":
        news_message(call.message)


# tsn keyboard handler
@bot.callback_query_handler(
    func=lambda call: call.data in ["/userinfo", "/requisites", "/contacts", "/street", "/getid"])
def callback_tsn_command(call):
    if call.data == "/userinfo":
        tsn.tsn_userinfo(call.message, call.from_user.id)
    elif call.data == "/requisites":
        tsn.tsn_requisites(call.message)
    elif call.data == "/contacts":
        tsn_contacts_message(call.message)
    elif call.data == "/street":
        tsn.tsn_streets(call.message)
    elif call.data == "/getid":
        utilities.get_id(call.message, call.from_user.id)


# services keyboard handler
@bot.callback_query_handler(
    func=lambda call: call.data in ["bulk", "tractor", "well", "water", "warm", "land", "electric",
                                    "plumbing", "windows", "clean_water", "sewerage", "auto", "inside_build"])
def callback_tsn_command(call):
    if call.data == "bulk":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "tractor":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "well":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "water":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "warm":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "land":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "electric":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "plumbing":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "clean_water":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "sewerage":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "windows":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "auto":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "inside_build":
        services.get_servises(call.message, call.from_user.id, call.data)


# service -> build keyboard handler
@bot.callback_query_handler(
    func=lambda call: call.data in ["build", "build_house", "build_roof", "build_facade",
                                    "build_other"])
def callback_tsn_command(call):
    if call.data == "build":
        services.services_build(call.message, call.from_user.id)
    if call.data == "build_house":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "build_roof":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "build_facade":
        services.get_servises(call.message, call.from_user.id, call.data)
    if call.data == "build_other":
        services.get_servises(call.message, call.from_user.id, call.data)


# --------------------------------------main___________________________________
if __name__ == '__main__':
    bot.infinity_polling()
