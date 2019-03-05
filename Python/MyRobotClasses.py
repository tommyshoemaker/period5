#
# My Robot Classes
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
from StrategyClasses import *
from karel.robota import Robot


#------------------------------------------------------------
#TO DO: Create a class called Turner that inherits from UrRobot
#       This class should have the following functions:
#       1) turnRight  (we have written this one before)
#       2) turnAround - should make the robot do a 180 (face opposite direction).
#       3) backUp - should make the robot move back 1 step and remain facing
#                   in the same direction
#       4) slideLeft - should make the robot move left and remain facing in same
#                       direction
#       5) slideRight - should make the robot move right and remain facing in same
#                       direction





#------------------------------------------------------------
#TO DO: Create a class called Climber that inherits from Turner
#       Inside the class, create a method called climbStep.
#       Assume that the robot is facing North, and that one step is
#       one street high by one avenue long.
#       Robot must end up facing North after it climbs the step
