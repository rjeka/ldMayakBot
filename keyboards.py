from telebot import types


# back to main menu
def main_menu_key(keyboard_name):
    menu_button = types.InlineKeyboardButton(text="Вернуться в главное меню", callback_data="/menu")
    keyboard_name.add(menu_button)
