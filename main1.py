import telebot
from telebot import types
import asyncio
import logging
import configg
import handlers


token = configg.TOKEN
bot = telebot.TeleBot(token)

handlers.register_commands(bot)






bot.polling(non_stop=True)




