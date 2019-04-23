from ravegen import *

@RaveGen
@Text(description='Reply the same message')
def echo(message):
	return message
