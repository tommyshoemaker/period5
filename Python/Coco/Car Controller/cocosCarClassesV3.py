import cocos
import pyglet
from cocos.actions import *
from collections import defaultdict
import math

class Actor(cocos.sprite.Sprite):
    def __init__(self,image,x,y):
        super(Actor, self).__init__(image)
        self.position = x,y
        self.turnKey = None
        self.moveKey= None

    def isTouching(self,sprite):
        x1=self.x - self.width/2
        x2=self.x + self.width/2
        y1=self.y - self.height/2
        y2=self.y +self.height/2

        sx1=sprite.x - sprite.width/2
        sx2=sprite.x + sprite.width/2
        sy1=sprite.y - sprite.height/2
        sy2=sprite.y + sprite.height/2

        #x coords of actor are within x coords of target
        if x1<=sx2 and x2>=sx1 and y1<=sy2 and y2>=sy1:
            return True
        
    def turn(self):
        if (self.turnKey=='RIGHT'):
                self.do(RotateBy(5,duration=.08))
        elif (self.turnKey=='LEFT'):
                self.do(RotateBy(-5,duration=.08))

    def moveForward(self):
        #I adusted the angle because the unit circled is flipped on cocos2d
        #At the same time I converted to radians since python assumes it is given rads in sin, cos
        adjustedRotation = math.radians(-(self.rotation - 360))
        self.do(MoveBy((math.cos(adjustedRotation),math.sin(adjustedRotation)),duration=.00008))

    def moveBackward(self):
        #I adusted the angle because the unit circled is flipped on cocos2d
        #At the same time I converted to radians since python assumes it is given rads in sin, cos
        #Additionally note the - in both MoveBy coord since we want to move backwards
        adjustedRotation = math.radians(-(self.rotation - 360))
        self.do(MoveBy((-(math.cos(adjustedRotation)),-(math.sin(adjustedRotation))),duration=.008))

    def crash(self):
        for i in range (0,2):
            self.moveBackward()
        self.do(RotateBy(720,duration=1))
                   
    def gas(self):
        if (self.moveKey=='UP'):
            self.moveForward()
        if (self.moveKey=='DOWN'):
            self.moveBackward()       

class GameLayer(cocos.layer.Layer):
    is_event_handler = True  #: enable mouse and keyboard events
    #Always call super in the constructor:
    def __init__(self):
        super(GameLayer, self).__init__()

        #schedule method keeps refreshing the moveCar method below
        self.schedule(self.moveCar)

        #Create a car sprite
        self.car = Actor('car2.png',200,200)
        self.obstacle= Actor('obstacle.png',400,350)
        self.add( self.car)
        self.add(self.obstacle)
               
    #update is constantly refreshed by schedule method        
    def moveCar(self,dt):
        self.car.gas()
        self.car.turn()
        if self.car.isTouching(self.obstacle):
            self.car.crash()
        
    def on_key_press(self, key, modifiers):
        """This function is called when a key is pressed.
        
        'key' indicates which key was pressed.
        'modifiers' is a bitwise  of several constants indicating which
           modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
        See also on_key_release situations when a key press does not fire an
         'on_key_press' event.
        """
        #Only needed locally
        pressedKey = pyglet.window.key.symbol_string(key)
        
        if (pressedKey == 'UP' or pressedKey == 'DOWN'):
            self.car.moveKey = pressedKey
        if (pressedKey == 'RIGHT' or pressedKey == 'LEFT'):
            self.car.turnKey = pressedKey
        
    
    def on_key_release(self, key, modifiers):
        pressedKey = pyglet.window.key.symbol_string(key)
        if (pressedKey == 'RIGHT' or pressedKey == 'LEFT'):
            self.car.turnKey = None
        if (pressedKey == 'UP' or pressedKey == 'DOWN'):
            self.car.moveKey = None
        
            
 
        
        

        



