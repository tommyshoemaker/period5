""" Copyright 2008 Joseph Bergin
License: Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License


This adapter has the same interface as robotworld.py but hooks everything up to the Java
world. It creates robots there when the python programmer creates them here, registers them
in that world, moves them, etc. 


"""

import sys
import thread
import threading
import karel.robota
import time

from karel.basicdefinitions import legalCorner
from karel.basicdefinitions import infinity
from karel.basicdefinitions import NoBeepers
from karel.basicdefinitions import NoRobots
from karel.basicdefinitions import IllegalCorner

from karel.observable import Observer
#from exceptions import NotImplementedError
from kareltherobot import RobotWorldWindow
from kareltherobot import WorldBuilder
from kareltherobot import World
import kareltherobot
from java.awt import Color

try :
    if True :
        pass
except Exception :
    True = 1
    False = 0
#infinity = -1
#INFINITE = infinity # Deprecated, use infinity



class Runner:
    def run(self, task, *pargs):
       mainThread = threading.Thread(target = task, args=pargs)
       mainThread.start()

def window():
    return Runner()
    
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
        self._eastWestWalls = {}
        self._northSouthWalls = {}
        self._robots = {}
        self.__delay = 0
        self._isVisible = False
#        self.__world = World.asObject
        World.setTrace(False)
        World.setDelay(0)
        World.setVisible(True)
        self.__shadows = {}
        self.__directionMap = {karel.robota.North:kareltherobot.Directions.North, 
                               karel.robota.East: kareltherobot.Directions.East, 
                               karel.robota.South:kareltherobot.Directions.South,
                               karel.robota.West: kareltherobot.Directions.West}
        self.__colorMap = {
                           "red": Color.red,
                           "green": Color.green,
                           "yellow": Color.yellow,
                           "blue": Color.blue,
                           "orange": Color.orange,
                           "white": Color.white,
                           "black": Color.black,
                           "cyan": Color.cyan,
                           "magenta": Color.magenta,
                           "pink": Color.pink
                           }
        
    def update(self, robot, robotState = None):
        "This is called whenever any robot changes state since the world observes all robots"
        if robotState == None :
            return
        action = robotState.action()
        if action == karel.robota.UrRobot.createAction :
            theDirection = self.__directionMap[robot._UrRobot__direction]
            try :
                color = self.__colorMap[robot._UrRobot__fill]
            except Exception:
                color = None
            if color != None :
                self.__shadows[robot] = kareltherobot.UrRobot(robot._UrRobot__street, robot._UrRobot__avenue, 
                                            theDirection,robot._UrRobot__beepers, color)
            else :
                self.__shadows[robot] = kareltherobot.UrRobot(robot._UrRobot__street, robot._UrRobot__avenue, 
                                            theDirection,robot._UrRobot__beepers)
        elif action == karel.robota.UrRobot.moveAction :
            self.__shadows[robot].move()
        elif action == karel.robota.UrRobot.pickBeeperAction :
            self.__shadows[robot].pickBeeper()
        elif action == karel.robota.UrRobot.putBeeperAction :
            pass #self.__shadows[robot].putBeeper() 
        elif action == karel.robota.UrRobot.turnLeftAction :
            self.__shadows[robot].turnLeft()
        elif action == karel.robota.UrRobot.turnOffAction :
            self.__shadows[robot].turnOff()
        
        if action == karel.robota.UrRobot.moveAction or action == karel.robota.UrRobot.createAction :
            self._registerRobot(robot)
            
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
        World.setDelay(amount)
        
    def speedCheck(self):
        self.__delay = World.delay()
    
#    _runnables = []
    
        
    def placeBeepers(self, street, avenue, howMany=1, byUser = True):
        """
        Place any number of beepers at a corner. Use RobotWorld.infinity to place an infinite number.
        The number will be added to the number currently there. Don't try to reduce the number
        by giving a negative value. Strange behavior can result since negative values are treated as infinite. 
        """
        if byUser :
            World.placeBeepers(street, avenue, howMany)
        if howMany == 0 :
            return
        legalCorner(street, avenue)
        place = (street, avenue)
        if howMany < 0 :
            self._beepers[place] = infinity
            return
        inWorld = self._beepers.get(place, 0)
        if inWorld != infinity :
            self._beepers[place] = howMany + inWorld
            
        
    def placeWallNorthOf(self, street, avenue):
        "Place an east-west wall segment north of this corner"
        legalCorner(street, avenue)
        self._eastWestWalls[(street, avenue)] = 1;
        World.placeEWWall(street, avenue, 1)
        
    def placeWallEastOf(self, street, avenue):
        "Place a north-south wall segment east of this corner"
        legalCorner(street, avenue)
        self._northSouthWalls[(street, avenue)] = 1;
        World.placeNSWall(street, avenue, 1)
        
    def reset(self):
        World.resetRobots()
        World.reset()
        World.repaint()
        RobotWorldBase.reset(self)       

    def removeBeeper(self, street, avenue, byUser = True) :
        """Remove a single beeper from this corner. An exception will be raised if there are none"""
#        if byUser :
#            World.placeBeepers(street, avenue, -1)  #decreaseBeeperIfPossible(street, avenue)
        place = (street, avenue)
        howMany = self._beepers.get(place, 0)
        if howMany > 0 :
            howMany -= 1
            if howMany == 0 :
                self._beepers[place] = howMany #TODO: replace this with .pop(place)
            else:
                self._beepers[place] = howMany
        elif howMany == infinity :
            return
        else :
#            raise NoBeepers("(" + str(street) + ", " + str(avenue) + ")")
            pass
        
        
#    def _visible(self, x, y, xBound, yBound):
#        return x >= 0 and y >= 0 and x < xBound and y < yBound
        

    def setSize(self, numberOfStreets=10, numberOfAvenues=10):
        World.setSize(numberOfStreets, numberOfAvenues) # default 10 by 10
    
    def setVisible(self, visible = True):
        self._isVisible = visible
        World.setVisible(visible)
#        raise NotImplementedError("SetVisible needs to be implemented") # true to show, false to hide
    
    def isVisible(self):
        return self._isVisible
    
    def showBuilder(self):
        builder = WorldBuilder(True)
        
    def showSpeedControl(self, visible = True):
        World.showSpeedControl(visible)
    

world = RobotWorld("Karel's World")

if __name__ == '__main__' :
    World.setVisible(True)
    builder = WorldBuilder(False)
   