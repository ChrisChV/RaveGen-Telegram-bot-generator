import functionManager
from Handler import *

class MessageHandler(Handler):
    def __init__(self, func, filter):
        super(MessageHandler, self).__init__(func, "message")
        self.filter = filter
        functionManager.functionManager.addMessage(self)
    
    def __call__(self, *arg, **karg):
        return self.func(*arg, **karg)

    
