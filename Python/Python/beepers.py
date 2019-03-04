# beepers.py

# Program to instantiate a robot at the origin (facing East w/1 beeper).  

# Important preamble: keep in all karel programs
from karel.robota import East
from karel.robota import West
from karel.robota import North
from karel.robota import South
from karel.robota import infinity
from karel.robota import window
from karel.robota import world
from karel.robota import UrRobot
import time

# The Karel task block  
def task():
        #Commands to control the "world"
        #Open a particular world file
        world.readWorld("beeperWorld.kwld")
        #Set the size of the visible world
        world.setSize(10,10)
        #Set the speed of the robot
        world.setDelay(30)

        sb15 = UrRobot(5, 6, North, 1, fill='green', outline='blue')
        def turn(a):
                for i in range(a):
                        sb15.turnLeft()
        def pickAndTurn(a):
                for i in range(a):
                        sb15.pickBeeper()
                        sb15.turnLeft()
                        sb15.move()
                        turn(3)
                        sb15.move()
        #Write the code to make your robot pick up all the beepers.
        sb15.turnLeft()
        sb15.move()
        pickAndTurn(4)
        sb15.pickBeeper()
        time.sleep(3)
# Important epilogue: keep in all karel programs    
if __name__ == '__main__':
        window().run(task)
