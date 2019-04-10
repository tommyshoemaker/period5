#
# Name Animation:
# 

from tkinter import *
import time
import random
                
# The  task block  

tk = Tk()

#TO DO:  Create a canvas that is big enough for your name to fit:
canvas = Canvas(tk, width = 1000, height = 400)
#TO DO:  "pack" the canvas - shows it with dimensions specified
canvas.pack()
#Create different x and y coordinates for each letter of your name:
tx = 100
ty = 100
ox = 275
oy = 100
firstmx = 350
firstmy = 100
secondmx = 525
secondmy = 100
yx = 700
yy = 100
#Create the variables that will hold the PhotoImages for each of your letters:
letterT = PhotoImage(tx, ty, file="Pics/Letters/Letter_T.gif")
letterO = PhotoImage(ox, oy, file="Pics/Letters/Letter_O.gif")
letterM1 = PhotoImage(firstmx, firstmy, file="Pics/Letters/Letter_M_1.gif")
letterM2 = PhotoImage(secondmx, secondmy, file="Pics/Letters/Letter_M_1.gif")
letterY = PhotoImage(yx, yy, file="Pics/Letters/Letter_Y.gif")
#Place the your letter images at their starting places on the canvas:

#Add some shapes to enhance your program:

#Add the code animate your letters in some way inside the while 1 loop.
#You should have all the following animations: 1) random movement,
#  2)up and down movement, 3)left and right movement, 4) diagonal movement.
# No letter should go off the screen and not come back.  Make a letter "bounce".
while 1:
   #Make sure your code inside the while loop is indented to this level.
   #Refresh the screen
   tk.update()
   time.sleep(.05)
   




    



    
