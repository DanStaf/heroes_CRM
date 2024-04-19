import telebot
import time

"""
id: 1816252417 Данил
id: 1378096615 Катя
"""

"""
Сначала нужно написать /start
Затем название валюты или stop
"""

USER_DATA = {}

telebot.apihelper.ENABLE_MIDDLEWARE = True

# Укажем token полученный при регистрации бота
with open("TG_token_file") as f:
    TG_TOKEN = f.read()

bot = telebot.TeleBot(TG_TOKEN)


# Начнем обработку. Если пользователь запустил бота, ответим
@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    print(message.from_user.id, 'added (push START)')

    global USER_DATA
    """#stop_button = telebot.types.InlineKeyboardMarkup(row_width=1)
    #button_stop = telebot.types.InlineKeyboardButton("Stop", callback_data='stop')
    #stop_button.add(button_stop)

    #bot.send_message(message.from_user.id, " Здравствуйте. Я виртуальный бот Дэн!\n"
    #                                       " Введите имя валюты, чтобы узнать курс к рублю",
    #                 reply_markup=stop_button)
    """
    #LIST_OF_USERS_ID.append(message.from_user.id)
    #print('id added:', message.from_user.id)

    bot.send_message(message.from_user.id, " Здравствуйте. Я виртуальный бот Данил!")

    #USER_DATA[message.from_user.id] = {'in_processing': False, 'currencies': []}

"""
# Если пользователь что-то написал, ответим
@bot.message_handler(func=lambda message: True)
def get_text_messages(message):

    global USER_DATA
    message_id = message.from_user.id

    if message.text == 'stop':
        if USER_DATA[message_id]['in_processing']:
            USER_DATA[message_id]['in_processing'] = False
            USER_DATA[message_id]['currencies'].clear()
            reply = "Stopped"
            print('stop requested')
        else:
            reply = "Nothing in process"

        bot.send_message(message_id, reply)
        print(USER_DATA)

    else:
        user_currency = message.text
        USER_DATA[message_id]['currencies'].append(user_currency)
        print(f'{message_id} requested {user_currency}')

        if not USER_DATA[message_id]['in_processing']:
            USER_DATA[message_id]['in_processing'] = True
            send_rates_to_tg(message_id, 10)


def send_rates_to_tg(message_id, delay=60):
    global USER_DATA

    while USER_DATA[message_id]['in_processing']:
        reply = ""
        for currency in USER_DATA[message_id]['currencies']:
            reply += f"1 {currency} = 'its rate' RUB\n"
        #reply += "IN_PROCESSING = " + str(USER_DATA[message_id]['in_processing'])

        bot.send_message(message_id, reply)
        print(USER_DATA)
        time.sleep(delay)"""


# Запустим обработку событий бота
bot.infinity_polling(none_stop=True, interval=1)

