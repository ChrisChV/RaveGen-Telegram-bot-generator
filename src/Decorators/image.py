from MessageHandler import *
import functools

class Image(MessageHandler):
    def __init__(self, func):
        functools.update_wrapper(self, func)
        super(Image, self).__init__(func, "image")
