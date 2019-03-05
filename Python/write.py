# Important preamble: keep in all karel programs
from karel.robota import East
from karel.robota import West
from karel.robota import North
from karel.robota import South
from karel.robota import infinity
from karel.robota import window
from karel.robota import world
from karel.robota import UrRobot
from Shoemaker_Thomas_MyClasses import Writer

# The Karel task block  
def task():
        #Commands to control the "world"
        size = int(54)
        world.setSize(size, size)               # set the size of the visible world
        world.setDelay(0)                # set simulation speed. 0-fastest, 100-slowest
        
        
        #Write the code to test the methods of Dancer Class with different robots
        sb2 = Writer(1,1,East, infinity)
        #For newLine(a), a = the number of letters in the line before it.
        sb2.s()
        sb2.h()
        sb2.o()
        sb2.e()
        sb2.m()
        sb2.a()
        sb2.k()
        sb2.e()
        sb2.r()
        sb2.newLine(9)
        sb2.t()
        sb2.o()
        sb2.m()
        sb2.m()
        sb2.y()
 
# Important epilogue: keep in all karel programs    
if __name__ == '__main__':
        window().run(task)
    
