from MessageHandler import *
import functools

class Text(MessageHandler):
    def __init__(self, func):
        functools.update_wrapper(self, func)
        super(Text, self).__init__(func, "text")
    
    