import Utils.sad as sad
import Utils.commandManager as commandManager
import configManager as configManager

def createInitProject(fillConfig=True, createBasicModules=False, TOKEN = None):
    commandManager.runMkdirCommand(sad._CONFIG_DIR_NAME_)
    commandManager.runMkdirCommand(sad._MODULES_DIR_)
    commandManager.runMkdirCommand(sad._LOG_DIR_NAME_)
    commandManager.runTouchCommand(sad._LOG_FILE_PATH_)
    reqFile = open(sad._CONFIG_REQ_FILE_PAHT_, 'w')
    reqFile.write("ravegen\n")
    reqFile.close()
    runtimeFile = open(sad._CONFIG_RUNTIME_FILE_PATH_, 'w')
    runtimeFile.write("python-2.7.15\n")
    runtimeFile.close()
    if fillConfig:
        configManager.createInitConfig()
    if createBasicModules:
        _createBasicModules()
    if(TOKEN != None):
        config = configManager.getConfig()
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_, TOKEN)


def _createBasicModules():
    moduleFile = open(sad._MODULES_DIR_ + sad._DF_ + "start.py", 'w')
    moduleFile.write("from ravegen import *\n\n")
    moduleFile.write("@RaveGen\n")
    moduleFile.write("@Command(description='Start command')\n")
    moduleFile.write("def start(message):\n")
    moduleFile.write("\treturn 'Hello, tell me something'\n")
    moduleFile.close()
    moduleFile = open(sad._MODULES_DIR_ + sad._DF_ + "echo.py", 'w')
    moduleFile.write("from ravegen import *\n\n")
    moduleFile.write("@RaveGen\n")
    moduleFile.write("@Text(description='Reply the same message')\n")
    moduleFile.write("def echo(message):\n")
    moduleFile.write("\treturn message\n")
    moduleFile.close()
    moduleFile = open(sad._MODULES_DIR_ + sad._DF_ + "caps.py", 'w')
    moduleFile.write("from ravegen import *\n\n")
    moduleFile.write("@RaveGen\n")
    moduleFile.write("@Command(description='To Upper')\n")
    moduleFile.write("def caps(message):\n")
    moduleFile.write("\tif message == '':\n")
    moduleFile.write("\t\treturn 'The argument is missing'\n")
    moduleFile.write("\treturn message.upper()\n")
    moduleFile.close()
    moduleFile = open(sad._MODULES_DIR_ + sad._DF_ + "error.py", 'w')
    moduleFile.write("from ravegen import *\n\n")
    moduleFile.write("@RaveGen\n")
    moduleFile.write("@Error\n")
    moduleFile.write("def error(message):\n")
    moduleFile.write("\treturn 'ERROR: ' + message\n")
    moduleFile.close()
