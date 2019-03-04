import cocos
from cocos.actions import *
from cocosCarClassesV3 import *


if __name__ == '__main__':
    #After defining the HelloWorld class, we need to initialize and create a window. To do this, we initialize the Director:
    cocos.director.director.init(width=1000, height=800, resizable=True)

    #Then we create a HelloWorld instance:
    carLayer = GameLayer()   
    #Then we create a Scene that contains the HelloWorld layer as a child:
    #To add another layer to the scene you would just put a comma after
    #hello_layer and list the new layer
    main_scene = cocos.scene.Scene (carLayer)


    #And finally we run the scene:
    cocos.director.director.run(main_scene)



   
