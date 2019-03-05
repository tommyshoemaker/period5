#
# maze.py
#
# Program to instantiate a robot at the origin (facing East w/1 beeper).  


# Important preamble: keep in all karel programs


from karel.robota import Robot
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
#       Commands to control the "world"
        world.readWorld("maze2.kwld")    # open a particular world file
        world.setSize(10,10)               # set the size of the visible world
        world.setDelay(50)              # set simulation speed. 0-fastest, 100-slowest
 
        #create a Robot sprite (give it your name) and start it on
        # Street 3, Avenue 1
        sb15 = Robot(3, 1, East, 0, fill='blue', outline='green')
        
        #Write the code to make your robot find it's way out of the maze and end up 
        #on Street 8, Avenue 5 and pick up the beeper that's there
        while not sb15.anyBeepersInBeeperBag():
                if sb15.frontIsClear():
                        sb15.move()
                else:
                        sb15.turnLeft()
                        if not sb15.frontIsClear():
                                sb15.turnLeft()
                                sb15.turnLeft()
                if sb15.nextToABeeper():
                        sb15.pickBeeper()
                        
# Important epilogue: keep in all karel programs    
if __name__ == '__main__':
        window().run(task)
