import io
import Utils.sad as sad
import Utils.inputManager as inputManager
import Utils.commandManager as commandManager
import RaveEngine.configManager as configManager


def initConfiguration():
    config = configManager.getConfig()
    projectNameFlag = True
    initProjectFlag = True
    if configManager.get(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_) != None:
        projectNameFlag = False
    #TODO verify initProjectFlag
    _initConfiguration(projectNameFlag, initProjectFlag)

def _initConfiguration(projectNameFlag = True, initProjectFlag = True):
    config = configManager.getConfig()
    if projectNameFlag == True:
        projectName = inputManager.getInput("Heroku Project Name: ")
        configManager.set(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_, projectName)
        initProjectFlag = True
    if initProjectFlag == True:
        projectName = configManager.get(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_)
        commandManager.runHerokuCreateCommand(projectName)




    
        
    
        

