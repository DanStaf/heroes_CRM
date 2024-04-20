import telebot
import time


class TG_API:

    def __init__(self):

        # Укажем token полученный при регистрации бота
        with open("../data/TG_token_file") as f:
            self.__token = f.read()

        self.bot = telebot.TeleBot(self.__token)

    def get_bot(self):
        return self.bot

    @staticmethod
    def inline_keyboard(buttons: dict):
        keyboard = telebot.types.InlineKeyboardMarkup(row_width=len(buttons))

        b = []
        i = 0
        for key, value in buttons.items():

            button = telebot.types.InlineKeyboardButton(value, callback_data=key)
            b.append(button)

            i += 1
            if i > 1:
                keyboard.add(*b)
                b.clear()
                i = 0

        if i > 0:
            keyboard.add(*b)

        return keyboard

    @staticmethod
    def reply_keyboard(buttons: list):
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=len(buttons))

        b = []
        i = 0
        for text in buttons:
            button = telebot.types.KeyboardButton(text)
            b.append(button)

            i += 1
            if i > 1:
                keyboard.add(*b)
                b.clear()
                i = 0

        if i > 0:
            keyboard.add(*b)

        return keyboard

    def remove_keyboard(self, message):
        keyboard = telebot.types.ReplyKeyboardRemove()
        self.bot.send_message(message.chat.id,
                              '.',
                              reply_markup=keyboard)

    # Handlers

    def start_handler(self, message):

        print(f'{message.from_user.username} (id {message.chat.id}) push START')

        buttons = ["Наставник",
                   "Вожатая",
                   "Старший наставник",
                   "Старшая вожатая"
                   ]

        keyboard = self.reply_keyboard(buttons)

        self.bot.send_message(message.chat.id,
                              "Привет! Я виртуальный бот ШГ!\nКто ты, Герой?",
                              reply_markup=keyboard)

    def text_handler(self, message):

        print(message.from_user.username, 'sent:', message.text)

        # можно удалить клавиатуру, можно нет
        # при желании её можно скрыть и открыть
        # а если удалить, то заново открыть нельзя
        #self.remove_keyboard(message)

        text = "Раз, два, три, Ура!"

        if message.text == "Наставник":
            buttons = {
                'attendance': "Отметить явку",
                'new_heroes': "Проверить новичков",
                'start': "Начать заново"
            }
        elif message.text == "Вожатая":
            buttons = {
                'mom_attendance': "Отметить явку (надо?)",
                'add_hero': "Добавить новичка",
                'bonus': "Проверить оплату",
                'start': "Начать заново"
            }
        elif message.text == "Старший наставник":
            buttons = {
                'check_attendance': "Проверить явку",
                'add_hero': "Добавить новичка",
                'new_heroes': "Проверить новичков",
                'bonus': "Проверить бонусы",
                'start': "Начать заново"
            }
        elif message.text == "Старшая вожатая":
            buttons = {
                'mom_check_attendance': "Проверить явку (надо?)",
                'add_hero': "Добавить новичка",
                'start': "Начать заново"
            }
        elif message.text == "Начать заново":
            buttons = {}
            self.start_handler(message)

        elif message.text == "Отметить явку":
            text = "Множественный опрос - по списку ребят"
            buttons = {}

        elif message.text == "Проверить явку":
            text = "Список отделений с количеством отмеченных ребят"
            buttons = {}

        else:
            text = "Неизвестная команда"
            buttons = {}

        keyboard = self.reply_keyboard(list(buttons.values()))

        self.bot.send_message(message.chat.id, text, reply_markup=keyboard)

    """def call_handler(self, call):
        print(call.message.from_user.username, 'call:', call.message.text)
    """

####################
