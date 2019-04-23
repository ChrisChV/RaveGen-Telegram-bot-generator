from ravegen import *

@RaveGen
@Command(description='To Upper')
def caps(message):
	if message == '':
		return 'The argument is missing'
	return message.upper()
