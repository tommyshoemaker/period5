#
# tkinter Motion by Changing Coordinates
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

#Create a variable that holds holds a PhotoImage for the grid
gridImage = PhotoImage(file="pics/tkGrid.gif")

#Place the grid image on the canvas at 250,250:
canvas.create_image(250,250,image=gridImage)


x1 = 100
y1 = 200
x2 = x1 + 50
y2 = y1 + 50
#Create xImage with a value of 50, and yImage with a value of 450
xImage = 50
yImage = 450

#Create a variable that holds a PhotoImage
sharkImageForward = PhotoImage(file="pics/sharkforwards.gif")
sharkImageBackward = PhotoImage(file="pics/sharkbackwards.gif")

ball = canvas.create_oval(x1, y1, x2, y2, fill="#000000", outline="")

#Place the image on the canvas at xImage, yImage:
shark = canvas.create_image(xImage,yImage,image=sharkImageForward)
while True:
   x1 += 0.5
   x2 = x1 + 50
   y2 = y1 + 50
   canvas.coords(ball, x1, y1, x2, y2)
   while not xImage == 500:
      xImage = xImage + 0.5
      yImage = yImage - 0.5
      canvas.coords(shark,xImage,yImage)
      tk.update()
   while not xImage == 0:
      xImage = xImage - 0.5
      yImage = yImage + 0.5
      canvas.coords(shark,xImage,yImage)
      tk.update()
   #Refresh the screen
   tk.update()
   
   




    



    
