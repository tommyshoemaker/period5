#
# Using Classes and Methods Example
# 
#



from tkinter import *
import time
import random
from MyTkClasses2019 import *
# The  task block
tk = Tk()
#TO DO:  Create a canvas that is big enough for your name to fit:
canvas = Canvas(tk, width = 800, height = 400)
#TO DO:  "pack" the canvas - shows it with dimensions specified
canvas.pack()
#Create the variables that will hold the PhotoImages for each of your letters:
imageM = PhotoImage(file = "Pics/Letters/letterM.gif")
appleLogoImage = PhotoImage(file = "Pics/applelogo.gif")
#background
canvas.create_rectangle(0, 0, 800, 400, fill = "blue", outline = "")
#Create a sprite called mySprite on the canvas at 100, 50 with imageM

mySprite = Sprite(canvas, 100, 0, imageM)
appleLogo = Sprite(canvas, 100, 0, appleLogoImage)

#Add the code animate your letters in some way inside the while 1 loop.
while 1:
   #Make sure your code inside the while loop is indented to this level.
   #Make mySprite move down
   mySprite.velocityY(1)
   #Make the sprite move to the right also:
   mySprite.velocityX(1)
   canvas.create_rectangle(320, 190, 450, 210, fill = "blue", outline = "")
   canvas.create_text(400, 200, text = ("x:", mySprite.getX()), fill = "#ffffff", font = ("Times", 25))
   #Make the sprite move up when it reaches the bottom edge:
   #Hint: Use an if statement with getY method
   canvas.bind_all("<KeyPress-w>", appleLogo.key_control)
   canvas.bind_all("<KeyPress-a>", appleLogo.key_control)
   canvas.bind_all("<KeyPress-s>", appleLogo.key_control)
   canvas.bind_all("<KeyPress-d>", appleLogo.key_control)
   #Refresh the screen
   tk.update()
