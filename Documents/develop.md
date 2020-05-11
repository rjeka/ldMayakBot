## документация для разработчиков ldMayakBot
### Техническое описание
Язык разработки  python3, основная библиотека [telebot](https://github.com/eternnoir/pyTelegramBotAPI)

###База данных
Основная база данных: postgres12
Параметры в базу передаются через env
DB_NAME = ldmayakbot
DB_USER = ldmayak
DB_PASS = bb7d5369b5de (для dev)
DB_HOST = 127.0.0.1
DB_PORT = 15432

###Таблицы

| name          | description             |
| ------------- |:------------------------|
| menu_text     | тексты основных меню    |
| tsn_info      | инфо для меню tsn       |