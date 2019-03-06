#
# origin.py
#


# Important preamble: keep in all karel programs
from karel.robota import *
from Shoemaker_Thomas_MyClasses import *
import random              
# The Karel task block  
def task():
    street = random.randint(1,15)
    avenue = random.randint(1,15)
    directionNumber = random.randint(1,4)
    if directionNumber == 1:
        direction = North
    elif directionNumber == 2:
        direction = East
    elif directionNumber == 3:
        direction = South
    elif directionNumber == 4:
        direction = West
    world.setSize(15,15)
    world.readWorld("origin2.kwld") 
    
    #create a Prospector Robot with your name starting on  St. 12 and Ave. 11
    #After you get program working, test with several different St. and Ave
    #combinations
    sb2 = Prospector(street, avenue, direction, 0, fill='green', outline='blue')
    #TO DO: Write the instruction for your Prospector to go to the origin
    sb2.goToOrigin()

# Important epilogue: keep in all karel programs
if __name__ == '__main__':
        window().run(task)
    
