import os
import telebot
from telebot import types
import psycopg2
import time

import keyboards
import security
import menu

bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])

# main services menu
def services(message):
    services_keyboard = types.InlineKeyboardMarkup(row_width=2)
    bulk_button = types.InlineKeyboardButton(text="Сыпучие материалы", callback_data="bulk")
    well_button = types.InlineKeyboardButton(text="Колодцы, скважины", callback_data="well")
    electric_button = types.InlineKeyboardButton(text="Электрика", callback_data="electric")
    windows_button = types.InlineKeyboardButton(text="Окна, остекление", callback_data="windows")
    tractor_button = types.InlineKeyboardButton(text="Трактор, экскаватор", callback_data="tractor")
    plumbing_button =  types.InlineKeyboardButton(text="Сантехника", callback_data="plumbing")
    sewerage_button = types.InlineKeyboardButton(text="Канализация", callback_data="sewerage")
    clean_watter_button = types.InlineKeyboardButton(text="Очистка воды", callback_data="clean_water")
    air_button =  types.InlineKeyboardButton(text="Конционеры, вентиляция", callback_data="air")
    auto_button = types.InlineKeyboardButton(text="Автосервисы", callback_data="auto")
    services_keyboard.add(bulk_button, tractor_button, well_button, electric_button, plumbing_button, clean_watter_button,
                          sewerage_button, windows_button, air_button, auto_button)
    keyboards.main_menu_key(services_keyboard)
    bot.send_message(message.chat.id, "Выберите раздел с услугой:\n", reply_markup=services_keyboard)


# get services from Postgres if telegrams id in the white list and if all utility bill is payed
def get_servises(message, user_info, service_group):
    if security.check_user_id(user_info):
        con = psycopg2.connect(
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASS'],
            host=os.environ['DB_HOST'],
            port=os.environ['DB_PORT']
        )
        services_keyboard = types.InlineKeyboardMarkup(row_width=1)

        with con.cursor() as cur:
            cur.execute(
                " SELECT description, contact, first_tel, second_tel, email, url, vk, instagram, other_contact"
                " FROM services WHERE service_group='{}';".format(service_group))
            rows = cur.fetchall()
            print(len(rows))
            if len(rows) == 0:
                service_button = types.InlineKeyboardButton(text="Вернуться в меню услуг", callback_data="/services")
                services_keyboard.add(service_button)
                keyboards.main_menu_key(services_keyboard)
                bot.send_message(message.chat.id, "К сожалению в данном разделе пока нет записей",
                                 reply_markup=services_keyboard)
            else:
                for row in rows:
                    bot_message = ""
                    if row[0]:
                        bot_message = bot_message + row[0] + "\n\n"
                    if row[1]:
                        bot_message = bot_message + "Контактное лицо: " + row[1] + "\n\n"
                    if row[2]:
                        bot_message = bot_message + "Тел: " + row[2] + "\n\n"
                    if row[3]:
                        bot_message = bot_message + "Тел: " + row[3] + "\n\n"
                    if row[4]:
                        bot_message = bot_message + "email: " + row[4] + "\n\n"
                    if row[5]:
                        bot_message = bot_message + "сайт: " + row[5] + "\n\n"
                    if row[6]:
                        bot_message = bot_message + "VK:\n" + row[6] + "\n\n"
                    if row[7]:
                        bot_message = bot_message + "Instagram:\n" + row[7] + "\n\n"
                    if row[8]:
                        bot_message = bot_message + "Дополнительная информация:\n" + row[8] + "\n\n"

                    bot.send_message(message.chat.id, bot_message)
                    time.sleep(1)

                service_button = types.InlineKeyboardButton(text="Вернуться в меню услуг", callback_data="/services")
                services_keyboard.add(service_button)
                keyboards.main_menu_key(services_keyboard)
                bot.send_message(message.chat.id, "Запрос выполнен успешно найдено {} записи(ей)".
                                 format(len(rows)), reply_markup=services_keyboard)
    else:
        message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'tsn_access_deny'")
        services_keyboard = types.InlineKeyboardMarkup(row_width=1)
        get_id_button = types.InlineKeyboardButton(text="Получить Telegram ID", callback_data="/getid")
        services_keyboard.add(get_id_button)
        keyboards.main_menu_key(services_keyboard)
        bot.send_message(message.chat.id, message_menu, reply_markup=services_keyboard)
