#
# prospector.py
#
# Important prasfamble: keep in all karel programs
from karel.robota import *
from Shoemaker_Thomas_MyClasses import *               
# The Karel task block  
def task():
    world.readWorld("mine.kwld")
    #Make sure you add the Prospector class to MyRobotClasses as indicated on the agenda.
    #create a Prospector Robot with your name starting on the St. and Ave. indicated on the agenda.
    mrP = Prospector(1,1,North,0)
    #have the Prospector findNextDirection (you must define that method in MyRobotClasses first.
    mrP.findNextDirection()

    bob = Prospector(1,3,North,0)
    bob.findNextDirection()
    bob.findNextDirection()

    mary= Prospector(1,5,South,0)
    mary.findNextDirection()

    joe = Prospector(1,7,South,0)
    joe.findNextDirection()

    ana = Prospector(3,1,East,0)
    ana.findNextDirection()

    juan = Prospector(3,3,East,0)
    juan.findNextDirection()
    
    minHo = Prospector(3,5,West,0)
    minHo.findNextDirection()
    
    felicia = Prospector(3,7,West,0)
    felicia.findNextDirection()
# Important epilogue: keep in all karel programs
if __name__ == '__main__':
        window().run(task)
