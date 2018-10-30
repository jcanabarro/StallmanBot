import time

from response import Response


def main():
    bot = Response()
    last_update_id = None
    while True:
        updates = bot.get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = bot.get_last_update_id(updates) + 1
            bot.handle_updates(updates)
        time.sleep(1)


if __name__ == '__main__':
    main()