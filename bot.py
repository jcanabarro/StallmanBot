import json
import requests
import urllib.request
import shutil
import os
import time


class BasicActions:

    def __init__(self):
        pass

    def get_url(self, url):
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content

    def get_json_from_url(self, url):
        content = self.get_url(url)
        js = json.loads(content)
        return js

    def build_keyboard(self, items):
        keyboard = [[item] for item in items]
        reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}
        return json.dumps(reply_markup)

    def get_rms(self, url):
        return str(requests.get(url).content)

    def download_photo(self, path):
        urllib.request.urlretrieve("https://rms.sexy/" + path, "." + path)

    def clean_folder(self):
        time.sleep(1)
        shutil.rmtree("img/")
        if not os.path.exists("img/"):
            os.makedirs("img/")

    def format_image_path(self, path):
        position = path.find("src=\"/img/")
        return path[position:].split(" ")[0][5:-1]
