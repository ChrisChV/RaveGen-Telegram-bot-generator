from MessageHandler import *
import functools
import sadDec

class Text(MessageHandler):
    def __init__(self, func):
        functools.update_wrapper(self, func)
        super(Text, self).__init__(func, sadDec._MESSAGE_HANDLER_TEXT_)
    
    