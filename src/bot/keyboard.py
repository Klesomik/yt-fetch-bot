from telebot import types

def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    btn_subscribe = types.KeyboardButton(text='subscribe', callback_data='subscribe')
    btn_unsubscribe = types.KeyboardButton(text='unsubscribe', callback_data='unsubscribe')
    btn_import = types.KeyboardButton(text='import', callback_data='import')
    btn_export = types.KeyboardButton(text='export', callback_data='export')

    keyboard.add(btn_subscribe, btn_unsubscribe, btn_subscribe, btn_unsubscribe)

    return keyboard