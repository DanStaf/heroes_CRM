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

    def start_handler(self, message):

        print(message.from_user.username, 'push START')
        print(message.chat.id)

        keyboard = self.inline_keyboard()
        self.bot.send_message(message.chat.id,
                              "Привет! Я виртуальный бот Данил!\nКто ты, Герой?",
                              reply_markup=keyboard)

    def inline_keyboard(self):

        buttons = telebot.types.InlineKeyboardMarkup(row_width=4)
        button_1 = telebot.types.InlineKeyboardButton("Наставник", callback_data='mentor')
        button_2 = telebot.types.InlineKeyboardButton("Вожатая", callback_data='counselor')
        button_3 = telebot.types.InlineKeyboardButton("Старший наставник", callback_data='h_mentor')
        button_4 = telebot.types.InlineKeyboardButton("Старшая вожатая", callback_data='h_counselor')
        buttons.add(button_1, button_2)
        buttons.add(button_3, button_4)

        return buttons

    def reply_keyboard(self):

        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=4)
        button_1 = telebot.types.KeyboardButton("Наставник")
        button_2 = telebot.types.KeyboardButton("Вожатая")
        button_3 = telebot.types.KeyboardButton("Старший наставник")
        button_4 = telebot.types.KeyboardButton("Старшая вожатая")
        keyboard.add(button_1, button_2)
        keyboard.add(button_3, button_4)

        return keyboard

    def remove_keyboard(self, message):
        keyboard = telebot.types.ReplyKeyboardRemove()
        self.bot.send_message(message.chat.id,
                              'Удаляю клавиатуру',
                              reply_markup=keyboard)

    def mentor_handler(self, call):
        self.bot.send_message(call.message.chat.id, f'Ура наставникам!')

    def counselor_handler(self, call):
        self.bot.send_message(call.message.chat.id, f'Ура вожатым!')

    def h_mentor_handler(self, call):
        self.bot.send_message(call.message.chat.id, f'Ура старшему!')

    def h_counselor_handler(self, call):
        self.bot.send_message(call.message.chat.id, f'Ура старшему!')




