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
        self.schedule(self.moveCar)

        #Create a car sprite
        self.car = cocos.sprite.Sprite('car.png')
        #place the sprite in the center of the screen:
        self.car.position = 500,20
        self.add( self.car)
        self.pressedKey = None

    #update is constantly refreshed by schedule method        
    def moveCar(self,dt):
        if self.pressedKey =='RIGHT':
            if (self.car.rotation <= 178 or self.car.rotation >= 182):
                self.car.do(MoveBy((10,10),duration=.1))
                self.car.do(RotateBy(5,duration=.008))
            else:
                self.car.do(MoveBy((10,0),duration=.1))
               
        if self.pressedKey =='LEFT':
            self.car.rotation = 0
            self.car.do(MoveBy((-10,0),duration=.1))
        if self.pressedKey =='UP':
            self.car.rotation = 90
            self.car.do(MoveBy((0,10),duration=.1))
        if self.pressedKey =='DOWN':
            self.car.rotation = 270
            self.car.do(MoveBy((0,-10),duration=.1))
        
    def on_key_press(self, key, modifiers):
        """This function is called when a key is pressed.
        
        'key' indicates which key was pressed.
        'modifiers' is a bitwise  of several constants indicating which
           modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
        See also on_key_release situations when a key press does not fire an
         'on_key_press' event.
        """       
        self.pressedKey = pyglet.window.key.symbol_string(key)
    
    def on_key_release(self, key, modifiers):
        self.pressedKey= None
        
            
 
        
        

        



