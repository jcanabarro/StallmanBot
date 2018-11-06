import requests
import urllib.request
import shutil
import os
import time


class BasicActions:

    def __init__(self):
        pass

    def get_rms(self, url):
        return str(requests.get(url).content)

    def download_photo(self, path):
        urllib.request.urlretrieve("https://rms.sexy" + path, "." + path)

    def clean_folder(self):
        time.sleep(1)
        shutil.rmtree("img/")
        if not os.path.exists("img/"):
            os.makedirs("img/")

    def format_image_path(self, path):
        position = path.find("src=\"/img/")
        return path[position:].split(" ")[0][5:-1]
