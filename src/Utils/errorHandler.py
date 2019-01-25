import os
import sad

class ErrorHandler:
    _errorList = {}
    
    def __init__(self):
        self._errorList = {}

    def addError(self, error, errorType = sad._NORMAL_ERROR_):
        if not errorType in self._errorList:
            self._errorList[errorType] = []
        self._errorList[errorType].append(error)

    def handle(self):
        #TODO si es critico, matar el programa
        
        for key, typesOfErrors in self._errorList.iteritems():
            for error in typesOfErrors:
                print(error)
        


    