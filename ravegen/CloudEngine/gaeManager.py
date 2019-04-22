import RaveEngine.configManager as configManager
import Utils.commandManager as commandManager
import Utils.errorHandler as errorHandler
import Utils.logManager as logManager
import Utils.inputManager as inputManager
import Utils.utils as utils
import Utils.sad as sad


gaeErrorHandler = errorHandler.ErrorHandler("GAE Manager")

def initConfiguration():
    logManager.printVerbose("Verifying configuration...")
    logManager.printVerbose("Verifying Google Cloud installation...")
    _verifyGAEInstallation()
    logManager.printVerbose("Verifying Google Cloud login...")
    while True:
        if not _verifyGAELogin():
            logManager.printVerbose("Can't find google account")
            logManager.printVerbose("Google login...")
            _GAELogin()
        else:
            break
    config = configManager.getConfig()
    projectName = configManager.get(config, sad._DEPLOY_GAE_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_)
    logManager.printVerbose("Verifiying project name...")
    if projectName != None and projectName != sad._INIT_CONFIG_PROJECT_NAME:
        logManager.printVerbose("Project name found: " + projectName)
    else:
        projectName = _getNewGAEName(config)
    if _verifyGAEProject(projectName):
        logManager.printVerbose("The project has already been created in Google Cloud")
        token = configManager.get(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_)
        deployUrl = sad._HTTPS_ + projectName + sad._GAE_URL_
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_URL_OPTION, deployUrl)
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_WEBHOOK_PATH_OPTION, token)
    else:
        logManager.printVerbose("Project hasn't been created in Google Cloud")
        while True:
            _GAECreate(projectName)
            if _verifyGAEProject(projectName):                
                token = configManager.get(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_)
                deployUrl = sad._HTTPS_ + projectName + sad._GAE_URL_
                configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_URL_OPTION, deployUrl)
                configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_WEBHOOK_PATH_OPTION, token)
                break
            logManager.printVerbose("The project can't created in Google Cloud. Read the errors above and chose a new Google Cloud project name")
            projectName = _getNewGAEName(config)
    _GAEsetProject(projectName)
    logManager.printVerbose("All Configurations... OK")

def deploy():
    _createSkeleton()
    commandManager.runGAEDeploy()
    _deleteSkeleton()
    logManager.printVerbose("Deploying bot in Google Cloud...OK")

def deleteCloudApp():
    config = configManager.getConfig()
    projectName = configManager.get(config, sad._DEPLOY_GAE_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_)
    if projectName != None and projectName != sad._INIT_CONFIG_PROJECT_NAME:
        commandManager.runGAEDeleteProject(projectName)
        configManager.set(config, sad._DEPLOY_GAE_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_, "")
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_URL_OPTION, "")
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_WEBHOOK_PATH_OPTION, "")

def _createSkeleton():
    appYaml = open(sad._GAE_APP_YAML, 'w')
    runtimeFile = open(sad._CONFIG_RUNTIME_FILE_PATH_, 'r')
    runtime = runtimeFile.readline()
    runtimeFile.close()
    appYaml.write("runtime: " + runtime + "\n")
    appYaml.write("api_version: 1\n")
    appYaml.write("threadsafe: no\n\n")
    appYaml.write("handlers:\n")
    appYaml.write("- url: .*\n")
    appYaml.write("  script: bot/bot.py\n")
    appYaml.close()
    commandManager.runCpCommand(sad._CONFIG_REQ_FILE_PAHT_, sad._OUTPUT_BOT_DIR_ + sad._DF_ + sad._GAE_REQ_FILE_NAME)

def _deleteSkeleton():
    commandManager.runRmCommand(sad._GAE_APP_YAML)
    commandManager.runRmCommand(sad._OUTPUT_BOT_DIR_ + sad._DF_ + sad._GAE_REQ_FILE_NAME)

def _verifyGAEInstallation():
    commandManager.runLsCommand(sad._GAE_PATH_, writeFile=sad._TEMP_LS_VERIFY_FILE_NAME)
    tempFile = open(sad._TEMP_LS_VERIFY_FILE_NAME, 'r')
    line = tempFile.readline()    
    tempFile.close()
    commandManager.runRmCommand(sad._TEMP_LS_VERIFY_FILE_NAME)
    tokens = line.split(' ')
    tokens[0] = tokens[0].rstrip('\n')
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

def _verifyGAEProject(projectName):
    commandManager.runGAEListProjects(sad._TEMP_LS_VERIFY_FILE_NAME)
    tempFile = open(sad._TEMP_LS_VERIFY_FILE_NAME)
    flag = False
    for line in tempFile:
        tokens = line.split(' ')
        if tokens[0] == projectName:
            flag = True
            break
    tempFile.close()
    commandManager.runRmCommand(sad._TEMP_LS_VERIFY_FILE_NAME)
    return flag

def _GAELogin():
    commandManager.runGAELogin()

def _GAECreate(projectName):
    commandManager.runGAENewProject(projectName)

def _GAEsetProject(projectName):
    commandManager.runGAESetProject(projectName)

def _getNewGAEName(config):
    projectName = inputManager.getInput("Enter new GAE project name: ")
    configManager.set(config, sad._DEPLOY_GAE_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_, projectName)
    return projectName
