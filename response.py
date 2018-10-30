import urllib
import requests

from BotConfiguration import BotConfiguration
from bot import BasicActions


class Response:

    def __init__(self):
        self.URL = BotConfiguration.BOT_URL
        self.bot_basic_action = BasicActions()
        self.pressed_item = False
        self.TOKEN = BotConfiguration.TOKEN

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
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            response_array = [token for token in text.split(" ")]

            if response_array[0] == '/nudes' or response_array[0] == '/god':
                response = self.bot_basic_action.get_rms("https://rms.sexy/?js")
                position = response.find("src=\"/img/")
                response = response[position:].split(" ")[0][5:-1]
                self.bot_basic_action.download_photo(response)
                self.send_image(chat, response)

    def send_message(self, text, chat_id, reply_markup=None):
        text = urllib.parse.quote_plus(text)
        url = self.URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
        if reply_markup:
            url += "&reply_markup={}".format(reply_markup)
        self.bot_basic_action.get_url(url)

    def send_image(self, chat_id, path):
        url = "https://api.telegram.org/" + self.TOKEN + "/sendPhoto"
        files = {'photo': open("." + path, 'rb')}
        data = {'chat_id': str(chat_id)}
        requests.post(url, files=files, data=data)
