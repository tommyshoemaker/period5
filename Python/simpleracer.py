from karel.robota import *
from Shoemaker_Thomas_MyClasses import * ##Change this to your file name      
        
def task() :
    world.readWorld("hurdles.kwld")
    world.setDelay(30)
    #TO DO: Create a Racer Robot with your name starting on
    #Street 1, Avenue 1, facing East, with no beepers:
    sb2 = Racer(1, 1, East, 0, fill='green', outline='blue')
    #TO DO:  Write the instructions for your robot to complete the race
    sb2.run()
if __name__ == '__main__' :
    world.setDelay(30)
    window().run(task)
