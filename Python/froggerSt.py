#Frogger Game
from tkinter import *
import tkinter
import time
import random
from froggerClassesSt import *
#The Task Block  

tk = Tk()
canvas = Canvas(tk,width=500,height=400)
canvas.pack()

#Create the variables that will hold the PhotoImages for each sprites
frogImage = PhotoImage (file="pics/frog_froggerGame.gif")
deadFrogImage = PhotoImage(file="pics/dead-frog.gif")
redCarImage = PhotoImage (file="pics/carRed.gif")
blueCarImage = PhotoImage (file="pics/carBlue.gif")
redCarImage2 = PhotoImage (file="pics/carRed.gif")
blueCarImage2 = PhotoImage (file="pics/carBlue.gif")

#Background
canvas.create_rectangle(0,0,500,95,fill="Tan",outline="")
canvas.create_rectangle(0,95,500,200,fill="#00aef0",outline="")
canvas.create_rectangle(0,200,500,315,fill="Black",outline="")
canvas.create_rectangle(0,315,500,500,fill="#325325",outline="")

#Yellow Stripes
canvas.create_rectangle(10,250,90,260,fill="Yellow",outline="")
canvas.create_rectangle(110,250,190,260,fill="Yellow",outline="")
canvas.create_rectangle(210,250,290,260,fill="Yellow",outline="")
canvas.create_rectangle(310,250,390,260,fill="Yellow",outline="")
canvas.create_rectangle(410,250,490,260,fill="Yellow",outline="")

score = 0
lives = 3

frog = PlayerSprite(canvas,250,335,frogImage)
redCar = Sprite(canvas,0,285,redCarImage)
redCar2 = Sprite(canvas,-150,285,redCarImage2)
blueCar = Sprite(canvas,500,225,blueCarImage)
blueCar2 = Sprite(canvas,625,225,blueCarImage2)

#TO DO:
#Display the value of score and lives toward the top of the canvas:
canvas.create_text(50,25,text= ("Score:",score),fill="white", font=("Arial",20))
canvas.create_text(150,25,text= ("Lives:",lives),fill="white", font=("Arial",20))
alive = True
flySign = -1
mushroomSign = -1

while alive:
   if redCar.x == 550:
      redCar.x = -50
   if redCar2.x == 550:
      redCar2.x = -50
   if blueCar.x == -50:
      blueCar.x = 550
   if blueCar2.x == -50:
      blueCar2.x = 550
   frog.draw()
   redCar.draw(1, 5)
   redCar2.draw(1, 5)
   blueCar.draw(-1,7)
   blueCar2.draw(-1,7)

   tk.update_idletasks()
   tk.update()
   time.sleep(0.05)
canvas.create_rectangle(-50, -50, 550, 450, fill="black")
canvas.create_text(252, 200, text=("GAME OVER!"), fill="white", font=("Century Gothic", 78))
canvas.create_image(frog.x, frog.y, image=deadFrogImage)
