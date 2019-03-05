""" Copyright 2008 Joseph Bergin
License: Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License

Represents the robot world. It maintains knowledge about walls and beepers in the world. It also knows 
about the robots that have been created. 

It has API to place beepers and walls.

It can read and write world files

It is a mediator between the robota classes and the pygtk graphics layer. 
"""

import threading
import karel.robota
import time
from karel.observable import Observer
#from exceptions import NotImplementedError

from karel.basicdefinitions import legalCorner
from karel.basicdefinitions import infinity
from karel.basicdefinitions import NoBeepers
from karel.basicdefinitions import NoRobots
from karel.basicdefinitions import IllegalCorner


from karel.gtkwindow import RobotImage
from karel.gtkwindow import KarelWindow
from karel.gtkWorldMaker import WorldMaker

_window = None #KarelWindow(12, 12)

try :
    if True :
        pass
except Exception :
    True = 1
    False = 0


from karel.robotworldbase import RobotWorldBase

class RobotWorld(RobotWorldBase, Observer) :
    """
    The robot world consisting of horizontal streets, vertical avenues, walls, and beepers. 
    The bottom left corner of the world is (1, 1), First street and first avenue. 
    While it is technically possible to create many objects of type RobotWorld, note that they won't be
    useful, as the robots themselves have defined their own world and "live" there. robota.world is the
    world known to the robots. It can, however, be replaced with a simple assignment.
    
    The world observes all robots. 
    """
    
    def __init__(self, name):
        "Create an empty world."
        self._name = name
        self._beepers = {}
#        self.__gBeepers = {}
        self._eastWestWalls = {}
        self._northSouthWalls = {}
        self._robots = {}
        self.__gRobots = {}
        self.__delay = 80 # slow
        self._isVisible = False
        self.__beeperControl = threading.Condition()
        
    def update(self, robot, robotState = None):
        "This is called whenever any robot changes state since the world observes all robots"
        if robotState == None :
            return
        action = robotState.action()
        if action == karel.robota.UrRobot.moveAction  :
            self._registerRobot(robot)
#            self.__gRobots[robot].move(_window.drawArea(), _window.delta())
            if _window != None:
                _window.moveRobot(self.__gRobots[robot])
            
        elif action == karel.robota.UrRobot.createAction :
            self._registerRobot(robot)
            if _window != None:
                (street, avenue) = (robot._UrRobot__street, robot._UrRobot__avenue)
                self.__gRobots[robot] = _window.addRobot(street, avenue, robot._UrRobot__direction,
                                                     robot._UrRobot__fill, robot._UrRobot__outline)
            
        elif action == karel.robota.UrRobot.turnLeftAction :
            if _window != None:
                self.__gRobots[robot].rotate()
        
        elif action == karel.robota.UrRobot.pickBeeperAction :
            pass # moved to removeBeeper
        
        elif action == karel.robota.UrRobot.putBeeperAction :
            pass
        
        elif action == karel.robota.UrRobot.turnOffAction :
                self.__gRobots[robot].turnOff()
                        
        else :
            pass
        
            
    def name(self):
        "Return the name of this world"
        return self._name
    
    def setDelay(self, amount): # MANUALTEST: Must be tested manually
        """Set the amount by which primitive instructions should be delayed
        0 (default) means not at all
        100 (the maximum) means a lot (currently about 1 second)
        """
        if amount < 0 : amount = 0
        if amount > 100 : amount = 100
        self.__delay = amount 
        if _window != None :
            _window.setDelay(amount)
