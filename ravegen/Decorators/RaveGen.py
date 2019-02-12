import functools
import Handler
import MessageHandler
import CommandHandler
import Error
import functionManager
import sadDec

class RaveGen:
    def __init__(self, handler):
        functools.update_wrapper(self, handler)
        self.handler = handler
        self.getNewHandler()
        

    def getNewHandler(self):
        if(self.handler.handlerType == sadDec._HANDLER_TYPE_COMMAND_):
            functionManager.functionManager.addCommand(self.c_handler())

        if(self.handler.handlerType == sadDec._HANDLER_TYPE_MESSAGE_):
            functionManager.functionManager.addMessage(self.m_handler(filter=self.handler.filter))

        if(self.handler.handlerType == sadDec._HANDLER_TYPE_ERROR_):
            functionManager.functionManager.addError(self.e_handler())

    def m_handler(self, *arg, **karg):
        filter = karg["filter"]
        def _m_handler(bot, update):
            message = update.effective_message.text
            reply = self.handler(message=message)       
            update.effective_message.reply_text(reply)

        _newMessageHandler = MessageHandler.MessageHandler(_m_handler, filter, funcName=self.handler.funcName)
        return _newMessageHandler

    def c_handler(self, *arg, **karg):
        def _c_handler(bot, update, args = None):
            message = ''
            if(args != None):
                message = ' '.join(args)
            reply = self.handler(message=message)
            update.effective_message.reply_text(reply)
        
        _newCommandHandler = CommandHandler.Command(_c_handler, funcName=self.handler.funcName, passArgs=True)
        return _newCommandHandler
            
    def e_handler(self, *arg, **karg):
        def _e_handler(bot, update, error):
            reply = self.handler(message=str(error))
            print(reply)
        _newErrorHandler = Error.Error(_e_handler, funcName=self.handler.funcName)
        return _newErrorHandler