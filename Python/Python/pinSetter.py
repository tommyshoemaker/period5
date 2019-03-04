#
#

# Important preamble: keep in all karel programs
from karel.robota import East
from karel.robota import West
from karel.robota import North
from karel.robota import South
from karel.robota import infinity
from karel.robota import window
from karel.robota import world
from karel.robota import UrRobot
from Shoemaker_Thomas_MyClasses import * #CHANGE To your file name

# The Karel task block  
def task():
#       Commands to control the "world"
        
        # set the size of the visible world
        world.setSize(9)
        # set simulation speed. 0-fastest, 100-slowest
        world.setDelay(0.001)

        
        
        #TO DO: Create a PinSetter Robot, Street 1, Avenue 5, facing North, 10 beepers
        ps = PinSetter(1, 5, North, 17, fill='green', outline='blue')
        hv = Harvester(1, 5, North, 0, fill='blue', outline='green')
        #Wirte the instructions for your robot to set the pins:
        ps.setPins()
        hv.colPins()
# Important epilogue: keep in all karel programs    
if __name__ == '__main__':
        window().run(task)
