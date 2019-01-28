import os
import sys
import Utils.sad as sad
import Utils.commandManager as commandManager
import configManager as configManager

def createInitProject(fillConfig=True, createBasicModules=False):
    commandManager.runMkdirCommand(sad._CONFIG_DIR_NAME_)
    commandManager.runMkdirCommand(sad._MODULES_DIR_)
    if(fillConfig == True):
        configManager.createInitConfig()
    if(createBasicModules == True):
        _createBasicModules()


def _createBasicModules():
    moduleFile = open(sad._MODULES_DIR_ + sad._DF_ + "start.py", 'w')
    moduleFile.write("def start(bot,update):\n")
    moduleFile.write("\tupdate.effective_message.reply_text(\"I'm a bot, please talk to me!\")")
    moduleFile.close()





