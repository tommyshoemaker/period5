"""Make nextRow() in each row sequence"""
from karel.robota import *
#------------My Classes------------

#------------Climber Class------------
class Climber(UrRobot):
    def turn(self, a):
        for i in range(a):
            self.turnLeft()
    def climbStep(self, a):
        for i in range(a):
            #Must be facing north at bottom of step
            self.move()
            self.turn(3)
            self.move()
            self.turn(1)
#------------Dancer Class------------
class Dancer(UrRobot):
    def pickBeeperNum(self, a):
        for i in range(a):
            self.pickBeeper()
    def turnRight(self):
        self.turnLeft()
        self.turnLeft()
        self.turnLeft()
    def turnAround(self):
        self.turnLeft()
        self.turnLeft()
    def spin(self):
        self.turnAround()
        self.turnAround()
    def backUp(self, a):
        for i in range(a):
            self.turnAround()
            self.move()
            self.turnAround()
    def slideRight(self, a):
        for i in range(a):
            self.turnRight()
            self.move()
            self.turnLeft()
    def slideLeft(self, a):
        for i in range(a):
            self.turnLeft()
            self.move()
            self.turnRight()
    def dance(self, a):
        self.move()
        self.backUp(2)
        self.move()
        self.slideLeft(1)
        self.slideRight(2)
        self.slideLeft(1)
        self.slideRight(1)
        self.slideLeft(1)
    def partnerDance(self, a):
        self.backUp(1)
        self.move()
        self.move()
        self.backUp(1)
        self.slideRight(1)
        self.slideLeft(2)
        self.slideRight(1)
        self.slideLeft(1)
        self.slideRight(1)
    def danceSteps1(self):
        self.move()
        self.pickBeeper()
        self.backUp(1)
        self.slideLeft(1)
        self.backUp(1)
        self.pickBeeper()
        self.move()
        self.slideRight(2)
        self.backUp(1)
        self.pickBeeper()
        self.move()
        self.slideLeft(1)
        self.pickBeeper()
    def danceSteps2(self):
        self.move()
        self.slideLeft(1)
        self.pickBeeper()
        self.slideRight(2)
        self.pickBeeper()
        self.slideLeft(1)
        self.backUp(2)
        self.slideLeft(1)
        self.pickBeeper()
        self.slideRight(2)
        self.pickBeeper()
        self.slideLeft(1)
        self.move()
        self.pickBeeper()
