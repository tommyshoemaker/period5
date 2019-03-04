import cocos
from cocos.actions import *

class HelloWorld(cocos.layer.Layer):

    #Always call super in the constructor:
    def __init__(self):
        super(HelloWorld, self).__init__()


        #To display the text, we will create a Label.
        #Keyword arguments are used to set the font, position and alignment of the label:
        label = cocos.text.Label('Hello World', font_name='Times New Roman', font_size=32,anchor_x='center', anchor_y='center')

        #The label position will be the center of the screen:
        label.position = 320, 400

        #Adds label to the HelloWorld layer
        #add is a method inherited from Cocos Node
        self.add(label) 

        #Create a Sprite and set its image:
        sprite = cocos.sprite.Sprite('car.png')

        #place the sprite in the center of the screen:
        #position is a property inherited from Coco Node
        sprite.position = 320,240   #Change these values and run

        #Sets the scale of sprite to 2 (twice as big as original)
        sprite.scale = 1
        
        #add the sprite to the layer
        #z is its position, if ommited it's 0.  The greater the # the closer to top
        self.add( sprite, z=1 )

        #Some actions inherited from Cocos Node:
        #ScaleBy
        sprite.do(ScaleBy(2,duration=1))
        #RotateBy
        label.do(RotateBy(-360, duration =3))
        #MoveBy
        sprite.do(MoveBy((200,100), duration=2))

        #ScaleTo
        sprite.do(ScaleTo(1,duration=1))
        #RotateTo
        sprite.do(RotateTo(60, duration =3))
        #MoveTo
        sprite.do(MoveTo((50,100), duration=2))

        #Experiment with some more actions below
        
       


        



