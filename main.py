import telebot
from BotConfiguration import BotConfiguration
from bot import BasicActions


bot = telebot.TeleBot(BotConfiguration.TOKEN)
bot_basic_action = BasicActions()
subscribed_id = []


def get_rms_photo():
    image_path = bot_basic_action.get_rms("https://rms.sexy/?js")
    formatted_path = bot_basic_action.format_image_path(image_path)
    bot_basic_action.download_photo(formatted_path)
    return formatted_path


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome to the magic Richard Matthew Stallman Bot, you can send /list to "
                                      "show the available commands")


@bot.message_handler(commands=['list'])
def list_commands(message):
    bot.send_message(message.chat.id, "The available commands:\n"
                                      "\t\start\n"
                                      "\t\help\n"
                                      "\t \god\n"
                                      "\t \\nudes\n"
                                      "\t \stallman\n"
                                      "\t \\rms\n"
                                      "\t \song\n"
                                      "\t \github\n"
                                      "\t \subscribe\n"
                                      "\t \\unsubscribe")


@bot.message_handler(commands=['god', 'nudes', 'stallman', 'rms'])
def send_photo(message):
    image_path = bot_basic_action.get_rms("https://rms.sexy/?js")
    formatted_path = bot_basic_action.format_image_path(image_path)
    bot_basic_action.download_photo(formatted_path)
    bot.send_photo(chat_id=message.chat.id, photo=open("." + formatted_path, 'rb'))
    bot_basic_action.clean_folder()


@bot.message_handler(commands=['song'])
def send_audio(message):
    bot.send_audio(chat_id=message.chat.id, audio=open("./song/Free Software Song.mp3", 'rb'))


@bot.message_handler(commands=['github'])
def send_github(message):
    bot.reply_to(message, "My code is available in this github: https://github.com/jcanabarro/StallmanBot")


@bot.message_handler(commands=['subscribe'])
def subscribe_id(message):
    if message.chat.id not in subscribed_id:
        subscribed_id.append(message.chat.id)
        bot.reply_to(message,
                     "You now are subscribed on RMS timed photos, 3 time per day i'll send to you awesome photos")

    else:
        bot.send_message(message.chat.id, "You already subscribed on this service")


@bot.message_handler(commands=['unsubscribe'])
def subscribe_id(message):
    if message.chat.id in subscribed_id:
        subscribed_id.remove(message.chat.id)
        bot.reply_to(message, "Unfortunately you don't want this magic service anymore, but if you change your opinion,"
                              " send to me /subscribe again")
    else:
        pass


bot.polling()
