import os
import sad

def runMkdirCommand(directory, *args):
    _executeCommand(sad._LINUX_MKDIR_COMMAND_, directory, args)

def runRmCommand(file, *args):
    _executeCommand(sad._LINUX_RM_COMMAND_, file, args)

def runRmDirCommand(directory, *args):
    _executeCommand(sad._LINUX_RM_COMMAND_DIR, directory, args)

def runLsCommand(directory):
    _executeCommand(sad._LINUX_LS_COMMAND_, directory, [])

def _executeCommand(command, fistrArg, args, writeFile = None):
    command = command + fistrArg
    for arg in args:
        command += " " + arg
    if(writeFile != None):
        command += sad._LINUX_WRITE_COMMAND_ + writeFile
    os.system(command)