#----------------Writer Class ------------------------------
class Writer(Dancer):
    """All methods in this class assume Writer is in the bottom 
    left of letter and pointing East. All methods line writes should
    make the robot move 5 avenues across.
    All letters have a width of 5 avenues and a height of 5 streets"""

    def bigMove(self, a):
        #Moves 'a' times
        for i in range(a):
            self.move()

    def putMove(self, a):
        #Puts beeper and moves
        for i in range(a):
            self.putBeeper()
            self.move()

    def xxxxx(self):
        self.putMove(5)
        self.nextRow()

    def xxxx_(self):
        self.putMove(4)
        self.move()
        self.nextRow()

    def x_xxx(self):
        self.putMove(1)
        self.move()
        self.putMove(3)
        self.nextRow()

    def xxx__(self):
        self.putMove(3)
        self.bigMove(2)
        self.nextRow()

    def x___x(self):
        self.putMove(1)
        self.bigMove(3)
        self.putMove(1)
        self.nextRow()
        
        
    def x__x_(self):
        self.putMove(1)
        self.bigMove(2)
        self.putMove(1)
        self.move()
        self.nextRow()

    def _x_x_(self):
        self.move()
        self.putMove(1)
        self.move()
        self.putMove(1)
        self.move()
        self.nextRow()

    def x_x__(self):
        self.putMove(1)
        self.move()
        self.putMove(1)
        self.bigMove(2)
        self.nextRow()

    def x____(self):
        self.putMove(1)
        self.bigMove(4)
        self.nextRow()

    def __x__(self):
        self.bigMove(2)
        self.putMove(1)
        self.bigMove(2)
        self.nextRow()

    def ____x(self):
        self.bigMove(4)
        self.putMove(1)
        self.nextRow()

    def x_x_x(self):
        self.putMove(1)
        self.move()
        self.putMove(1)
        self.move()
        self.putMove(1)
        self.nextRow()

    def xx_xx(self):
        self.putMove(2)
        self.move()
        self.putMove(2)
        self.nextRow()
    def x__xx(self):
        self.putMove(1)
        self.bigMove(2)
        self.putMove(2)
        self.nextRow()
    def xx__x(self):
        self.putMove(2)
        self.bigMove(2)
        self.putMove(1)
        self.nextRow()
        
    def nextRow(self):
        '''Robot must be one avenue further than last beeper placed and facing East.
        Robot should end up one corner North, five corners West, facing East'''
        self.turnLeft()
        self.move()
        self.turnLeft()
        self.bigMove(5)
        self.turnAround()

    def nextLetter(self):
        '''Assumes robot position is one corner to the East of top right corner of
        letter and facing East. Must end up 2 corners East of previous letter and
        at the bottom to be in position to start at the bottom left of the new letter'''
        self.bigMove(6)
        self.turnRight()
        self.bigMove(6)
        self.turnLeft()

    def newLine(self, a):
        self.turnLeft()
        self.bigMove(7)
        self.turnLeft()
        for i in range(a):
            self.bigMove(6)
        self.turnAround()

    """----------LETTERS----------"""
    def a(self):
        self.x___x()
        self.x___x()
        self.x___x()
        self.xxxxx()
        self.x___x()
        self.xxxxx()
        self.nextLetter()
    def b(self):
        self.xxxx_()
        self.x___x()
        self.x___x()
        self.xxxx_()
        self.x___x()
        self.xxxx_()
        self.nextLetter()
    def c(self):
        self.xxxxx()
        self.x____()
        self.x____()
        self.x____()
        self.x____()
        self.xxxxx()
        self.nextLetter()
    def d(self):
        self.xxxx_()
        self.x___x()
        self.x___x()
        self.x___x()
        self.x___x()
        self.xxxx_()
        self.nextLetter()
    def e(self):
        self.xxxxx()
        self.x____()
        self.x____()
        self.xxxx_()
        self.x____()
        self.xxxxx()
        self.nextLetter()
    def f(self):
        self.x____()
        self.x____()
        self.x____()
        self.xxxx_()
        self.x____()
        self.xxxxx()
        self.nextLetter()
    def g(self):
        self.xxxxx()
        self.x___x()
        self.x_xxx()
        self.x____()
        self.x____()
        self.xxxxx()
        self.nextLetter()
    def h(self):
        self.x___x()
        self.x___x()
        self.xxxxx()
        self.x___x()
        self.x___x()
        self.x___x()
        self.nextLetter()
    def i(self):
        self.xxxxx()
        self.__x__()
        self.__x__()
        self.__x__()
        self.__x__()
        self.xxxxx()
        self.nextLetter()
    def j(self):
        self.xxxxx()
        self.x___x()
        self.x___x()
        self.____x()
        self.____x()
        self.____x()
        self.nextLetter()
    def k(self):
        self.x___x()
        self.x___x()
        self.x__x_()
        self.xxx__()
        self.x__x_()
        self.x___x()
        self.nextLetter()
    def l(self):
        self.xxxxx()
        self.x____()
        self.x____()
        self.x____()
        self.x____()
        self.x____()
        self.nextLetter()
    def m(self):
        self.x___x()
        self.x___x()
        self.x___x()
        self.x_x_x()
        self.xx_xx()
        self.x___x()
        self.nextLetter()
    def n(self):
        self.x___x()
        self.x__xx()
        self.x_x_x()
        self.x_x_x()
        self.xx__x()
        self.x___x()
        self.nextLetter()
    def o(self):
        self.xxxxx()
        self.x___x()
        self.x___x()
        self.x___x()
        self.x___x()
        self.xxxxx()
        self.nextLetter()
    def p(self):
        self.x____()
        self.x____()
        self.x____()
        self.xxxx_()
        self.x___x()
        self.xxxx_()
        self.nextLetter()
    def q(self):
        self.xxxxx()
        self.x__xx()
        self.x_x_x()
        self.x___x()
        self.x___x()
        self.xxxxx()
        self.nextLetter()
    def r(self):
        self.x___x()
        self.x__x_()
        self.x_x__()
        self.xxxx_()
        self.x___x()
        self.xxxx_()
        self.nextLetter()
    def s(self):
        self.xxxxx()
        self.____x()
        self.____x()
        self.xxxxx()
        self.x____()
        self.xxxxx()
        self.nextLetter()
    def t(self):
        self.__x__()
        self.__x__()
        self.__x__()
        self.__x__()
        self.__x__()
        self.xxxxx()
        self.nextLetter()
    def u(self):
        self.xxxxx()
        self.x___x()
        self.x___x()
        self.x___x()
        self.x___x()
        self.x___x()
        self.nextLetter()
    def v(self):
        self.__x__()
        self._x_x_()
        self._x_x_()
        self.x___x()
        self.x___x()
        self.x___x()
        self.nextLetter()
    def w(self):
        self.x___x()
        self.xx_xx()
        self.x_x_x()
        self.x___x()
        self.x___x()
        self.x___x()
        self.nextLetter()
    def x(self):
        self.x___x()
        self.x___x()
        self._x_x_()
        self.__x__()
        self._x_x_()
        self.x___x()
        self.nextLetter()
    def y(self):
        self.__x__()
        self.__x__()
        self.__x__()
        self.__x__()
        self._x_x_()
        self.x___x()
        self.nextLetter()
    def z(self):
        self.xxxxx()
        self.x____()
        self._x___()
        self.__x__()
        self.___x_()
        self.xxxxx()
        self.nextLetter()
