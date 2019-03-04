#
# treasureHunt.py
#


# Important preamble: keep in all karel programs
from karel.robota import *
#Change the file name below to your file name:
from Shoemaker_Thomas_MyClasses import *               
# The Karel task block  
def task():
    world.readWorld("treasure.kwld")  #change to treasure2.kwld after it works with treasure.kwld
    world.setSize(15,15)
    #create a Prospector Robot with your name starting on  St. 2 and Ave. 2, facing East.
    #to test treasure.kwld -
    #Start robot on St. 1, Ave. 1, when using treasure2.kwld
    sb2 = TreasureHunter(2, 2, North, 0)
    #Write the instruction for your robot to hunt the treasure
    sb2.hunt()
# Important epilogue: keep in all karel programs
if __name__ == '__main__':
        window().run(task)
    
