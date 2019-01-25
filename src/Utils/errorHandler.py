import os
import sys
import sad

class ErrorHandler:
    _errorList = {}
    _errorHandlerName = ""

    def __init__(self, name):
        self._errorList = {}
        self._errorHandlerName = name

    def addError(self, error, errorType = sad._NORMAL_ERROR_):
        if not errorType in self._errorList:
            self._errorList[errorType] = []
        self._errorList[errorType].append(error)

    def handle(self):
        #TODO si es critico, matar el programa
        terminate = False

        for typeOfError, errors in self._errorList.iteritems():
            if(typeOfError == sad._CRITICAL_ERROR_):
                terminate = True            
            for error in errors:
                print(self._errorHandlerName + ": " + error)
        
        if terminate == True:
            print(self._errorHandlerName + ": CRITICAL ERROR")
            print(self._errorHandlerName + ": Terminate execution")
            sys.exit()


        


    