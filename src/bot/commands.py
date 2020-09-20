import io
from . import bot
#from .keyboard import get_keyboard

from database import (
    Channel,
    subscribe,
    unsubscribe,
    export,
    import_,
)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'subscribe':
        cmd_subscribe(call)
    elif call.data == 'unsubscribe':
        cmd_unsubscribe(call)
    elif call.data == 'import':
        cmd_import(call)
    elif call.data == 'export':
        cmd_export(call)

@bot.message_handler(commands=['start'])
def cmd_start(msg):
    bot.send_message(msg.chat.id, 'Hello! I will help you to get rid of youtube account')

@bot.message_handler(commands=['help'])
def cmd_help(msg):
    pass

def get_subscribe(msg):
    subscribe(Channel(msg.chat.id, msg.text))
    bot.send_message(msg.chat.id, 'Channel was successfully added!')

@bot.message_handler(commands=['subscribe'])
def cmd_subscribe(msg):
    link_msg = bot.send_message(msg.chat.id, 'Send me a link to channel')
    bot.register_next_step_handler(link_msg, get_subscribe)

def get_unsubscribe(msg):
    unsubscribe(Channel(msg.chat.id, msg.text))
    bot.send_message(msg.chat.id, 'Channel was successfully deleted!')

@bot.message_handler(commands=['unsubscribe'])
def cmd_unsubscribe(msg):
    link_msg = bot.send_message(msg.chat.id, 'Send me a link to channel')
    bot.register_next_step_handler(link_msg, get_unsubscribe)

@bot.message_handler(commands=['export'])
def cmd_export(msg):
    lst = '\n'.join(export(msg.chat.id))

    if len(lst) > 0:
        buf = io.BytesIO(bytes(lst, 'utf-8'))
        buf.name = f'export.txt'
        bot.send_document(msg.chat.id, buf)
    else:
        bot.send_message(msg.chat.id, 'You do not have any channels')

def get_import(msg):
    file_id_info = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    urls_list = downloaded_file.decode('utf-8').split('\n')
    del urls_list[-1]
    import_(msg.chat.id, urls_list)
    bot.send_message(msg.chat.id, 'Channels were successfully added!')

@bot.message_handler(commands=['import'])
def cmd_import(msg):
    link_msg = bot.send_message(msg.chat.id, 'Send me a .txt file with list of urls')
    bot.register_next_step_handler(link_msg, get_import)

def bot_polling():
    bot.polling(none_stop=True)