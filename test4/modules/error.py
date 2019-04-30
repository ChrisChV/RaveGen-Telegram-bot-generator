from ravegen import *

@RaveGen
@Error
def error(message):
	return 'ERROR: ' + message
