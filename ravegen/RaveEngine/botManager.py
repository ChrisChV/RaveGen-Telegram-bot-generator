from telegram.ext import Updater, CommandHandler, MessageHandler
import logging
import Utils.sad as sad
import Utils.commandManager as commandManager
import Utils.utils as utils
import Utils.logManager as logManager
import CloudEngine.cloudManager as cloudManager
import configManager as configManager

def generateBot(testFlag = True):
    config = configManager.getConfig()
    TOKEN = config.get(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_)
    if testFlag:
        _generateBot(TOKEN, testFlag=testFlag)
    else:
        webhookURL = configManager.get(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_URL_OPTION)
        port = configManager.get(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_PORT_OPRION)
        if port == sad._INIT_CONFIG_DEPLOY_PORT:
            port = None
        webhookPath = configManager.get(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_WEBHOOK_PATH_OPTION)
        if webhookPath == sad._INIT_CONFIG_WEBHOOK_PATH:
            webhookPath = None
        _generateBot(TOKEN, webhookURL, port, webhookPath, testFlag= testFlag)

def deployBot(withOptions = False, testFlag = True, generateFlag = True):
    if not withOptions:
        if utils.file_Or_Directory_Exists(sad._ACTUAL_PATH, sad._OUTPUT_BOT_DIR_):
            if utils.file_Or_Directory_Exists(sad._OUTPUT_BOT_DIR_, sad._OUTPUT_BOT_NAME_):
                generateFlag = False
                headers = _getHeaders()
                testFlag = headers[sad._HEADER_TOKEN_FLAG] == sad._STR_TRUE_
    if testFlag:
        if generateFlag:
            generateBot(testFlag)
        logManager.printVerbose("Running Test Bot")
        commandManager.runPythonCommand(sad.OUTPUT_BOT_PATH)
        commandManager.runRmCommand(sad._MODULES_DIR_ + sad._DF_ + sad._LINUX_ALL_TAG_ + sad._PYC_EXTENTION)
    else:
        cloudManager.configure()
        if generateFlag:
            generateBot(testFlag)
        cloudManager.deploy()

def changeState(testFlag):
    if testFlag:
        deployBot(withOptions=True)
    else:
        logManager.printVerbose("Changing to deploy mode...")
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger(__name__)
        config = configManager.getConfig()
        updater = Updater(config.get(sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_TOKEN_OPTION_))
        webhookURL = configManager.get(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_DEPLOY_URL_OPTION)
        webhookPath = configManager.get(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_WEBHOOK_PATH_OPTION)
        if(webhookURL[-1] == '/'):
            webhookURL = webhookURL[:-1]
        if(webhookPath[-1] == '/'):
            webhookPath = webhookPath[:-1]
        webhookURL += sad._DF_ + webhookPath
        logManager.printVerbose("Changing webhook to: " + webhookURL)
        updater.bot.setWebhook(webhookURL)
        logManager.printVerbose("DONE")

