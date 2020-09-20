import telebot
from config import TG_TOKEN

# bot init
bot = telebot.TeleBot(TG_TOKEN)

from .commands import bot_polling
from .videos_checker import videos_checker