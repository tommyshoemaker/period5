from tkinter import *
import time
# The Karel task block  

tk = Tk()

#TO DO:  Create a canvas that is 500 px wide and 900 px high:
canvas = Canvas(tk,width=500,height=500)
#TO DO:  "pack" the canvas - shows it with dimensions specified
canvas.pack()
#TO DO: Create  a diagonal purple line that starts at x1,y1 = 5,5 and ends on
#       x2,y2 = 20,5
canvas.create_line(5,5,20,5,fill="purple")
#TO DO: Create a rectangle with the following coordinates:
#       Top left corner (x1,y1): 10,10 Bottom right corner(x2,y2): 50,100
#       The rectangle should have a blue outline and be filled with yellow
canvas.create_rectangle(10,10,50,100,fill="yellow",outline="blue")
#TO DO: Create a rectangle with the opposite dimensions of the above rectangle.
#       the top left corner should start at 100,100
#       The rectangle should have a red outline and be filled with black
canvas.create_rectangle(100,100,190,140,fill="black",outline="red")
#TO DO: Create a square with top corner at 100,300 with sides of 75 pixels.
#       Fill the square with green:
canvas.create_rectangle(100,300,175,375,fill="green",outline="")
#TO DO: Create a triangle with a vertex at 300,300
#       Fill the triangle with gray:
canvas.create_polygon(300,300,200,400,400,400,fill="#696969")
#TO DO: Create an oval that fits inside a rectangle at x1,y1,x2,y2 = 60,50,80,100
#       Fill it with any color you want.
canvas.create_rectangle(60,50,80,10,fill="#fff000")
canvas.create_arc(60,50,80,10,fill="#325325",outline="",extent=359.999999999)
#TO DO: Create  a semi circle with a radius of 100 pixels:
canvas.create_arc(300,200,200,300,extent=180,fill="turquoise",outline="")
#TO DO: Create  a  circle with a radius of 150 pixels. Place it anywhere open
#       in your canvas:
canvas.create_arc(250,350,400,500,extent=359.999999999,fill="black",outline="")
#TO DO: Create a variable that will hold a gif image that you have saved
#       in a folder called pics INSIDE your Python 1 folder (get a gif image
#       online first and save it there), call it pic:
sb2 = PhotoImage(file="sb2gif.gif")
#TO DO: Create the image on your canvas at x1,y1 = 10,200 and display your gif
canvas.create_image(250,200,image=sb2)
#Place the next items towards the top right corner of the canvas:
#TO DO: Create text with your Last, First name
canvas.create_text(350,100,text="Tommy Shoemaker",font=("Futura",30),fill="white")
#TO DO: Create text with that says "Period 1". Make it a different font and size:
canvas.create_text(350,150,text="Period 5",font=("Roboto",20),fill="white")
#TO DO: Create text with that with today's date. Make it a different font and size:
canvas.create_text(350,200,text="March 11, 2019",font=("Helvetica",20),fill="white")
