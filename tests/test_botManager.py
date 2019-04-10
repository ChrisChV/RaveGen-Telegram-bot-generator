import pytest
import os
import RaveEngine.projectManager as projectManager
import RaveEngine.botManager as botManager
import Utils.commandManager as commandManager
from flaky import flaky
import Utils.sad as sad

@pytest.fixture(autouse=True)
def setup():
    projectManager.createInitProject()
    yield
    commandManager.runRmDirCommand(sad._CONFIG_DIR_NAME_)
    commandManager.runRmDirCommand(sad._LOG_DIR_NAME_)
    commandManager.runRmDirCommand(sad._MODULES_DIR_)
    commandManager.runRmDirCommand(sad._OUTPUT_BOT_DIR_)

def data_generateHeaders():
    return [sad._HEADER_TOKEN_FLAG]

@flaky(3,1)
@pytest.mark.parametrize('testFlag', [False, True])
def test_generateBot(testFlag):
    botManager.generateBot(testFlag=testFlag)
    assert os.path.exists(sad._OUTPUT_BOT_DIR_)
    assert os.path.exists(sad.OUTPUT_BOT_PATH)
    headers = botManager._getHeaders()
    if testFlag:
        assert headers[sad._HEADER_TOKEN_FLAG] == sad._STR_TRUE_
    else:
        assert headers[sad._HEADER_TOKEN_FLAG] == sad._STR_FALSE_

@flaky(3,1)
@pytest.mark.parametrize('header', data_generateHeaders())
def test_generateHeaders(header):
    botManager.generateBot()
    headers = botManager._getHeaders()
    assert header in headers
