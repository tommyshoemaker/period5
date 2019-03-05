#
# prospector.py
#


# Important preamble: keep in all karel programs
from karel.robota import *
#Change the file name below to your file name:
from Shoemaker_Thomas_MyClasses import *






          
                
# The Karel task block  
def task():

    world.readWorld("carpet.kwld")
    world.setDelay(50)
    #Make sure you add the CarpetLayer class to MyRobotClasses as indicated on the agenda.
    #create a CarpetLayer Robot with your name starting on the St. and Ave. indicated on the
    sb2 = CarpetLayer(2, 1, North, infinity, fill="green", outline="blue")
    #Write the instruction for your robot to carpet a block:
    #sb2.layCarpet()
    while sb2.carpetBlock():
        pass

# Important epilogue: keep in all karel programs
if __name__ == '__main__':
        window().run(task)
    
