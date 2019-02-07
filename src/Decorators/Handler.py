class Handler(object):
    def __init__(self, func, handlerType):
        self.funcName = func.__name__ 
        self.func = func
        self.handlerType = handlerType
    
    