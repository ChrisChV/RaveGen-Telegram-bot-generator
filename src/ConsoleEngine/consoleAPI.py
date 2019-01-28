import consoleManager as consoleManager
import RaveEngine.projectManager as projectManager
import RaveEngine.botManager as botManager

def initProgram(argv):
    consoleManager.verifyArgs(argv)
    
    command = argv[1]

    if command == "help":
        consoleManager.printHelp()
    elif command == "init":
        options = consoleManager.getOptions(argv)
        if(len(options) == 0):
            projectManager.createInitProject()
        else:
            createBasicModules = False
            for option in options:
                if option == 'm':
                    createBasicModules = True
            projectManager.createInitProject(createBasicModules=createBasicModules)
    elif command == "create":
        options = consoleManager.getOptions(argv)
        testFlag = True
        for option in options:
            if option == 't':
                testFlag = True
            if option == 'd':
                testFlag = False
        botManager.generateBot(testFlag)


        
        


    







