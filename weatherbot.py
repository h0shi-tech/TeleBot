import telebot
import requests
import json

bot = telebot.TeleBot('6551051283:AAFo_VWOtnAUOJC8eSonVF2KMPuv77MW64I')
API = 'be260d6d417a8ffe6ceacf6b0092e4ca'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp} °С')

        image = 'sunny.jpg' if temp > 5.0 else 'rainy.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан неверно')


bot.polling(none_stop=True)
