from text import *
from image import *
from ravegen import *

@RaveGen
@Text
def test(message):
    print("TEXT")
    return message


@RaveGen
@Image
def test2(message):
    print("IMAGE")
    return message
        