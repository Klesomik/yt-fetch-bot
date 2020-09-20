from bot import bot_polling

def main():
    try:
        bot_polling()
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    main()
