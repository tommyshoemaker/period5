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
firstmx = 450
firstmy = 100
secondmx = 625
secondmy = 100
yx = 800
yy = 100
#Create the variables that will hold the PhotoImages for each of your letters:
imageT = PhotoImage(file = "Pics/Letters/Letter_T.gif")
imageO = PhotoImage(file = "Pics/Letters/Letter_O.gif")
imageM1 = PhotoImage(file = "Pics/Letters/Letter_M_1.gif")
imageM2 = PhotoImage(file = "Pics/Letters/Letter_M_2.gif")
imageY = PhotoImage(file = "Pics/Letters/Letter_Y.gif")
#Place the your letter images at their starting places on the canvas:
letterT = canvas.create_image(tx, ty, image = imageT)
letterO = canvas.create_image(ox, oy, image = imageO)
letterM1 = canvas.create_image(firstmx, firstmy, image = imageM1)
letterM2 = canvas.create_image(secondmx, secondmy, image = imageM2)
letterY = canvas.create_image(yx, yy, image = imageY)
#Add some shapes to enhance your program:

#Add the code animate your letters in some way inside the while 1 loop.
#You should have all the following animations: 1) random movement,
#  2)up and down movement, 3)left and right movement, 4) diagonal movement.
# No letter should go off the screen and not come back.  Make a letter "bounce".
sign = 1
while 1:
   #Make sure your code inside the while loop is indented to this level.
   #Random coords for letterT
   tx = random.randint(100, 150)
   ty = random.randint(100, 150)
   #Letter O going up and down
   if oy == 0:
      sign = 1
   elif oy == 150:
      sign = 0
   if sign == 0:
      oy -= 1
      firstmx -= 1
      secondmx -= 1
      secondmy -= 1
   elif sign == 1:
      oy += 1
      firstmx += 1
      secondmx += 1
      secondmy += 1
   ycoords = [ty, oy, firstmy, secondmy]
   randomy = random.choice(ycoords)
   yx = random.randint(775, 825)
   yy = randomy
   #Coords
   canvas.coords(letterT, tx, ty)
   canvas.coords(letterO, ox, oy)
   canvas.coords(letterM1, firstmx, firstmy)
   canvas.coords(letterM2, secondmx, secondmy)
   canvas.coords(letterY, yx, yy)
   #Refresh the screen
   tk.update()
   time.sleep(0.05)
