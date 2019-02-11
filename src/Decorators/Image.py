from MessageHandler import *
import functools
import sadDec

class Image(MessageHandler):
    def __init__(self, func):
        functools.update_wrapper(self, func)
        super(Image, self).__init__(func, sadDec._MESSAGE_HANDLER_IMAGE_)
