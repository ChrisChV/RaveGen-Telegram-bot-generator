import os
import sys
import datetime
import platform
import signal
import commandManager as commandManager
import sad as sad

def file_Or_Directory_Exists(parent, file_directory):
    commandManager.runLsCommand(parent,writeFile=sad._TEMP_LS_VERIFY_FILE_NAME)
    verifyFile = open(sad._TEMP_LS_VERIFY_FILE_NAME, 'r')
    files = []
    for line in verifyFile:
        files.append(line.rstrip('\n'))
    verifyFile.close()
    commandManager.runRmCommand(sad._TEMP_LS_VERIFY_FILE_NAME)
    if file_directory in files:
        return True
    else:
        return False
        
def getTime():
    return str(datetime.datetime.now())

def getDist():
    return platform.dist()[0].lower()

def hasSupport():
    dist = getDist()
    if dist in sad._SUPPORT_DIST_:
        return True
    return False

def sigintHandler(sig, frame):
    sys.exit()


def getInstalationPath():
    commandManager.runPipShowRavegen(sad._TEMP_PYTHON_PATH_FILE_NAME)
    tempFile = open(sad._TEMP_PYTHON_PATH_FILE_NAME, 'r')
    res = None
    for line in tempFile:
        tokens = line.split(" ")
        tokens[-1] = tokens[-1].rstrip('\n')
        if(tokens[0] == "Location:"):
            res = tokens[1]
    tempFile.close()
    commandManager.runRmCommand(sad._TEMP_PYTHON_PATH_FILE_NAME)
    return res




