import telebot
from telebot import types
from keyboards import menu_kb
import adad
import getr
import getr_tod

import datetime
import re


def register_commands(bot):
    global prv
    prv = []
    
    def make_day_today(today, form):
        lessons = getr_tod.loader_tod(today, form)
        return f'{lessons}'

    def make_day(tomorrow, tomorrow1, tomorrow2, form):
        lessons = getr.loader(tomorrow, tomorrow1, tomorrow2, form)
        return f'{lessons}'
    
    def get_lessons_today(message):
        today = datetime.date.today()

        if len(prv) > 1:
            tec = prv[0]
            less =prv[1]

            form = adad.get_form(tec, less)

            if form:
                lessons = make_day_today(today, form)
                bot.send_message(message.chat.id, lessons)
            else:
                bot.send_message(message.chat.id, 'Сначала выберите урок')
        else:
            bot.send_message(message.chat.id, 'Сначала выберите урок')

    def get_lessons(message):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        tomorrow1 = today + datetime.timedelta(days=2)
        tomorrow2 = today + datetime.timedelta(days=3)

        if len(prv) > 1:

            tec = prv[0]
            less = prv[1]       

            form = adad.get_form(tec, less)


            if form:
                lessons = make_day(tomorrow,  tomorrow1, tomorrow2, form)
                bot.send_message(message.chat.id, lessons)
            else:
                bot.send_message(message.chat.id, 'Сначала выберите урок')
        else:
            bot.send_message(message.chat.id, 'Сначала выберите урок')





    def ang(call, message):
        ch_gr = types.InlineKeyboardMarkup()
        ch_gr.row_width = 2
        ch_gr.add(types.InlineKeyboardButton('Рослякова', callback_data='ros'), types.InlineKeyboardButton('Вихрист', callback_data='vih'))
        ch_gr.add(types.InlineKeyboardButton('Осолодкина', callback_data='oso'), types.InlineKeyboardButton('Борисова', callback_data='bor'), 
                types.InlineKeyboardButton('Сачкова', callback_data='sac'))
        
        bot.send_message(call.from_user.id, 'Веберите группу', reply_markup=ch_gr)
        bot.delete_message(message.chat.id, message_id=message.message_id)
        bot.delete_message(message.chat.id, message_id=message.message_id - 1)

    def inf(call, message):
        ch_gr = types.InlineKeyboardMarkup()
        # ch_gr.row_width = 2 (ДЛЯ ВТОРОГО УЧИТЕЛЯ)
        ch_gr.add(types.InlineKeyboardButton('Лукачева', callback_data='lk'))#, types.InlineKeyboardButton('Лосева', callback_data='ls'))
        bot.send_message(call.from_user.id, 'Выберите группу', reply_markup=ch_gr)
        bot.delete_message(message.chat.id, message_id=message.message_id)
        bot.delete_message(message.chat.id, message_id=message.message_id - 1)

    #Добавляет в список выбор урока и группы
    def pr(call, les, teach, message):       
        bot.send_message(call.from_user.id, f'Теперь вы привязаны к уроку {les}, группе {teach}', reply_markup=menu_kb())
        bot.delete_message(message.chat.id, message_id=message.message_id)
        if len(prv) > 0:
            prv.clear()
        
        prv.append(les)
        prv.append(teach)
        # bot.send_message(message.chat.id, prv[0])
        # bot.send_message(message.chat.id, prv[1])
        return prv



    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, 'Привет! Я бот который может прислать расписание для учителя!')

        ch_s = types.InlineKeyboardMarkup()
        ch_s.row_width = 2
        ch_s.add(types.InlineKeyboardButton('Информатика', callback_data='s1'), types.InlineKeyboardButton('Английский язык', callback_data='s2'))

        bot.send_message(message.chat.id, 'Выберите ваш урок', reply_markup=ch_s)

    @bot.callback_query_handler(func=lambda call:True)
    def query_handler(call):
        if call.data == 's1':
            inf(call, call.message)
            bot.answer_callback_query(call.id, text='Выбран урок информатика')
        elif call.data == 's2':
            ang(call, call.message)
            bot.answer_callback_query(call.id, text='Выбран урок Английский язык')
        
        elif call.data == 'lk':
            les = 'Информатика'
            teach = 'Лукачевой'
            pr(call, les, teach, call.message)
        # elif call.data == 'ls':
        #     les = 'Информатика'
        #     teach = 'Лосевой'
        #     pr(call, les, teach, call.message) Второй учитель
        elif call.data == 'ros':
            les = 'Английский язык'
            teach = 'Росляковой'
            pr(call, les, teach, call.message)
        elif call.data == 'vih':
            les = 'Английский язык'
            teach = 'Вихрист'
            pr(call, les, teach, call.message)
        elif call.data == 'bor':
            les = 'Английский язык'
            teach = 'Борисовой'
            pr(call, les, teach, call.message)
        elif call.data == 'oso':
            les = 'Английский язык'
            teach = 'Осолодкиной'
            pr(call, les, teach, call.message)
        elif call.data == 'sac':
            les = 'Английский язык'
            teach = 'Сачковой'
            pr(call, les, teach, call.message)

    @bot.message_handler(commands=['menu'])
    def show_menu(message):
        bot.send_message(message.chat.id, 'Меню', reply_markup=menu_kb())

    @bot.message_handler(commands=['rem'])
    def rem(message):
        bot.send_message(message.chat.id, 'Меню скрыто', reply_markup=types.ReplyKeyboardRemove())

    @bot.message_handler(content_types=['text'])
    def comm(message):
        if message.text == 'Узнать расписание на сегодня':
            get_lessons_today(message)
        elif message.text == 'Узнать расписание':
            get_lessons(message)
        elif message.text == 'Команды':
            bot.send_message(message.chat.id, 'Команды\n\n/start - Начать заново\n/menu - показать меню\n/rem - Скрыть меню')
        elif len(prv) == 0 or len(prv) == 1:
            bot.send_message(message.chat.id, 'Сначала выберите урок и группу')
        else:
            bot.send_message(message.chat.id, 'я не знаю таких команд :(')

    


    