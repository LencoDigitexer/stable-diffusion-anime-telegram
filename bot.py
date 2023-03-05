import telebot
import requests
import base64
from stablediff import get_ai_image
import os

token = "5587741514:AAF0e7hu_UyCtTFGQFLIyjnwJwCeSyXObUw"
'''
try:
    from config import token
except ImportError:
    if os.environ.get('token'):
        token = os.environ.get('token')
    else:
        print("I can't find bot token!")
        exit()
        '''
    
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["photo"])
def start(message):

    bot.send_message(message.from_user.id, "**Hello, Welcome to AnimeConvertorBot. This bot was made by @MznStudiosOfc.**")

    # Get Photo ID
    fileID = message.photo[-1].file_id
    filepath = bot.get_file(fileID).file_path

    # Downlading your photo
    r = requests.get(
        "https://api.telegram.org/file/bot" + token + "/" + filepath,
        timeout=None,
        stream=True,
    )

    # Convert Image To Anime
    base64_image_string = base64.b64encode(r.content).decode("utf-8")

    # Getting a link to the processed image
    try:
        ai_image = get_ai_image(base64_image_string)["media_info_list"][0]["media_data"]
        bot.send_photo(message.from_user.id, ai_image)
    except:
        bot.send_message(message.from_user.id, "❌️ An error has occurred, Please try again")


bot.polling(none_stop=True, interval=0)
