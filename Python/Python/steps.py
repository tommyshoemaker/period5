#
# firstKarelPgm.py
#
# Program to instantiate a robot at the origin (facing East w/1 beeper).  Robot moves over a fixed size
# hurdle, lays a beeper at the hurdle's base, then moves one block away, faces North and shuts off.

# Important preamble: keep in all karel programs
from karel.robota import East
from karel.robota import West
from karel.robota import North
from karel.robota import South
from karel.robota import infinity
from karel.robota import window
from karel.robota import world
from karel.robota import UrRobot

# The Karel task block  
def task():
        def turnSB15(a):
                for i in range(a):
                        sb15.turnLeft()
        def turnKarel(a):
                for i in range(a):
                        karel.turnLeft()
#       Commands to control the "world"
        world.readWorld("stepsWorld.kwld")    # open a particular world file
        world.setSize(10,10)               # set the size of the visible world
        #^^ should be 10
        world.setDelay(90)                # set simulation speed. 0-fastest, 100-slowest

        karel = UrRobot(2,3,East, 1,fill="blue")
        sb15 = UrRobot(1,6,North, 10, fill="green")
        sb15.move()
        karel.turnLeft()
        turnSB15(1)
        sb15.move()
        turnSB15(3)
        sb15.move()
        turnSB15(1)
        sb15.move()
        turnSB15(1)
        turnKarel(1)
        karel.move()
        turnKarel(1)
        karel.move()
        turnKarel(2)
        turnSB15(2)
        
        #Write the code to make your robot climb the steps and get to the other side
        


# Important epilogue: keep in all karel programs    
if __name__ == '__main__':
        window().run(task)
    
