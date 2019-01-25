import generateBot
import RaveEngine.configManager as configManager
import Utils.commandManager as commandManager

TOKEN = "717635382:AAE9Qy-9Vd0wAsUAVnII9y9CLE-8E-s9EAA"
webhookURLHeroku = "https://rave-osioluyo.herokuapp.com/717635382:AAE9Qy-9Vd0wAsUAVnII9y9CLE-8E-s9EAA"
webhookURL = "https://bad72e47.ngrok.io"
generateBot._generateBot(TOKEN)

#commandManager.runLsCommand("config", writeFile="tt")

