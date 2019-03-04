#
# prospector.py
#
# Important preamble: keep in all karel programs
from karel.robota import *
from Shoemaker_Thomas_MyClasses import *






          
                
# The Karel task block  
def task():

    world.readWorld("mine3.kwld")


    #Have each robot findNextDirection after its creation
    gus = Prospector(1,1,North,0)
    gus.findNextDirection()
    
    bob = Prospector(1,2,South,0)
    bob.findNextDirection()
    
    mary = Prospector(1,3,East,0)
    mary.findNextDirection()
    
    joe = Prospector(1,4,West,0)
    joe.findNextDirection()
    
    ana = Prospector(2,1,North,0)
    ana.findNextDirection()
    
    juan = Prospector(2,2,South,0)
    juan.findNextDirection()
    
    minHo = Prospector(2,3,East,0)
    minHo.findNextDirection()
    
    felicia = Prospector(2,4,West,0)
    felicia.findNextDirection()
    
    ana = Prospector(3,1,North,0)
    ana.findNextDirection()
    
    juan = Prospector(3,2,South,0)
    juan.findNextDirection()
    
    minHo = Prospector(3,3,East,0)
    minHo.findNextDirection()
    
    felicia = Prospector(3,4,West,0)
    felicia.findNextDirection()
    
    ana = Prospector(4,1,North,0)
    ana.findNextDirection()
    
    juan = Prospector(4,2,South,0)
    juan.findNextDirection()
    
    minHo = Prospector(4,3,East,0)
    minHo.findNextDirection()
    
    felicia = Prospector(4,4,West,0)
    felicia.findNextDirection()
    
    bob = Prospector(5,2,North,0)
    bob.findNextDirection()
# Important epilogue: keep in all karel programs
if __name__ == '__main__':
        window().run(task)
    
