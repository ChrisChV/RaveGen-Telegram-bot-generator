import os
import datetime
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