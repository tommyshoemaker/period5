import cocos
import cocos.collision_model as cm
import cocos.euclid as eu

from collections import defaultdict
from pyglet.window import key

class Actor(cocos.sprite.Sprite):
    def __init__(self, x, y, color):
        super(Actor, self).__init__('ball.png', color=color) #Sprite uses this image and color can be defined later
                                                            #try saving a different png and using it here instead.
        self.position = pos = eu.Vector2(x, y) #Sets the x,y position
        self.cshape = cm.CircleShape(pos, self.width/2)

class MainLayer(cocos.layer.Layer):#inherits from cocos.layer.Layer
    is_event_handler = True

    def __init__(self):
        super(MainLayer, self).__init__() #New python way of initializing class
        self.player = Actor(320, 240, (0, 255, 255))#Sprite(x,y, (R,G,B)). Experiment changing these values
        self.add(self.player)  #Adds a child 
        
        self.speed = 100.0
        self.pressed = defaultdict(int)  
        self.schedule(self.update)

    def on_key_press(self, k, m):
        self.pressed[k] = 1

    def on_key_release(self, k, m):
        self.pressed[k] = 0
        
    '''This is method to make sprite move and respond to user input'''
    def update(self, dt):

        x = self.pressed[key.RIGHT] - self.pressed[key.LEFT]
        y = self.pressed[key.UP] - self.pressed[key.DOWN]
        if x != 0 or y != 0:
            pos = self.player.position
            new_x = pos[0] + self.speed * x * dt
            new_y = pos[1] + self.speed * y * dt
            self.player.position = (new_x, new_y)
            self.player.cshape.center = self.player.position
            
'''This is the main method which we usually have in a separate file.'''
if __name__ == '__main__':
    cocos.director.director.init(caption='Hello, Cocos')
    layer = MainLayer()
    scene = cocos.scene.Scene(layer)
    cocos.director.director.run(scene)