#        _window.iv.set(100 - amount) # TODO needs a replacemen t
        
    def speedCallback(self,*args):
        global _window
        if _window != None :
            self.setDelay(100 - args[0]) # TODO needs a replacemen t
            pass
        
    def speedCheck(self):
        pass
    
    def reset(self):
        window().reset()
        RobotWorldBase.reset(self)

            
    def placeBeepers(self, street, avenue, howMany=1, byUser = True):
        """
        Place any number of beepers at a corner. Use RobotWorld.infinity to place an infinite number.
        The number will be added to the number currently there. Don't try to reduce the number
        by giving a negative value. Strange behavior can result since negative values are treated as infinite. 
        """
        self.__beeperControl.acquire()
        if howMany == 0 :
            return
        legalCorner(street, avenue)
        place = (street, avenue)
        
        if howMany < 0 :
            self._beepers[place] = infinity
            if _window != None:
                _window.deleteBeeper(place)               
                _window.placeBeeper(street, avenue, infinity)
                self.__beeperControl.notify()
                self.__beeperControl.release()
            return
        inWorld = self._beepers.get(place, 0)
        toPut = howMany + inWorld
        if inWorld != infinity :
            self._beepers[place] = toPut
            if _window != None:
                if inWorld > 0 :
                    _window.deleteBeeper(place)
                _window.placeBeeper(street, avenue, toPut)
        self.__beeperControl.notify()
        self.__beeperControl.release()
            
        
    def placeWallNorthOf(self, street, avenue):
        "Place an east-west wall segment north of this corner"
        legalCorner(street, avenue)
        self._eastWestWalls[(street, avenue)] = 1;
#        if _window != None:
        window().placeWallNorthOf(street, avenue)
        
    def removeWallNorthOf(self, street, avenue):
        legalCorner(street, avenue)
        try:
            self._eastWestWalls.pop((street, avenue))
            if _window != None:
                _window.removeWallNorthOf(street, avenue)
        except:
#            print "world ew wall"
            pass
            
        
    def placeWallEastOf(self, street, avenue) :
        "Place a north-south wall segment east of this corner"
        legalCorner(street, avenue)
        self._northSouthWalls[(street, avenue)] = 1;
#        if _window != None:
        window().placeWallEastOf(street, avenue)
        
    def removeWallEastOf(self, street, avenue):
        legalCorner(street, avenue)
        try:
            self._northSouthWalls.pop((street, avenue))
            if _window != None:
                _window.removeWallEastOf(street, avenue)
        except:
#            print "world ns wall"
            pass
        
    def removeAllBeepers(self, street, avenue):
        place = (street, avenue)
        _window.deleteBeeper(place)
        self._beepers.pop(place)
        

    def removeBeeper(self, street, avenue, byUser = True) :
        """Remove a single beeper from this corner. An exception will be raised if there are none"""
        self.__beeperControl.acquire()
        place = (street, avenue)
        howMany = self._beepers.get(place, 0)
        if howMany > 0 :
            howMany -= 1
            if howMany == 0 :
                self._beepers.pop(place)
                if _window != None :
                    _window.deleteBeeper(place)
            else:
                self._beepers[place] = howMany
                if _window != None:
                    _window.deleteBeeper(place)
                    _window.placeBeeper(street, avenue, howMany)
        elif howMany == infinity :
            return
        else :
            self.__beeperControl.notify()
            self.__beeperControl.release()
            raise NoBeepers("(" + str(street) + ", " + str(avenue) + ")")
        self.__beeperControl.notify()
        self.__beeperControl.release()
                

    def setSize(self, numberOfStreets=10, numberOfAvenues=10):  
        if numberOfStreets <= 0 or numberOfAvenues <= 0:
            numberOfStreets = 10
            numberOfAvenues = 10
        global _window
        if _window == None :
            _window = KarelWindow(numberOfStreets, numberOfAvenues, world.speedCallback)   
        else :   
            _window.clearScreen()
            _window.setSize(numberOfStreets)
    
    def setVisible(self, visible = True):
        self._isVisible = visible
    
    def isVisible(self):
        return self._isVisible
    
    def _showBuilder(self):
        self._builder = WorldMaker(window(), self) 
        
    def showSpeedControl(self, visible = True):
        pass #Not needed in this version. Always visible
    
    def getWindow(self):
        global window
        return window()
    
world = RobotWorld("Karel's World")

def window():
    global _window
    if _window == None :
        _window = KarelWindow(12, 12, world.speedCallback)      
    return _window

def task():
    world.setSize(10, 10)
    world._showBuilder()

    
if __name__ == '__main__' :
    window().run(task)
    
    
