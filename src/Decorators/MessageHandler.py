import functionManager
from Handler import *
import sadDec

class MessageHandler(Handler):
    def __init__(self, func, filter, funcName = None):
        super(MessageHandler, self).__init__(func, sadDec._HANDLER_TYPE_MESSAGE_, funcName)
        self.filter = filter
        functionManager.functionManager.addMessage(self)
    

    
