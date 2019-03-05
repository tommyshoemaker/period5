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
from MyRobotClasses import Turner

# The Karel task block  
def task():
#       Commands to control the "world"
        world.readWorld("steps2.kwld")    # open a particular world file
        world.setSize(10,10)               # set the size of the visible world
        world.setDelay(50)                # set simulation speed. 0-fastest, 100-slowest

        
        robot1= Turner(1,1,West,0)  #Note: this will cause an error until you import the class
        robot2= Turner(2,2,South,0,"pink")
        robot3= Turner(4,3,North,0,"red")
        robot4= Turner(5,4,North,0,"blue")
        robot5= Turner(6,7,North,0,"black")

        #Make robot1 turn right

        #Make robot2 turn around

        #Make robot3 back up

        #Make robot4 slide left

        #Make robot5 slide right
        
        
        


# Important epilogue: keep in all karel programs    
if __name__ == '__main__':
        window().run(task)
    
