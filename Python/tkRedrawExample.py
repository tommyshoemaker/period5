#
# tkinter Motion by Redrawing
#



from tkinter import *
import time
import random

                
# The  task block  

tk = Tk()

#TO DO:  Create a canvas that is 500 px wide and 500 px high:
canvas = Canvas(tk,width=500,height=500)

#TO DO:  "pack" the canvas - shows it with dimensions specified
canvas.pack()

#Create xImage with a value of 50, and yImage with a value of 450
xImage = 50
yImage = 450

#Create a variable that holds a PhotoImage for a shark
sharkImage = PhotoImage(file="pics/shark.gif")

#Create a variable that holds holds a PhotoImage for the grid
gridImage = PhotoImage(file="pics/tkGrid.gif")


while 1:
   #Background
   canvas.create_rectangle(-50, -50, 550, 550, fill="#ffffff", outline="")
   #Place the grid image on the canvas at 250,250:
   canvas.create_image(250,250,image=gridImage)
   
   #Place the shark image on the canvas at xImage, yImage:
   canvas.create_image(xImage,yImage,image=sharkImage)
 
   #Use the counter pattern (on two variables) so that the image moves up and to the right:
   xImage = xImage + 2
   yImage = yImage - 2
   
   #Refresh the screen
   tk.update()
   




    



    
