import io
import herokuManager
import Utils.sad as sad
import RaveEngine.configManager as configManager

def configure():
    config = configManager.getConfig()
    hosting = configManager.get(config, sad._CONFIG_RAVEGEN_SECTION_, sad._CONFIG_HOSTING_OPTION_)
    if(hosting == sad._DEPLOY_HEROKU_OPTION):
        herokuManager.initConfiguration()

#def deploy():
    