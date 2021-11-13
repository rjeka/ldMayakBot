import os
import telebot

import menu

message_menu = menu.get_menu("SELECT text FROM menu_text WHERE name LIKE 'start'")
print(message_menu)