# Important preamble: keep in all karel programs
from karel.robota import East
from karel.robota import West
from karel.robota import North
from karel.robota import South
from karel.robota import infinity
from karel.robota import window
from karel.robota import world
from karel.robota import UrRobot
#change the name of this file to your file name:
from Shoemaker_Thomas_MyClasses import Dancer
# The Karel task block  
def task():
        #Commands to control the "world"
        world.readWorld("danceWorld.kwld")
        #Set the size of the visible world
        world.setSize(10,10)
        #Set simulation speed. 0-fastest, 100-slowest
        world.setDelay(20)
        #Start a Dancer at Street 7, Avenue 3, facing North, with 0 beepers:
        dancer1 = Dancer(7,3,North,0)
        #Write the code for the dancer to perform the first dance
        dancer1.danceSteps1()
        #Start 2nd Dancer at Street 7, Avenue 7, facing North, with 0 beepers:
        dancer2 = Dancer(7,7,North,0)
        #Write the code for the second dancer to perform the second dance
        dancer2.danceSteps2()
# Important epilogue: keep in all karel programs    
if __name__ == '__main__':
      window().run(task)
