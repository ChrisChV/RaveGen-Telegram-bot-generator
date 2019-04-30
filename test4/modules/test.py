from ravegen import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup
import json

def build_callback(data):
    return_value = json.dumps(data)
    return return_value

#@Command
#def test(bot, update):
#    keyboard = [[InlineKeyboardButton('hola', callback_data=build_callback({"command": "start"})), InlineKeyboardButton('adios', url = "https://github.com/ChrisChV/RaveGen-Telegram-bot-generator")]]
#    reply_markup = InlineKeyboardMarkup(keyboard)
#    update.message.reply_text('Esto es una prueba de botones:', reply_markup=reply_markup)

@RaveGen
@Command
def test(message):
    menu = [[('hola', "command::caps, args::hola mundo"), ('adios', "url::https://github.com/ChrisChV")], [('pruebame', 'function::test2, message::AAA, index::10')]]
    return "Esto es una prueba de botones:", menu


@RaveGen
@RaveFunction
def test2(message, index):
    index = int(index)
    for i in range(0,index):
        message += 'O'
    return message
    

