#Frogger Game
from tkinter import *
import time
import random
from froggerClassesSt import *
#The Task Block  

tk = Tk()
canvas = Canvas(tk,width=500,height=400)
canvas.pack()

#Create the variables that will hold the PhotoImages for each sprites
#(frog, mushroom, and fly):
frogImage = PhotoImage (file="pics/frog.gif")
mushroomImage = PhotoImage (file="pics/mushroom.gif")
flyImage = PhotoImage (file="pics/fly.gif")
deadFrogImage = PhotoImage(file="pics/dead-frog.gif")

#background:
canvas.create_rectangle(0,0,500,95,fill="Tan",outline="")
canvas.create_rectangle(0,95,500,200,fill="#00aef0",outline="")
canvas.create_rectangle(0,200,500,315,fill="Black",outline="")
canvas.create_rectangle(0,315,500,500,fill="#325325",outline="")

#Yellow Stripes
canvas.create_rectangle(10,250,90,260,fill="Yellow",outline="")
canvas.create_rectangle(110,250,500,260,fill="Yellow",outline="")
canvas.create_rectangle(0,250,500,260,fill="Yellow",outline="")
canvas.create_rectangle(0,250,500,260,fill="Yellow",outline="")
canvas.create_rectangle(0,250,500,260,fill="Yellow",outline="")

#TO DO:Create a variable called score and set its value to 0
score = 0
#TO DO:Create a variable called lives and set its value to 3
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
alive = True
flySign = -1
mushroomSign = -1
while alive:
   #the method draw controls the motions of the sprite.
   #Note that PlayerSprites and regular Sprites have different draw methods -
   #this is called polymorphysm.
   frog.draw()
   mushroom.draw(mushroomSign,5)
   fly.draw(flySign, 7)
   if mushroom.x <= 0:
      mushroomSign = 1
   if mushroom.x >= 500:
      mushroomSign = -1
   if fly.x <= 0:
      flySign = 1
   if fly.x >= 500:
      flySign = -1
   #If the frog touches the mushroom, the following should happen:
   # 1) mushroom resets to the right of the screen
   # 2) Use the counter pattern to decrease lives by 1
   # 3) Display Lives
   if frog.isTouching(mushroom):
      mushroomSign = -1
      mushroom.x = 510
      lives -= 1
      if lives <= 0:
         alive = False
      canvas.create_rectangle(100,0,200,40,fill="#00adff",outline="")
      canvas.create_text( 150,25,text= ("Lives:",lives),fill="white", font=("Arial",20))
   #If the frog touches the fly, the following should happen:
   # 1) fly resets to the right of the screen and a random y position
   # 2) Use the counter pattern to increase score  by 1
   # 3) Display score again
   if frog.isTouching(fly):
      flySign = -1
      fly.x = 510
      score += 1
      canvas.create_rectangle(0, 0, 110, 40, fill="#00adff", outline="")
      canvas.create_text(50, 25, text=("Score:", score), fill="white", font=("Arial", 20))

   #Refresh the screen
   tk.update_idletasks()
   tk.update()
   time.sleep(0.005)
canvas.create_rectangle(-50, -50, 550, 450, fill="black")
canvas.create_text(252, 200, text=("GAME OVER!"), fill="white", font=("Century Gothic", 78))
canvas.create_image(frog.x, frog.y, image=deadFrogImage)