import telebot
from telebot import types

def menu_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Узнать расписание')
    button2 = types.KeyboardButton('Узнать расписание на сегодня')
    button3 = types.KeyboardButton('Команды')
    kb.add(button1, button2)
    kb.add(button3)
    return kb