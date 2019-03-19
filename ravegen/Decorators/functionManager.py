from telegram.ext import CommandHandler, MessageHandler, Filters
import telegram
import sadDec

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
        for _, func in self.messages.iteritems():
            func(message=func.filter)

    def generateHandlers(self, dispatcher):
        self.generateCommandHandlers(dispatcher)
        self.generateMsgHandlers(dispatcher)
        self.generateErrorHandlers(dispatcher)
        self.generateHelpCommand(dispatcher)

    def generateCommandHandlers(self, distpatcher):
        for _, command in self.commands.iteritems():
            distpatcher.add_handler(CommandHandler(command.funcName, command, pass_args = command.passArgs))

    def generateMsgHandlers(self, dispatcher):
        for _, message in self.messages.iteritems():
            if(message.filter == sadDec._MESSAGE_HANDLER_TEXT_):
                dispatcher.add_handler(MessageHandler(Filters.text, message))

    def generateErrorHandlers(self, dispatcher):
        for _, error in self.errors.iteritems():
            dispatcher.add_error_handler(error)
    
    def generateHelpCommand(self, dispatcher):
        if sadDec._BOT_HELP_COMMAND_ not in self.commands:
            def help(bot, update):
                replyText = bot.first_name + "\n"
                replyText += "*Commands:*\n"
                for key, func in self.commands.iteritems():
                    key = self.formatFunctionName(key)
                    if(func.description):
                        replyText += "/" + key + ": " + func.description + "\n"
                    else:
                        replyText += "/" + key + "\n"
                for key, func in self.messages.iteritems():
                    if(func.filter == sadDec._MESSAGE_HANDLER_TEXT_):
                        replyText += "*For text messages:* " + func.description
                update.effective_message.reply_text(replyText, parse_mode=telegram.ParseMode.MARKDOWN)
            dispatcher.add_handler(CommandHandler(sadDec._BOT_HELP_COMMAND_, help))

    def formatFunctionName(self, key):
        newKey = ""
        for c in key:
            if(c == '_'):
                newKey += "\\"
            newKey += c
        return newKey

functionManager = FunctionManager()
