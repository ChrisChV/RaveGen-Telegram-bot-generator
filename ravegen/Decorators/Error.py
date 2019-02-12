from Handler import *
import functionManager
import functools
import sadDec

class Error(Handler):
    def __init__(self, func, funcName = None):
        functools.update_wrapper(self, func)
        super(Error, self).__init__(func, sadDec._HANDLER_TYPE_ERROR_, funcName=funcName)
        functionManager.functionManager.addError(self)
