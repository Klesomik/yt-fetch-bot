import time
from database import get_db
from . import bot

def videos_checker():
    last_video_buffer = {}

    while True:
        time.sleep(1.0)
        for channel in get_db():
            prv_link = last_video_buffer.get(channel.url) 
            nxt_link = channel.get_latest_video()

            if prv_link != nxt_link:
                last_video_buffer.update({ channel.url : nxt_link })
                if prv_link != None:
                    bot.send_message(channel.chat_id, nxt_link)

            time.sleep(0.1)