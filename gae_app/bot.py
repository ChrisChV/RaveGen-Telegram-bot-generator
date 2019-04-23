#HEADERS
#TokenFlag False
import sys
from telegram.ext import Updater
from telegram import Update
from flask import Flask, request
import ravegen.Decorators.functionManager as functionManager 
sys.path.insert(0, '.')
import modules
import logging

app = Flask(__name__)
global updater
global TOKEN
TOKEN = '655780268:AAEiIzy3IbW4tckEMQhF4axX54qfGYzO7iA'
updater = Updater(TOKEN)

@app.route("/" + TOKEN, methods=['POST'])
def webhook_handler():
	if request.method == "POST":
		logging.info(request.get_json(force=True))
		update = Update.de_json(request.get_json(force=True), updater.bot)
		updater.dispatcher.process_update(update)
	return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
	dispatcher = updater.dispatcher
	functionManager.functionManager.generateHandlers(dispatcher)
	s = updater.bot.setWebhook("https://ravegentest22222.appspot.com/" + TOKEN)	
	if s:
		return "webhook setup ok"
	else:
		return "webhook setup failed"

@app.route('/')
def index():
	return 'Hello'


