import telebot
import time
from class_TG_API import TG_API

"""
id: 1816252417 Данил
id: 1378096615 Катя
"""

"""
Сначала нужно написать /start
Затем название валюты или stop
"""

telebot.apihelper.ENABLE_MIDDLEWARE = True

api = TG_API()
bot = api.get_bot()


# Начнем обработку. Если пользователь запустил бота, ответим
@bot.message_handler(commands=['start'])
def start_message(message):
    api.start_handler(message)


@bot.message_handler(commands=['rkb'])  # 'remove_keyboard'
def remove_keyboard(message):
    api.remove_keyboard(message)


@bot.callback_query_handler(func=lambda call: call.data == 'mentor')
def mentor_message(call):
    api.mentor_handler(call)


@bot.callback_query_handler(func=lambda call: call.data == 'counselor')
def mentor_message(call):
    api.counselor_handler(call)


@bot.callback_query_handler(func=lambda call: call.data == 'h_mentor')
def mentor_message(call):
    api.h_mentor_handler(call)


@bot.callback_query_handler(func=lambda call: call.data == 'h_counselor')
def mentor_message(call):
    api.h_counselor_handler(call)


# Если пользователь что-то написал, ответим
@bot.message_handler(func=lambda message: True)
def get_text_messages(message):
    print(message.text)


# Запустим обработку событий бота
bot.infinity_polling(none_stop=True, interval=1)

#################
