import cocos
import pyglet
from cocos.actions import *
from collections import defaultdict
import math


class CarLayer(cocos.layer.Layer):
    is_event_handler = True  #: enable mouse and keyboard events
    #Always call super in the constructor:
    def __init__(self):
        super(CarLayer, self).__init__()

        #schedule method i keeps refreshing the moveCar method below
        self.schedule(self.driveCar)

        #Create a car sprite
        self.car = cocos.sprite.Sprite('car2.png')
        #place the sprite in the center of the screen:
        self.car.position = 200,200
        self.add( self.car)
        #Key used for turning car
        self.turnKey = None
        #Key used for moving car
        self.moveKey= None

    def turn(self):
        if (self.turnKey=='RIGHT'):
                self.car.do(RotateBy(5,duration=.08))
        elif (self.turnKey=='LEFT'):
                self.car.do(RotateBy(-5,duration=.08))

    def moveForward(self):
        #I adusted the angle because the unit circled is flipped on cocos2d
        #At the same time I converted to radians since python assumes it is given rads in sin, cos
        adjustedRotation = math.radians(-(self.car.rotation - 360))
        self.car.do(MoveBy((math.cos(adjustedRotation),math.sin(adjustedRotation)),duration=.008))

    def moveBackward(self):
        #I adusted the angle because the unit circled is flipped on cocos2d
        #At the same time I converted to radians since python assumes it is given rads in sin, cos
        #Additionally note the - in both MoveBy coord since we want to move backwards
        pass
        
    def move(self):
        if (self.moveKey=='UP'):
            self.moveForward()
        #add the condition for moveBackward
        
    #update is constantly refreshed by schedule method
    #Note that since I changed the name of the method here I had to change it in the schedule call above
    def driveCar(self,dt):
        self.move()
        self.turn()
        
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
        if (pressedKey == 'RIGHT' or pressedKey == 'LEFT'):
            self.turnKey = pressedKey
        if (pressedKey == 'UP' or pressedKey == 'DOWN'):
            self.moveKey = pressedKey
        
    
    def on_key_release(self, key, modifiers):
        pressedKey = pyglet.window.key.symbol_string(key)
        if (pressedKey == 'RIGHT' or pressedKey == 'LEFT'):
            self.turnKey = None
        if (pressedKey == 'UP' or pressedKey == 'DOWN'):
            self.moveKey = None
        
            
 
        
        

        



