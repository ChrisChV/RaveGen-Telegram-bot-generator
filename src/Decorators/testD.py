from text import *
from image import *
from ravegen import *

@RaveGen
@Text
def test(message):
    return message
    

@Image
def test2(message):
    return message
        