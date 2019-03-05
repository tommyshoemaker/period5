import cocos
from cocos.actions import *
from cocosKeyInputClasses import *


if __name__ == "__main__":
    director.init(resizable=True)
    # Run a scene with our event displayers:
    myLayer = KeyDisplay()
    mainScene = cocos.scene.Scene(myLayer)
    director.run(mainScene)

