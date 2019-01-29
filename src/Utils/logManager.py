import os
import io
import datetime
import ConfigParser
import sad as sad


def printVerbose(_string):
    if _verbose():
        print(_string)

def printLog(_string):
    if _log():
        logFile = open(sad._LOG_FILE_PATH_, 'a+')
        logFile.write(str(datetime.datetime.now()) + ": " + _string + "\n")
        logFile.close()

def print_all(_string):
    printVerbose(_string)
    printLog(_string)

def _verbose():
    configFile = open(sad._CONFIG_FILE_PATH, 'r')
    configStream = configFile.read()
    config = ConfigParser.RawConfigParser(allow_no_value=False)
    config.readfp(io.BytesIO(configStream))
    configFile.close()
    if not config.has_section(sad._CONFIG_RAVEGEN_SECTION_):
        return True
    if not config.has_option(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_VERBOSE_OPTION_):
        return True
    
    return config.getboolean(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_VERBOSE_OPTION_)

def _log():
    configFile = open(sad._CONFIG_FILE_PATH, 'r')
    configStream = configFile.read()
    config = ConfigParser.RawConfigParser(allow_no_value=False)
    config.readfp(io.BytesIO(configStream))
    configFile.close()
    if not config.has_section(sad._CONFIG_RAVEGEN_SECTION_):
        return True
    if not config.has_option(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_LOG_OPTION_):
        return True
    
    return config.getboolean(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_LOG_OPTION_)
    