def _generateBot(TOKEN, webhookURL = None, port = None, webhookPath = None, testFlag = True):
    commandManager.runMkdirCommand(sad._OUTPUT_BOT_DIR_)
    commandManager.runLsCommand(sad._MODULES_DIR_, writeFile=sad._TEMP_LS_MODULES_FILE_NAME)
    modules = []
    tempLsFile = open(sad._TEMP_LS_MODULES_FILE_NAME, 'r')

    for line in tempLsFile:
        modules.append(line.rstrip('\n'))

    tempLsFile.close()
    
    

    modules = [module.split('.')[0] for module in modules if len(module.split('.')) == 2 and module.split('.')[1] == sad._MODULES_EXTENTION_]

    initFile = open(sad._MODULES_DIR_ + sad._DF_ + sad._INIT_PY, 'w')
    for module in modules:
        initFile.write("from " + module + " import *\n")
    initFile.close()

    commandManager.runRmCommand(sad._TEMP_LS_MODULES_FILE_NAME)
    outputBotFile = open(sad.OUTPUT_BOT_PATH, 'w')
    _generateHeaders(outputBotFile, testFlag)
    outputBotFile.write("from telegram.ext import Updater, CommandHandler, MessageHandler, Filters \n")
    outputBotFile.write("import logging \n")
    outputBotFile.write("import os \n")
    outputBotFile.write("import sys \n")
    outputBotFile.write("import ravegen.Decorators.functionManager as functionManager \n")
    outputBotFile.write("sys.path.insert(0, '.')\n")
    outputBotFile.write("import modules\n")
    outputBotFile.write('\n')
    outputBotFile.write("if __name__ == \"__main__\":\n")
    outputBotFile.write("\tTOKEN = \"" + TOKEN + "\"\n")
    if(webhookURL != None):
        if port is None:
            outputBotFile.write("\tPORT = os.environ.get('PORT')\n")
        else:
            outputBotFile.write("\tPORT = " + str(port) + "\n")


    outputBotFile.write("\tlogging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)\n")
    outputBotFile.write("\tlogger = logging.getLogger(__name__)\n")
    outputBotFile.write("\tupdater = Updater(TOKEN)\n")
    outputBotFile.write("\tdispatcher = updater.dispatcher\n")

    #_writeModule(outputBotFile, modules)

    outputBotFile.write("\tfunctionManager.functionManager.generateHandlers(dispatcher)\n")

    if(webhookURL != None):
        if webhookPath is None:
            outputBotFile.write("\tupdater.start_webhook(listen=\"0.0.0.0\", port=int(PORT), url_path=TOKEN)\n")
            webhookURL += TOKEN
        else:
            outputBotFile.write("\tupdater.start_webhook(listen=\"0.0.0.0\", port=int(PORT), url_path=\"" + webhookPath + "\")\n")
            webhookURL += webhookPath
        outputBotFile.write("\tupdater.bot.setWebhook(\"" + webhookURL + "\")\n")
    else:
        outputBotFile.write("\tupdater.bot.deleteWebhook()\n")
        outputBotFile.write("\tupdater.start_polling()\n")


    outputBotFile.write("\tupdater.idle()\n")
    outputBotFile.close()

def _writeModule(outputBotFile, modules):
    for module in modules:
        createHandler = "\t" + module + "_handler = CommandHandler('" + module + "'," + module + ")\n"
        addHandler = "\tdispatcher.add_handler(" + module + "_handler)\n"
        tempFile = open(sad._MODULES_DIR_ + sad._DF_ + module + "." + sad._MODULES_EXTENTION_)
        while True:
            flag, line = _arroba_gen_next_line(tempFile)
            if(flag == 0):
                continue
            if(flag == -1):
                break
            if(line == "command"):
                _ , option = _arroba_gen_next_line(tempFile)
                if option is None:
                    break
                if(option == "args"):
                    createHandler = "\t" + module + "_handler = CommandHandler('" + module + "'," + module + ", pass_args=True)\n"
            elif(line == "text"):
                createHandler = "\t" + module + "_handler = MessageHandler(Filters.text," + module + ")\n"
            elif(line == "error"):
                createHandler = "\t" + module + "_error_handler = " + module + "\n"
                addHandler = "\tdispatcher.add_error_handler(" + module + "_error_handler)\n"
        tempFile.close()
        outputBotFile.write(createHandler)
        outputBotFile.write(addHandler)




def _arroba_gen_next_line(tempFile):
    line = tempFile.readline()
    if line:
        line = line.strip(' ')
        line = line.rstrip('\n')
        if(line[0] == '#'):
            if(line[1] != '@'):
                return 0, None
        else:
            return -1, None
        line = line[2:]
        line = line.lower()
        return 1, line
    else:
        return -1, None

def _generateHeaders(outputBotFile, testFlag):
    outputBotFile.write("#HEADERS\n")
    outputBotFile.write("#" + sad._HEADER_TOKEN_FLAG + " " + str(testFlag) + "\n")

def _getHeaders():
    outputBotFile = open(sad.OUTPUT_BOT_PATH, 'r')
    count = 0
    headers = {}
    for line in outputBotFile:
        if(count == 0):
            count = 1
            continue
        if(line[0] != '#'):
            break
        line = line[1:]
        tokens = line.split(" ")
        headers[tokens[0]] = tokens[1].rstrip('\n')
    outputBotFile.close()
    return headers
