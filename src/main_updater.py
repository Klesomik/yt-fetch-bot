from bot import videos_checker

def main():
    try:
        videos_checker()
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    main()
