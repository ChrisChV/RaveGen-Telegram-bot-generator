import Utils.commandManager as commandManager
import Utils.errorHandler as errorHandler
import Utils.logManager as logManager
import Utils.utils as utils
import Utils.sad as sad


gaeErrorHandler = errorHandler.ErrorHandler("GAE Manager")

def _verifyGAEInstallation():
    commandManager.runLsCommand(sad._GAE_PATH_, writeFile=sad._TEMP_LS_VERIFY_FILE_NAME)
    tempFile = open(sad._TEMP_LS_VERIFY_FILE_NAME, 'r')
    line = tempFile.readline()
    tempFile.close()
    commandManager.runRmCommand(sad._TEMP_LS_VERIFY_FILE_NAME)
    tokens = line.split(' ')
    tokens[0] = tokens[0].rstrip('n')
    if(tokens[0] != sad._GAE_PATH_):
        logManager.printVerbose("Google Cloud SDK is not installed")
        if(utils.hasSupport()):
            gaeErrorHandler.addError("You have to install Google Cloud SDK. Instructions: https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu?hl=es-419", sad._CRITICAL_ERROR_)
        else:
            gaeErrorHandler.addError("Google Cloud SDK is no installed", sad._CRITICAL_ERROR_)
    gaeErrorHandler.handle()

def _verifyGAELogin():
    commandManager.runGAEAuthListCommand(writeFile=sad._TEMP_GAE_AUTH_FILE_NAME)
    tempFile = open(sad._TEMP_GAE_AUTH_FILE_NAME, 'r')
    tempFile.readline()
    line = tempFile.readline()
    tokens = line.split(' ')
    tempFile.close()
    commandManager.runRmCommand(sad._TEMP_GAE_AUTH_FILE_NAME)
    return tokens[0] == sad._GAE_LOGIN_ACTIVE_

def _GAELogin():
    commandManager.runGAELogin()
    