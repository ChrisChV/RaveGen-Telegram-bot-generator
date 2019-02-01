import io
import Utils.sad as sad
import Utils.inputManager as inputManager
import Utils.commandManager as commandManager
import Utils.logManager as logManager
import RaveEngine.configManager as configManager


def initConfiguration():
    logManager.printVerbose("Verifying configuration...")
    config = configManager.getConfig()
    projectNameFlag = True
    initProjectFlag = True
    projectName = configManager.get(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_)
    logManager.printVerbose("Verifiying project name...")
    if projectName != None and projectName != sad._INIT_CONFIG_PROJECT_NAME:
        logManager.printVerbose("Project name found: " + projectName)
        projectNameFlag = False
    logManager.printVerbose("Verifiying project in heroku...")
    if _verifyProject(projectName) == True:
        logManager.printVerbose("The project has already been created in heroku")
        initProjectFlag = False
    #TODO verify initProjectFlag
    
    _initConfiguration(projectNameFlag, initProjectFlag)
    logManager.printVerbose("All Configuration... OK")

def deleteCloudApp():
    config = configManager.getConfig()
    projectName = configManager.get(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_)
    if projectName != None and projectName != sad._INIT_CONFIG_PROJECT_NAME:
        commandManager.runHerokuDestroyCommand(projectName)
        configManager.set(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_, "")
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_URL_OPTION, "")
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_WEBHOOK_PATH_OPTION, "")
        configManager.set(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_GIT_OPTION_, "")

def _initConfiguration(projectNameFlag = True, initProjectFlag = True):
    config = configManager.getConfig()
    if projectNameFlag == True:
        logManager.printVerbose("Project name dosen't found")
        _getNewHerokuName(config)
        initProjectFlag = True
    if initProjectFlag == True:
        logManager.printVerbose("Project hasen't been craeted in heroku")
        erroFlag = False
        while True:
            if erroFlag == True:
                logManager.printVerbose("The project can't created in heroku. Read the erros above and chose a new heroku project name")
                _getNewHerokuName(config)
            projectName = configManager.get(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_)
            token = configManager.get(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_)
            deployUrl = sad._HTTPS_ + projectName + sad._HEROKU_URL
            gitUrl = sad._HTTPS_ + sad._HEORKU_GIT_URL + projectName + sad._GIT_EXTENTION
            commandManager.runHerokuCreateCommand(projectName)
            if _verifyProject(projectName) == True:
                configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_URL_OPTION, deployUrl)
                configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_WEBHOOK_PATH_OPTION, token)
                configManager.set(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_GIT_OPTION_, gitUrl)
                break
            else:
                erroFlag = True

        

def _verifyProject(projectName):
    if projectName == None:
        projectName = "None"
    commandManager.runHerokuInfoCommand(projectName, sad._TEMP_HEROKU_INFO_FILE_NAME)
    tempFile = open(sad._TEMP_HEROKU_INFO_FILE_NAME, 'r')
    count = 0
    line = tempFile.readline()
    tokens = line.split(' ')
    tempFile.close()
    commandManager.runRmCommand(sad._TEMP_HEROKU_INFO_FILE_NAME)
    if(tokens[0] == '==='):
        return True
    return False

def _getNewHerokuName(config):    
    projectName = inputManager.getInput("Enter new Heroku Project Name: ")
    configManager.set(config, sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_, projectName)
        
    
    




    
        
    
        

