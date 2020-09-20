import sys
from os import environ
import telebot

if 'TG_TOKEN' not in environ:
    sys.exit(1)

TG_TOKEN = environ['TG_TOKEN']

# bot init
bot = telebot.TeleBot(TG_TOKEN)

from .commands import bot_polling
from .videos_checker import videos_checker