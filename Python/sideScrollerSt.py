#
# Side Scroller Game
# 
#



from tkinter import *
import time
import random
from ScrollerClasses import *

                
# The  task block  

tk = Tk()

#TO DO:  Create a 500 by 400 canvas t:
canvas = Canvas(tk,width=500,height=400)

#TO DO:  "pack" the canvas - shows it with dimensions specified
canvas.pack()



#Create the variables that will hold the PhotoImages for each sprites
#(frog, mushroom, and fly):

frogImage = PhotoImage (file="pics/frog.gif")
mushroomImage = PhotoImage (file="pics/mushroom.gif")
flyImage = PhotoImage (file="pics/fly.gif")


#background: bottom 5th should be different than the rest (such as
#grass bottom and rest sky:

canvas.create_rectangle(0,0,500,350,fill="blue",outline="")
canvas.create_rectangle(0,345,500,400,fill="green",outline="")


#Create a variable called score and set its value to 0
score = 0

#Create a variable called lives and set its value to 3
lives = 3




#Create the  frog PlayerSprites:
#frog should start in the horizontal middle, sitting on grass (or whatever
#your bottom 5th is.
frog = PlayerSprite(canvas,250,325,frogImage)

#Create the regular Sprites:
#Mushroom should start all the way to the right and also
#on the grass.  Fly should start all the way to the left at a random y
mushroom = Sprite(canvas, 510, 325, mushroomImage)
yFly = random.randint(180,300)
fly = Sprite(canvas, 530, yFly, flyImage)

#Display the value of score and lives toward the top of the canvas:
canvas.create_text( 40,25,text= ("Score:",score),fill="white", font=("Times",15) )
canvas.create_text( 100,25,text= ("Lives:",lives),fill="white", font=("Times",15) )

while 1:

   

   #the method draw controls the motions of the sprite.
   #Note that PlayerSprites and regular Sprites have different draw methods -
   #this is called polymorphysm.
   frog.draw()
   mushroom.draw()
   fly.draw()

   #If the frog touches the mushroom, the following should happen:
   # 1) mushroom resets to the right of the screen
   # 2) Use the counter pattern to decrease lives by 1
   # 3) Display Lives
   if frog.isTouching(mushroom):
      mushroom.x = 510
      lives = lives - 1
      canvas.create_rectangle(70,15,165,35,fill="red",outline="")
      canvas.create_text( 100,25,text= ("Lives:",lives),fill="white", font=("Times",15) )

   #If the frog touches the fly, the following should happen:
   # 1) fly resets to the right of the screen and a random y position
   # 2) Use the counter pattern to increase score  by 1
   # 3) Display score again
   if frog.isTouching(fly):
      fly.x = 510
      fly.y = random.randint(180,300)
      score = score + 1
      canvas.create_rectangle(10,15,69,35,fill="red",outline="")
      canvas.create_text( 40,25,text= ("Score",score),fill="white", font=("Times",15) )
   

   #Refresh the screen
   tk.update_idletasks()
   tk.update()
   time.sleep(.05)
   




    



    
