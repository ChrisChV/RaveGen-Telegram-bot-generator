from Handler import *
import functools
import functionManager
import sadDec

class Command(Handler):
    def __init__(self, func, funcName = None, passArgs = False):
        functools.update_wrapper(self, func)
        super(Command, self).__init__(func, sadDec._HANDLER_TYPE_COMMAND_, funcName=funcName)
        self.passArgs = passArgs
        functionManager.functionManager.addCommand(self)
        