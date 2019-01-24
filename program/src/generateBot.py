import os
import sad

def generateBot(TOKEN, webhookURL = None, port = None, webhookPath = None):
    rmCommand = sad._LINUX_RM_COMMAND_DIR + sad._OUTPUT_BOT_DIR_
    os.system(rmCommand)
    mkdirCommand = sad._LINUX_MKDIR_COMMAND_ +  sad._OUTPUT_BOT_DIR_
    os.system(mkdirCommand)
    lsCommand = sad._LINUX_LS_COMMAND_ + sad._MODULES_DIR_ + sad._LINUX_WRITE_COMMAND_ + sad._TEMP_LS_MODULES_FILE_NAME
    os.system(lsCommand)
    modules = []
    tempLsFile = open(sad._TEMP_LS_MODULES_FILE_NAME, 'r')

    for line in tempLsFile:
        modules.append(line.rstrip('\n'))

    tempLsFile.close()

    modules = [module.split('.')[0] for module in modules if module.split('.')[1] == sad._MODULES_EXTENTION_]
    rmCommand = sad._LINUX_RM_COMMAND_ + sad._TEMP_LS_MODULES_FILE_NAME
    os.system(rmCommand)
    outputBotFile = open(sad.OUTPUT_BOT_PATH, 'w')
    outputBotFile.write("from telegram.ext import Updater, CommandHandler, MessageHandler, Filters \n")
    outputBotFile.write("import logging \n")
    outputBotFile.write("import os \n")
    outputBotFile.write("import sys \n")
    outputBotFile.write("sys.path.insert(0, '../" + sad._MODULES_DIR_ + "')\n")
    for module in modules:
        outputBotFile.write("from " + module + " import *\n")
    outputBotFile.write('\n')
    outputBotFile.write("if __name__ == \"__main__\":\n")
    outputBotFile.write("\tTOKEN = \"" + TOKEN + "\"\n")
    if(webhookURL != None):
        if(port == None):
            outputBotFile.write("\tPORT = os.environ.get('PORT')\n")    
        else:
            outputBotFile.write("\tPORT = " + str(port) + "\n")

    
    outputBotFile.write("\tlogging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)\n")
    outputBotFile.write("\tlogger = logging.getLogger(__name__)\n")
    outputBotFile.write("\tupdater = Updater(TOKEN)\n")
    outputBotFile.write("\tdispatcher = updater.dispatcher\n")
    for module in modules:
        outputBotFile.write("\t" + module + "_handler = CommandHandler('" + module + "'," + module + ")\n")
        outputBotFile.write("\tdispatcher.add_handler(" + module + "_handler)\n")
    
    if(webhookURL != None):
        if(webhookPath == None):
            outputBotFile.write("\tupdater.start_webhook(listen=\"0.0.0.0\", port=int(PORT), url_path=TOKEN)\n")
        else:
            outputBotFile.write("\tupdater.start_webhook(listen=\"0.0.0.0\", port=int(PORT), url_path=\"" + webhookPath + "\")\n")
        outputBotFile.write("\tupdater.bot.setWebhook(\"" + webhookURL + "\")\n")
    else:
        outputBotFile.write("\tupdater.bot.deleteWebhook()\n")
        outputBotFile.write("\tupdater.start_polling()\n")


    outputBotFile.write("\tupdater.idle()\n")
    outputBotFile.close()