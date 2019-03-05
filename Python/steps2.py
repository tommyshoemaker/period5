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
        #Commands to control the "world"
        world.readWorld("steps2.kwld")
        #Opens a particular world file
        world.setSize(10,10)
        #Sets the size of the visible world
        world.setDelay(30)
        #set simulation speed. 0-fastest, 100-slowest

        sb15 = Climber(1, 1, North, 1, fill="green", outline="blue")        
        #Write the code to make your robot climb the steps and get to the other side
        sb15.climbStep(5)
        sb15.turnOff()
# Important epilogue: keep in all karel programs    
if __name__ == '__main__':
        window().run(task)
