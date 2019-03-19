import functools
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
        _filter = karg["filter"]
        def _m_handler(bot, update):
            message = update.effective_message.text
            reply = self.handler(message=message)
            update.effective_message.reply_text(reply)

        _newMessageHandler = MessageHandler.MessageHandler(_m_handler, _filter, funcName=self.handler.funcName, description=self.handler.description)
        return _newMessageHandler

    def c_handler(self, *arg, **karg):
        def _c_handler(bot, update, args = None):
            message = ''
            if(args != None):
                message = ' '.join(args)
            reply = self.handler(message=message)
            update.effective_message.reply_text(reply)

        _newCommandHandler = CommandHandler._Command(_c_handler, funcName=self.handler.funcName, passArgs=True, description=self.handler.description)
        return _newCommandHandler

    def e_handler(self, *arg, **karg):
        def _e_handler(bot, update, error):
            reply = self.handler(message=str(error))
            print(reply)
        _newErrorHandler = Error.Error(_e_handler, funcName=self.handler.funcName)
        return _newErrorHandler
