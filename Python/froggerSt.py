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
log1Image = PhotoImage (file="pics/log.gif")
log2Image = PhotoImage (file="pics/log.gif")
log3Image = PhotoImage (file="pics/log.gif")


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

redCar = Sprite(canvas,0,285,redCarImage)
redCar2 = Sprite(canvas,-150,285,redCarImage2)
blueCar = Sprite(canvas,500,225,blueCarImage)
blueCar2 = Sprite(canvas,625,225,blueCarImage2)
log1 = Sprite(canvas,550,115,log1Image)
log2 = Sprite(canvas,-50,145,log2Image)
log3 = Sprite(canvas,600,180,log3Image)
frog = frogSprite(canvas,250,335,frogImage)

onLog = False

#TO DO:
#Display the value of score and lives toward the top of the canvas:
canvas.create_text(50,25,text= ("Score:",score),fill="white", font=("Arial",20))
canvas.create_text(150,25,text= ("Lives:",lives),fill="white", font=("Arial",20))
alive = True
flySign = -1
mushroomSign = -1

while alive:
   if redCar.x >= 550:
      redCar.x = -50
   if redCar2.x >= 550:
      redCar2.x = -50
   if blueCar.x <= -50:
      blueCar.x = 550
   if blueCar2.x <= -50:
      blueCar2.x = 550
   if log1.x <= -50:
      log1.x = 550
   if log2.x >= 550:
      log2.x = -50
   if log3.x <= -50:
      log3.x = 550
   if frog.isTouching(redCar):
      lives -= 1
      canvas.create_rectangle(100, 0, 200, 50, fill = "Tan", outline = "")
      canvas.create_text(150,25,text= ("Lives:",lives),fill="white", font=("Arial",20))
      frog.restart()
   elif frog.isTouching(redCar2):
      lives -= 1
      canvas.create_rectangle(100, 0, 200, 50, fill = "Tan", outline = "")
      canvas.create_text(150,25,text= ("Lives:",lives),fill="white", font=("Arial",20))
      frog.restart()
   elif frog.isTouching(blueCar):
      lives -= 1
      frog.restart()
   elif frog.isTouching(blueCar2):
      lives -= 1
      canvas.create_rectangle(100, 0, 200, 50, fill = "Tan", outline = "")
      canvas.create_text(150,25,text= ("Lives:",lives),fill="white", font=("Arial",20))
      frog.restart()
   elif frog.y <= 60:
      score += 1
      if lives < 3:
         lives += 1
      canvas.create_rectangle(0, 0, 200, 50, fill = "Tan", outline = "")
      canvas.create_text(50,25,text= ("Score:",score),fill="white", font=("Arial",20))
      canvas.create_text(150,25,text= ("Lives:",lives),fill="white", font=("Arial",20))
      frog.restart()

   #Is touching log? If not, reset if also on river
   if frog.isTouching(log3):
      frog.x = log3.x
      frog.velocityX(-5)
      onLog = True
   elif frog.isTouching(log2):
      frog.x = log2.x
      frog.velocityX(5)
      onLog = True
   elif frog.isTouching(log1):
      frog.x = log1.x
      frog.velocityX(-5)
      onLog = True
   else:
      onLog = False
   if not onLog:
      if (frog.y < 200 and frog.y > 95):
         lives -= 1
         canvas.create_rectangle(100, 0, 200, 50, fill = "Tan", outline = "")
         canvas.create_text(150,25,text= ("Lives:",lives),fill="white", font=("Arial",20))
         frog.restart()
         onLog = False
   #Make frog follow the log (frog.x is attached to log)
      
   if lives <= 0:
      alive = False
   log1.draw(-1, 5)
   log2.draw(1, 6)
   log3.draw(-1, 5)
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
