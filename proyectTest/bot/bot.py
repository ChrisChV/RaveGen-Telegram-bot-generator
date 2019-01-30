from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import logging 
import os 
import sys 
sys.path.insert(0, 'modules')
from echo import *
from start import *

if __name__ == "__main__":
	TOKEN = "TOKEN"
	PORT = PORT
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
	logger = logging.getLogger(__name__)
	updater = Updater(TOKEN)
	dispatcher = updater.dispatcher
	echo_handler = CommandHandler('echo',echo)
	dispatcher.add_handler(echo_handler)
	start_handler = CommandHandler('start',start)
	dispatcher.add_handler(start_handler)
	updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path="PATH")
	updater.bot.setWebhook("URL")
	updater.idle()
