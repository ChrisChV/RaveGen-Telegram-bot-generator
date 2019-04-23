#HEADERS
#TokenFlag False

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import logging 
import os 
import sys 
import ravegen.Decorators.functionManager as functionManager 
sys.path.insert(0, '.')
import modules

if __name__ == "__main__":
	TOKEN = "655780268:AAEiIzy3IbW4tckEMQhF4axX54qfGYzO7iA"
	PORT = os.environ.get('PORT')
	logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
	logger = logging.getLogger(__name__)
	updater = Updater(TOKEN)
	dispatcher = updater.dispatcher
	functionManager.functionManager.generateHandlers(dispatcher)
	updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path="655780268:AAEiIzy3IbW4tckEMQhF4axX54qfGYzO7iA")
	updater.bot.setWebhook("https://ravegentest54321.appspot.com/655780268:AAEiIzy3IbW4tckEMQhF4axX54qfGYzO7iA")
	updater.idle()
