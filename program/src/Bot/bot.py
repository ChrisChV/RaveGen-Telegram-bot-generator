from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import logging 
import os 
import sys 
sys.path.insert(0, '../../modules')
from echo import *
from start import *

if __name__ == "__main__":
	TOKEN = "717635382:AAE9Qy-9Vd0wAsUAVnII9y9CLE-8E-s9EAA"
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
	logger = logging.getLogger(__name__)
	updater = Updater(TOKEN)
	dispatcher = updater.dispatcher
	echo_handler = CommandHandler('echo',echo)
	dispatcher.add_handler(echo_handler)
	start_handler = CommandHandler('start',start)
	dispatcher.add_handler(start_handler)
	updater.bot.deleteWebhook()
	updater.start_polling()
	updater.idle()

