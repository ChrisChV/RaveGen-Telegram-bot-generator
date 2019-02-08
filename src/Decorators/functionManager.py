from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import functools

class FunctionManager:
    def __init__(self):
        self.commands = {}
        self.messages = {}
        self.errors = {}
    

    def addCommand(self, commandHandler):
        self.commands[commandHandler.funcName] = commandHandler

    def addMessage(self, messageHandler):
        self.messages[messageHandler.funcName] = messageHandler
    
    def addError(self, errorHandler):
        self.errors[errorHandler.funcName] = errorHandler

    def test_run(self):
        for key, func in self.messages.iteritems():
            func(message=func.filter)

    def generateHandlers(self, dispatcher):
        for key, message in self.messages.iteritems():
            if(message.filter == "text"):
                dispatcher.add_handler(MessageHandler(Filters.text, message))

functionManager = FunctionManager()

        
