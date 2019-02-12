import consoleManager
import Utils.sad as sad


def generateAutoCompletition():
    outFile = open(sad._INSTALL_PATH + sad._DF_ + sad._CONSOLE_ENGINE_AUTOCOMPLETITION_FILE_NAME, 'w')
    commands, commandsInfo = consoleManager.getConsoleCommands()
    outFile.write("#/usr/bin/env bash\n")
    outFile.write("Commands=\"")
    for command in commands:
        outFile.write(command + " ")
    outFile.write("\"\n")
    outFile.write("_completions()\n")
    outFile.write("{\n")
    outFile.write("if [ \"${#COMP_WORDS[@]}\" == \"2\" ]; then\n")
    outFile.write("COMPREPLY=($(compgen -W \"$Commands\" \"\\\"${COMP_WORDS[1]}\\\"\"))\n")
    outFile.write("fi\n")
    outFile.write("if [ \"${#COMP_WORDS[@]}\" != \"2\" ]; then\n")
    for command, info in commandsInfo.iteritems():
        if(len(info["Options"]) != 0):
            outFile.write("if [ \"${COMP_WORDS[1]}\" == \"" + command + "\" ]; then\n")
            options = ""
            for option, info in info["Options"].iteritems():
                options += "-" + option + " "
            outFile.write("COMPREPLY=($(compgen -W \"" + options + "\" \"\\\"${COMP_WORDS[-1]}\\\"\"))\n")
            outFile.write("fi\n")
    outFile.write("fi\n")
    outFile.write("}\n\n")
    outFile.write("complete -F _completions ravegen")
    outFile.close()