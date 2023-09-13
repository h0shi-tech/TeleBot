import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6551051283:AAFo_VWOtnAUOJC8eSonVF2KMPuv77MW64I')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Перейти на сайт')
    markup.row(button1)
    button2 = types.KeyboardButton('Изменить текст')
    button3 = types.KeyboardButton('Удалить фото')
    markup.row(button2, button3)
    file = open('./photo.PNG', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Deleted')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Открыть сайт', url='https://pypi.org/project/pyTelegramBotAPI/')
    markup.row(button1)
    button2 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    button3 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    markup.row(button2, button3)
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://pypi.org/project/pyTelegramBotAPI/')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Помощь</b>', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name} ')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
