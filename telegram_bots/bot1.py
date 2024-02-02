import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message):
    print(f'Message: {message.text}')
    bot.send_message(message.chat.id, 'Привет, я телеграм Бот!')


@bot.message_handler(func=lambda message: True)
def message_handler_func(message):
    print(f'Message: {message.text}')
    bot.send_message(message.chat.id, 'Это текст')


@bot.message_handler(content_types=['audio'])
def audio_handler(message):
    print(f'Message: {message.audio}')
    bot.send_message(message.chat.id, 'Это аудио')


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, 'Работает функция echo:')
    bot.send_message(message.chat.id, message.text)


bot.polling()
