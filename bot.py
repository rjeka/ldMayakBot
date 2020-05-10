import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


# -----------------------------------------Messages handlers------------------------------------------------------
@bot.message_handler(commands=['start'])
def start_message(message):
    name = message.from_user.first_name
    start_keyboard = types.InlineKeyboardMarkup()
    menu_button = types.InlineKeyboardButton(text="Показать все доступные команды", callback_data="/menu")
    start_keyboard.add(menu_button)
    bot.send_message(message.chat.id, config.START_MENU.format(message.from_user.first_name), reply_markup=start_keyboard)


@bot.message_handler(commands=['help', 'menu'])
def help_message(message):
    help_keyboard = types.InlineKeyboardMarkup(row_width=1)

    start_button = types.InlineKeyboardButton(text="/start - показать приветствие", callback_data="/start")
    help_button = types.InlineKeyboardButton(text="/help -  показать список всех команд", callback_data="/menu")
    tsn_button = types.InlineKeyboardButton(text="/tsn - показать информацию о ТСН", callback_data='/tsn')
    government_button = types.InlineKeyboardButton(text="/government - информация о госорганах",
                                                   callback_data="/government")
    bill_button = types.InlineKeyboardButton(text="/bill - квитанция за КУ", callback_data="/bill")

    help_keyboard.add(start_button, help_button, tsn_button, government_button, bill_button)
    bot.send_message(message.chat.id, config.HELP_MENU, reply_markup=help_keyboard)


@bot.message_handler(commands=['tsn'])
def tsn_message(message):
    tsn_keyboard = types.InlineKeyboardMarkup(row_width=1)
    requisites_button = types.InlineKeyboardButton(text="реквизиты ТСН", callback_data="/requisites")
    contacts_button = types.InlineKeyboardButton(text="полезные телефоны", callback_data="/contacts")
    menu_button = types.InlineKeyboardButton(text="в/еытернуться в главное меню", callback_data="/menu")
    tsn_keyboard.add(requisites_button, contacts_button, menu_button)
    bot.send_message(message.chat.id, "Выберите раздел\n", reply_markup=tsn_keyboard)


@bot.message_handler(commands=['requisites'])
def tsn_requisites_message(message):
    tsn_keyboard = types.InlineKeyboardMarkup(row_width=1)
    tsn_button = types.InlineKeyboardButton(text="Вернуться в меню ТСН", callback_data="/tsn")
    menu_button = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="/menu")
    tsn_keyboard.add(tsn_button, menu_button)
    bot.send_message(message.chat.id, config.TSN_REQUISITES, reply_markup=tsn_keyboard)



@bot.message_handler(commands=['contacts'])
def tsn_contacts_message(message):
    tsn_keyboard = types.InlineKeyboardMarkup(row_width=1)
    tsn_button = types.InlineKeyboardButton(text="Вернуться в меню ТСН", callback_data="/tsn")
    menu_button = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="/menu")
    tsn_keyboard.add(tsn_button, menu_button)
    bot.send_message(message.chat.id, config.TSN_CONTACTS, reply_markup=tsn_keyboard)


@bot.message_handler(commands=['bill'])
def bill_message(message):
    bot.send_message(message.chat.id, 'К сожалению в данный момент раздел в разработке')


@bot.message_handler(content_types=["text"])
def default_text(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Может быть поискать на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)


# -----------------------------------------------Keyboard handlers----------------------------------
# main menu keyboard handler
@bot.callback_query_handler(func=lambda call: call.data in ["/start", "/menu", "/tsn", "/bill"])
def callback_main_command(call):
    if call.data == "/start":
        start_message(call.message)
    elif call.data == "/menu":
        help_message(call.message)
    elif call.data == "/tsn":
        tsn_message(call.message)
    elif call.data == "/bill":
        bill_message(call.message)


# tsn keyboard handler
@bot.callback_query_handler(func=lambda call: call.data in ["/requisites", "/contacts"])
def callback_tsn_command(call):
    if call.data == "/requisites":
        tsn_requisites_message(call.message)
    elif call.data == "/contacts":
        tsn_contacts_message(call.message)


if __name__ == '__main__':
    bot.infinity_polling()
