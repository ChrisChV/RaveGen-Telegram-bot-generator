import ConfigParser
import pytest
import RaveEngine.configManager as configManager
import RaveEngine.projectManager as projectManager
import Utils.commandManager as commandManager
import Utils.sad as sad
from flaky import flaky

@pytest.fixture(autouse=True)
def setup():
    projectManager.createInitProject()
    yield
    commandManager.runRmDirCommand(sad._CONFIG_DIR_NAME_)
    commandManager.runRmDirCommand(sad._LOG_DIR_NAME_)
    commandManager.runRmDirCommand(sad._MODULES_DIR_)

@flaky(3,1)
def test_getConfig():
    config = configManager.getConfig()
    assert isinstance(config, ConfigParser.RawConfigParser)

@flaky(3,1)
def test_verifyConfig():
    config = configManager.getConfig()
    configManager.verifyConfig(config)
