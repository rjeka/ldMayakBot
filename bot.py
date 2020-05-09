import config
import telebot
from telebot import types



bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот ТСН "Ладожский маяк"\n'
                                      '1. Я могу помочь узнать наличие и сумму задолженности по комунальным услугам\n'
                                      '2  Отправлю квитанцию и QR код для оплаты коммунальных услуг\n'
                                      '3. Покажу полезные телефоны служб поселка\n'
                                      '4. Подскажу контакты проверенных фирм и услуг в нашем Коттеджном поселке\n\n'
                                      'Для обзора всех возможностей введите /help')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот ТСН "Ладожский маяк"\n\n'
                                      'Введите в окно диалога или нажмите на одну из команд'
                                      '/start - показать приветствие\n'
                                      '/help -  показать список полезных команд\n'
                                      '/contact - показать телефоны правления ТСН, Охраны\n'
                                      '/bill - получить квитанцию для оплаты коммунальных услуг')


@bot.message_handler(content_types=["text"])
def default_text(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)



if __name__ == '__main__':
    bot.infinity_polling()