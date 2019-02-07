import functools
import Handler
import MessageHandler
import functionManager


class RaveGen:
    def __init__(self, handler):
        functools.update_wrapper(self, handler)
        self.handler = handler
        self.newHandler = self.getNewHandler()
        functionManager.functionManager.addMessage(self.newHandler)
        

    def getNewHandler(self):
        if(self.handler.handlerType == "message"):
            return self.m_handler(filter=self.handler.filter)

    def m_handler(self, *arg, **karg):
        #def _m_handler(bot, update):
        #    message = update.effective_message.text
        #    reply = self.handler(message=message)       
        #    update.effective_message.reply_text(reply)
        filter = karg["filter"]
        def _m_handler(message):
            print("AAAAAAAAAA")
            reply = self.handler(message=message)
            print(reply)
            print("BBBBBBBB")
        _newMessageHandler = MessageHandler.MessageHandler(_m_handler, filter, funcName=self.handler.funcName)
        return _newMessageHandler

    
            
            
    

