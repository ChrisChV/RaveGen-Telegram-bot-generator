from ravegen import *

@RaveGen
@Text(description='Reply the same message')
def echo(message):
	menu = [[('presioname', 'url::https://github.com/ChrisChV/RaveGen-Telegram-bot-generator')]]
	return message, menu
