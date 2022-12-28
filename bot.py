import telebot
import requests
import base64
from stablediff import get_ai_image
import os

token = ""

try:
    from config import token
except ImportError:
    if os.environ.get('token'):
        token = os.environ.get('token')
    else:
        print("Не обнаружен токен во временной переменной")
        exit()
    
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["photo"])
def start(message):

    bot.send_message(message.from_user.id, "🤖Нейросеть конвертирует фото")

    # Получаем ID фоторгафии
    fileID = message.photo[-1].file_id
    filepath = bot.get_file(fileID).file_path

    # Скачиваем фотографию
    r = requests.get(
        "https://api.telegram.org/file/bot" + token + "/" + filepath,
        timeout=None,
        stream=True,
    )

    # Преобразовываем картинку в base64
    base64_image_string = base64.b64encode(r.content).decode("utf-8")

    # Получаем ссылку на обработанное изображение
    try:
        ai_image = get_ai_image(base64_image_string)["media_info_list"][0]["media_data"]
        bot.send_photo(message.from_user.id, ai_image)
    except:
        bot.send_message(message.from_user.id, "🚨 Произошла ошибка, попробуйте еще раз")


bot.polling(none_stop=True, interval=0)
