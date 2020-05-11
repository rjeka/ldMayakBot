import os

import telebot
from telebot import types

import keyboards
import menu

bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])


# -----------------------------------------Messages handlers------------------------------------------------------
@bot.message_handler(commands=['start'])
def start_message(message):
    message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'start'")\
        .format(message.from_user.first_name)
    start_keyboard = types.InlineKeyboardMarkup(row_width=1)
    menu_button = types.InlineKeyboardButton(text="Показать все доступные команды", callback_data="/menu")
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
    bill_button = types.InlineKeyboardButton(text="/bill - квитанция за КУ", callback_data="/bill")
    check_button = types.InlineKeyboardButton(text="/check - проверка платежей и наличия задолженности",
                                              callback_data="/check")
    news_button = types.InlineKeyboardButton(text="/news - показать новости", callback_data="/news")

    help_keyboard.add(start_button, help_button, tsn_button, government_button, bill_button, check_button, news_button)
    bot.send_message(message.chat.id, message_menu, reply_markup=help_keyboard)

# tsn menu
@bot.message_handler(commands=['tsn'])
def tsn_message(message):
    tsn_keyboard = types.InlineKeyboardMarkup(row_width=1)
    requisites_button = types.InlineKeyboardButton(text="реквизиты ТСН", callback_data="/requisites")
    contacts_button = types.InlineKeyboardButton(text="полезные телефоны", callback_data="/contacts")
    street_button = types.InlineKeyboardButton(text="список улиц", callback_data="/street")
    tsn_keyboard.add(requisites_button, contacts_button, street_button)
    keyboards.main_menu_key(tsn_keyboard)
    bot.send_message(message.chat.id, "Выберите раздел\n", reply_markup=tsn_keyboard)


@bot.message_handler(commands=['requisites'])
def tsn_requisites_message(message):
    message_menu = menu.get_menu("SELECT text FROM tsn_info WHERE name LIKE 'requisites'")
    tsn_keyboard = types.InlineKeyboardMarkup(row_width=1)
    tsn_button = types.InlineKeyboardButton(text="Вернуться в меню ТСН", callback_data="/tsn")
    tsn_keyboard.add(tsn_button)
    keyboards.main_menu_key(tsn_keyboard)
    bot.send_message(message.chat.id, message_menu, reply_markup=tsn_keyboard)


@bot.message_handler(commands=['contacts'])
def tsn_contacts_message(message):
    message_menu = menu.get_menu("SELECT text FROM tsn_info WHERE name LIKE 'contacts'")
    tsn_keyboard = types.InlineKeyboardMarkup(row_width=1)
    tsn_button = types.InlineKeyboardButton(text="Вернуться в меню ТСН", callback_data="/tsn")
    tsn_keyboard.add(tsn_button)
    keyboards.main_menu_key(tsn_keyboard)
    bot.send_message(message.chat.id, message_menu, reply_markup=tsn_keyboard)

@bot.message_handler(commands=['street'])
def tsn_streets_message(message):
    message_menu = menu.all_street("SELECT name FROM street")
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
    news_keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboards.main_menu_key(news_keyboard)
    bot.send_message(message.chat.id, 'К сожалению в данный момент раздел в разработке', reply_markup=news_keyboard)


@bot.message_handler(content_types=["text"])
def default_text(message):
    default_keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboards.main_menu_key(default_keyboard)
    bot.send_message(message.chat.id, 'К сожалению я не знаю такой команды', reply_markup=default_keyboard)


# -----------------------------------------------Keyboard handlers----------------------------------
# main menu keyboard handler
@bot.callback_query_handler(func=lambda call: call.data in ["/start", "/menu", "/tsn", "/government", "/bill",
                                                            "/check", "/news"])
def callback_main_command(call):
    if call.data == "/start":
        start_message(call.message)
    elif call.data == "/menu":
        help_message(call.message)
    elif call.data == "/tsn":
        tsn_message(call.message)
    elif call.data == "/government":
        government_message(call.message)
    elif call.data == "/bill":
        bill_message(call.message)
    elif call.data == "/check":
        check_message(call.message)
    elif call.data == "/news":
        news_message(call.message)


# tsn keyboard handler
@bot.callback_query_handler(func=lambda call: call.data in ["/requisites", "/contacts", "/street"])
def callback_tsn_command(call):
    if call.data == "/requisites":
        tsn_requisites_message(call.message)
    elif call.data == "/contacts":
        tsn_contacts_message(call.message)
    elif call.data == "/street":
        tsn_streets_message(call.message)


if __name__ == '__main__':
    bot.infinity_polling()
