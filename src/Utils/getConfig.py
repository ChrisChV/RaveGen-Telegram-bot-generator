import ConfigParser
import io
import sad

def getConfig():
    configFile = open(sad._CONFIG_FILE_PATH, 'r')
    configStream = configFile.read()
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(configStream))
    configFile.close()
    return config

def verifyConfig(config):
    
    if not config.has_option(_CONFIG_RAVEGEN_SECTION_, _CONFIG_TOKEN_OPTION_):


    