#------------PinSetter Class------------
class PinSetter(Writer):
    def getReady(self):
        #Assumes robot is facing North and one street lower
        #than where the first pin should be set
        self.move()
        self.turnRight()
    def set(self, a):
        #Assumes robot is facing East OR West on corner that a pin goes on.
        #Puts variable a amount of beepers and moves accordingly
        #Variable a can be integer 1-4
        if a == 1:
            self.putMove(1)
        elif a > 1:
            self.putMove(1)
            for i in range(a-1):
                self.move()
                self.putMove(1)
    def nextRowRight(self):
        #Assumes robot is facing East and tht he has
        #finished setting pins for that row
        #Robot will end up one Street North and facing West.
        self.turnLeft()
        self.move()
        self.turnLeft()
    def nextRowLeft(self):
        #Assumes robot is facing West and that he has
        #finished setting pins for that row
        #Robot will end up one street North and facing East
        self.turnRight()
        self.move()
        self.turnRight()
    def nextRowRightUp(self):
        self.nextRowRight()
        self.move()
        self.move()
    def nextRowLeftUp(self):
        self.nextRowLeft()
        self.move()
        self.move()
    def setPins(self):
        self.getReady()
        self.set(1)
        self.nextRowRight()
        self.set(2)
        self.nextRowLeft()
        self.set(3)
        self.nextRowRight()
        self.set(4)
        self.nextRowLeftUp()
        self.set(3)
        self.nextRowRightUp()
        self.set(2)
        self.nextRowLeftUp()
        self.set(1)
#------------Harvester Class------------
class Harvester(PinSetter):
    #col = collect
    def colMove(self, a):
        self.pickBeeper()
        self.move()
    def col(self, a):
        #Assumes robot is facing East OR West on corner that a pin goes on.
        #Collects variable a amount of beepers and moves accordingly
        #Variable a can be integer 1-4
        if a == 1:
            self.colMove(1)
        elif a > 1:
            self.colMove(1)
            for i in range(a-1):
                self.move()
                self.colMove(1)
    def colPins(self):
        self.getReady()
        self.col(1)
        self.nextRowRight()
        self.col(2)
        self.nextRowLeft()
        self.col(3)
        self.nextRowRight()
        self.col(4)
        self.nextRowLeftUp()
        self.col(3)
        self.nextRowRightUp()
        self.col(2)
        self.nextRowLeftUp()
        self.col(1)
class Racer(Writer,Robot):
    def moveJump(self):
            if self.frontIsClear():
                self.move()
            else:
                self.turnLeft()
                self.move()
                for i in range(2):
                    self.turnRight()
                    self.move()
                self.turnLeft()
    def celebrate(self):
        world.setDelay(1)
        while True:
            self.turnLeft()
    def run(self):
        while not self.anyBeepersInBeeperBag():
            self.moveJump()
            if self.nextToABeeper():
                self.pickBeeper()
                self.celebrate()
class SteepleChaser(Racer):
    def jump(self):
        self.checkHeight()
        self.move()
        self.turnRight()
        self.drop()

    def checkHeight(self):
        while not self.frontIsClear():
            self.turnLeft()
            self.move()
            self.turnRight()
    
    def drop(self):
        while self.frontIsClear():
            self.move()
        self.turnLeft()
class CarpetLayer(SteepleChaser):
    def isRoom(self):
        #Returns True if corner is bounded by walls
        #on the North, East, and West and False otherwise.
        room = False
        
        if self.facingNorth and not self.frontIsClear():
            self.turnLeft()
            if self.facingWest and not self.frontIsClear():
                self.turnLeft()
                self.turnLeft()
                if self.facingEast and not self.frontIsClear():
                    room = True
                self.turnRight()
            else:
                self.turnLeft()
        return room
    def layCarpet(self):
        #Should check if it is a "small room" and if so, put a beeper down.
        print(self.isRoom())
            
    def carpetBlock(self):
        #Should carpet rooms on a block
        while True:
            if self.layCarpet():
                self.putBeeper()
            elif self.facingNorth():
                self.turnAround()
                self.move()
                self.turnLeft()
                self.move()
                self.turnLeft()
                self.move()
class Prospector(CarpetLayer):
    def faceNorth(self):
        while not self.facingNorth():
            self.turnLeft()
    def faceSouth(self):
        while not self.facingSouth():
            self.turnLeft()
    def faceEast(self):
        while not self.facingEast():
            self.turnLeft()
    def faceWest(self):
        while not self.facingWest():
            self.turnLeft()
    def howManyBeepers(self):
        number = 0
        while self.nextToABeeper():
            self.pickBeeper()
            number += 1
        for i in range(number):
            self.putBeeper()
        return number
    def findNextDirection(self):
        direction = self.howManyBeepers()
        if direction == 1:
            self.faceNorth()
        elif direction == 2:
            self.faceSouth()
        elif direction == 3:
            self.faceWest()
        elif direction == 4:
            self.faceEast()
        else:
            self.turnOff()
    def hunt(self):
        while self.frontIsClear():
            if self.nextToABeeper():
                self.findNextDirection()
            self.move()
        self.findNextDirection()
    def goToOrigin(self):
        while self.frontIsClear():
           self.move()
        self.turnLeft()
        
