import telebot
from BotConfiguration import BotConfiguration
from bot import BasicActions

bot = telebot.TeleBot(BotConfiguration.TOKEN)
bot_basic_action = BasicActions()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome to the magic Richard Matthew Stallman Bot, you can send /list to "
                                      "show the available commands")


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


bot.polling()
