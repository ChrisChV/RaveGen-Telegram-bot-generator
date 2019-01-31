import io
import Utils.sad as sad
import Utils.inputManager as inputManager
import Utils.commandManager as commandManager
import RaveEngine.configManager as configManager


def initConfiguration():
    config = configManager.getConfig()
    projectNameFlag = True
    initProjectFlag = True
    projectName = configManager.get(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_)
    if projectName != None and projectName != sad._INIT_CONFIG_PROJECT_NAME:
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
        token = configManager.get(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_)
        deployUrl = sad._HTTPS_ + projectName + sad._HEROKU_URL
        gitUrl = sad._HTTPS_ + sad._HEORKU_GIT_URL + projectName + sad._GIT_EXTENTION
        commandManager.runHerokuCreateCommand(projectName)
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_URL_OPTION, deployUrl)
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_WEBHOOK_PATH_OPTION, token)
        configManager.set(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_GIT_OPTION_, gitUrl)




    
        
    
        

