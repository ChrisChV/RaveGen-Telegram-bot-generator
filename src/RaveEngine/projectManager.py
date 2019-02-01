import os
import sys
import Utils.sad as sad
import Utils.commandManager as commandManager
import configManager as configManager

def createInitProject(fillConfig=True, createBasicModules=False, TOKEN = None):
    commandManager.runMkdirCommand(sad._CONFIG_DIR_NAME_)
    commandManager.runMkdirCommand(sad._MODULES_DIR_)
    commandManager.runMkdirCommand(sad._LOG_DIR_NAME_)
    reqFile = open(sad._CONFIG_REQ_FILE_PAHT_, 'w')
    reqFile.write("python-telegram-bot\n")
    reqFile.close()
    if(fillConfig == True):
        configManager.createInitConfig()
    if(createBasicModules == True):
        _createBasicModules()
    if(TOKEN != None):
        config = configManager.getConfig()
        configManager.set(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_, TOKEN)


def _createBasicModules():
    moduleFile = open(sad._MODULES_DIR_ + sad._DF_ + "start.py", 'w')
    moduleFile.write("def start(bot,update):\n")
    moduleFile.write("\tupdate.effective_message.reply_text(\"I'm a bot, please talk to me!\")")
    moduleFile.close()





