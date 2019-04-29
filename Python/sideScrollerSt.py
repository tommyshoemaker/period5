#
# Side Scroller Game
# 
#



from tkinter import *
import time
import random
from ScrollerClassesSt import *

                
# The  task block  

tk = Tk()

#TO DO:  Create a 500 by 400 canvas t:
canvas = Canvas(tk,width=500,height=400)
#TO DO:  "pack" the canvas - shows it with dimensions specified
canvas.pack()

#TO DO:
#Create the variables that will hold the PhotoImages for each sprites
#(frog, mushroom, and fly):
frogImage = PhotoImage (file="pics/frog.gif")
mushroomImage = PhotoImage (file="pics/mushroom.gif")
flyImage = PhotoImage (file="pics/fly.gif")
#TO DO:
#background: bottom 5th should be different than the rest (such as
#grass bottom and rest sky:
canvas.create_rectangle(0,0,500,350,fill="#00adff",outline="")
canvas.create_rectangle(0,350,500,400,fill="#325325",outline="")
##TO DO:Create a variable called score and set its value to 0
score = 0
##TO DO:Create a variable called lives and set its value to 3
lives = 3
#TO DO:
#Create the  frog PlayerSprites:
#frog should start in the horizontal middle, sitting on grass (or whatever
#your bottom 5th is.
frog = PlayerSprite(canvas,250,325,frogImage)
#TO DO:
#Create the regular Sprites:
#Mushroom should start all the way to the right and also
#on the grass.  Fly should start all the way to the left at a random y
mushroom = Sprite(canvas, 510, 325, mushroomImage)
flyY = random.randint(180,300)
fly = Sprite(canvas, 530, flyY, flyImage)
#TO DO:
#Display the value of score and lives toward the top of the canvas:
canvas.create_text(50,25,text= ("Score:",score),fill="white", font=("Arial",20))
canvas.create_text(150,25,text= ("Lives:",lives),fill="white", font=("Arial",20))
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
      lives -= 1
      canvas.create_rectangle(110,0,200,40,fill="#00adff",outline="")
      canvas.create_text( 150,25,text= ("Lives:",lives),fill="white", font=("Arial",20))

   #If the frog touches the fly, the following should happen:
   # 1) fly resets to the right of the screen and a random y position
   # 2) Use the counter pattern to increase score  by 1
   # 3) Display score again
   if frog.isTouching(fly):
      fly.x = 510
      score += 1
      canvas.create_rectangle(0, 0, 110, 40, fill="#00adff", outline="")
      canvas.create_text(50, 25, text=("Score:", score), fill="white", font=("Arial", 20))

   #Refresh the screen
   tk.update_idletasks()
   tk.update()
   time.sleep(.05)
   




    



    
