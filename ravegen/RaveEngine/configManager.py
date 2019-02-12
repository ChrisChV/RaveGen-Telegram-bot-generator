import ConfigParser
import io
import Utils.sad as sad
import Utils.utils as utils
import Utils.errorHandler as errorHandler

configErrorHandler = errorHandler.ErrorHandler("Config Manager")

def getConfig():
    if utils.file_Or_Directory_Exists(sad._ACTUAL_PATH, sad._CONFIG_DIR_NAME_) == False:
        configErrorHandler.addError("The project haen't been initialized correctly. Run -> ravegen init", sad._CRITICAL_ERROR_)
        
    elif utils.file_Or_Directory_Exists(sad._CONFIG_DIR_NAME_, sad._CONFIG_FILE_NAME_) == False:
        configErrorHandler.addError("The project haen't been initialized correctly. Run -> ravegen init", sad._CRITICAL_ERROR_)
    
    configErrorHandler.handle()
        
    
    configFile = open(sad._CONFIG_FILE_PATH, 'r')
    configStream = configFile.read()
    config = ConfigParser.RawConfigParser(allow_no_value=False)
    config.readfp(io.BytesIO(configStream))
    configFile.close()
    verifyConfig(config)
    return config


def verifyConfig(config):
    _option_exists_and_is_NotEmpty(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_)
    if _option_exists_and_is_NotEmpty(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_HOSTING_OPTION_):
        hosting = config.get(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_HOSTING_OPTION_)
        _verify_hosting_option(hosting)


    configErrorHandler.handle()


def createInitConfig():
    config = ConfigParser.ConfigParser()
    config.add_section(sad._CONFIG_RAVEGEN_SECTION_)
    config.set(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_HOSTING_OPTION_, sad._DEPLOY_HEROKU_OPTION)
    config.set(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_, sad._INIT_CONFIG_TOKEN_)
    config.set(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_URL_OPTION, sad._INIT_CONFIG_DEPLOY_URL)
    config.set(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_PORT_OPRION, sad._INIT_CONFIG_DEPLOY_PORT)
    config.set(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_WEBHOOK_PATH_OPTION, sad._INIT_CONFIG_WEBHOOK_PATH)
    config.set(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_VERBOSE_OPTION_, sad._INIT_CONFIG_VERBOSE)
    config.set(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_LOG_OPTION_, sad._INIT_CONFIG_LOG)
    config.add_section(sad._DEPLOY_HEROKU_OPTION)
    config.set(sad._DEPLOY_HEROKU_OPTION, sad._CONFIG_PROJECT_NAME_OPTION_, sad._INIT_CONFIG_PROJECT_NAME)
    _save_config(config)
    
def get(config, section, option):
    if _option_exists_and_is_NotEmpty(config, section, option, errorFlag=False) == False:
        return None
    return config.get(section, option)

def getboolean(config, section, option):
    if _option_exists_and_is_NotEmpty(config, section, option, errorFlag=False) == False:
        return None
    return config.getboolean(section, option)

def set(config, section, option, val):
    if _section_exists(config, section, errorFlag=False) == False:
        config.add_section(section)
    config.set(section, option, val)
    _save_config(config)

def setSection(config, section):
    if _section_exists(config, section, errorFlag=False) == True:
        return None
    config.add_section(section)
    _save_config(config)




def _verify_hosting_option(hosting):
    flag = False
    if hosting == sad._DEPLOY_HEROKU_OPTION:
        flag = True
    
    if(flag == False):
        error = "Error in ravegen.conf: " + hosting + " hosting doesn't support"
        configErrorHandler.addError(error, sad._CRITICAL_ERROR_)


def _option_exists_and_is_NotEmpty(config, section, option, errorFlag = True):
    if _section_exists(config, section, errorFlag=errorFlag) == False:
        return False
    error = None
    if not config.has_option(section, option):
        error = "Error in ravegen.conf: " + option + " option didn'f found"
    elif config.get(section,option) == '':
        error = "Error in ravegen.conf: " + option + " option can't be empty"

    if(error == None):
        return True
    else:
        if(errorFlag == True):
            configErrorHandler.addError(error, sad._CRITICAL_ERROR_)
        return False


def _section_exists(config, section, errorFlag = True):
    error = None
    if not config.has_section(section):
        error = "Error in raven.conf: [" + section + "] section didn't found"    

    if(error == None):
        return True
    else:
        if(errorFlag == True):
            configErrorHandler.addError(error, sad._CRITICAL_ERROR_)
        return False



def _save_config(config):
    configFile = open(sad._CONFIG_FILE_PATH, 'w')
    config.write(configFile)
    configFile.close()