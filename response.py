import urllib
import requests

from BotConfiguration import BotConfiguration
from bot import BasicActions


class Response:

    def __init__(self):
        self.URL = BotConfiguration.BOT_URL
        self.bot_basic_action = BasicActions()
        self.TOKEN = BotConfiguration.TOKEN
        self.reserved_words = ['/nudes', '/god', '/stallman', '/rms']

    def get_updates(self, offset=None):
        url = self.URL + "getUpdates?timeout=100"
        if offset:
            url += "&offset={}".format(offset)
        js = self.bot_basic_action.get_json_from_url(url)
        return js

    def get_last_update_id(self, updates):
        update_ids = []
        for update in updates["result"]:
            update_ids.append(int(update["update_id"]))
        return max(update_ids)

    def handle_updates(self, updates):
        for update in updates["result"]:
            # if update["message"]["chat"]["type"] == "group":
            #     continue
            # else:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            response_array = [token for token in text.split(" ")]
            if response_array[0] in self.reserved_words:
                image_path = self.bot_basic_action.get_rms("https://rms.sexy/?js")
                formatted_path = self.bot_basic_action.format_image_path(image_path)
                self.bot_basic_action.download_photo(formatted_path)
                self.send_image(chat, formatted_path)
                self.bot_basic_action.clean_folder()
            elif response_array[0] == '/help':
                self.send_message("Try to use /god or /stallman", chat)
            elif response_array[0] == '/start':
                self.send_message("Welcome to the magic Richard Matthew Stallman Bot, you can send /list to show "
                                  "the available commands", chat)
            elif response_array[0] == '/list':
                self.send_message("I'm just joking, I'll not /help you", chat)
            elif response_array[0] == '/donate':
                self.send_message("If you want to donate to FSF click here: https://my.fsf.org/donate/", chat)
            else:
                continue

    def send_message(self, text, chat_id, reply_markup=None):
        text = urllib.parse.quote_plus(text)
        url = self.URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
        if reply_markup:
            url += "&reply_markup={}".format(reply_markup)
        self.bot_basic_action.get_url(url)

    def send_image(self, chat_id, path):
        url = "https://api.telegram.org/bot" + self.TOKEN + "/sendPhoto"
        files = {'photo': open("." + path, 'rb')}
        data = {'chat_id': str(chat_id)}
        requests.post(url, files=files, data=data)
