#
# tkinter Counter Pattern Examples
#



from tkinter import *
import time
import random

                
# The  task block  

tk = Tk()

#TO DO:  Create a canvas that is 500 px wide and 500 px high:
canvas = Canvas(tk, width=500, height=500)
#TO DO:  "pack" the canvas - shows it with dimensions specified
canvas.pack()
#Create the following variables:  xOval with a value of 500, yOval with a value of 10,
#xRect with a value of 50, and yRect with a value of 400
xOval = 500
yOval = 10

xRectangle = 50
yRectangle = 400
#Create a variable that holds a PhotoImage
applelogo = PhotoImage(file="applelogo.gif")
#Create xImage with a value of 50, and yImage with a value of 450
xImage = 50
yImage = 450
while True:
   #Create a Background that covers the whole canvas:
   canvas.create_rectangle(-50, -50, 550, 550, fill="#ffffff", outline="")
   #Display, on separate lines starting at 200,200, the value xOval, yOval in the format
   #xOval: value:
   xOvalValue = "xOval:", xOval
   yOvalValue = "yOval:", yOval
   #xOval2 and yOval2
   xOval2 = xOval + 30
   yOval2 = yOval + 30
   
   canvas.create_text(200, 200, text=xOvalValue, font=("Futura", 30), fill="#696969")
   canvas.create_text(200, 250, text=yOvalValue, font=("Futura", 30), fill="#abcdef")
   #Create a circle at xOval,yOval with a diameter of 30 px:
   canvas.create_oval(xOval, yOval, xOval2, yOval2, fill="#da9a5b", outline="")
   #Use the counter pattern so that the circle above, moves to the left:
   xOval -= 1
   #Create a square at xRect, yRect with sides of 25 px:
   xRectangle2 = xRectangle + 25
   yRectangle2 = yRectangle + 25
   canvas.create_rectangle(xRectangle, yRectangle, xRectangle2, yRectangle2, fill="#15ba55", outline="")
   #Use the counter pattern so that the square above, moves up:
   yRectangle -= 1
   #Place the image (for the PhotoImage you created before the while 1 loop) at
   # xImage, yImage:
   canvas.create_image(xImage, yImage, image=applelogo)
   #Use the counter pattern (on two variables) so that the image moves up and to the right:
   xImage += 1
   yImage -= 1
   tk.update()
   #time.sleep(.05)
   




    



    
