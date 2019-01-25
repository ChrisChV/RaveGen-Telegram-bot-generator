import ConfigParser
import io
import sad
from errorHandler import *

configErrorHandler = ErrorHandler()


def getConfig():
    configFile = open(sad._CONFIG_FILE_PATH, 'r')
    configStream = configFile.read()
    config = ConfigParser.RawConfigParser(allow_no_value=False)
    config.readfp(io.BytesIO(configStream))
    configFile.close()
    verifyConfig(config)



def verifyConfig(config):
    _option_exists_and_is_NotEmpty(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_)
    if _option_exists_and_is_NotEmpty(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_HOSTING_OPTION_):
        hosting = config.get(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_HOSTING_OPTION_)
        _option_exists_and_is_NotEmpty(config, hosting, sad._CONFIG_PROJECT_NAME_OPTION_)


    configErrorHandler.handle()


def _option_exists_and_is_NotEmpty(config, section, option):
    if _section_exists(config, section) == False:
        return False
    error = None
    if not config.has_option(section, option):
        error = "Error in ravegen.conf: " + option + " option didn'f found"
    elif config.get(section,option) == '':
        error = "Error in ravegen.conf: " + option + " option can't be empty"

    if(error == None):
        return True
    else:
        configErrorHandler.addError(error, sad._CRITICAL_ERROR_)
        return False


def _section_exists(config, section):
    error = None
    if not config.has_section(section):
        error = "Error in raven.conf: [" + section + "] section didn't found"    

    if(error == None):
        return True
    else:
        configErrorHandler.addError(error, sad._CRITICAL_ERROR_)
        return False

getConfig()