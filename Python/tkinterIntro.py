#
# tkinter Intro
#



from tkinter import *
import time         
                
# The Karel task block  

tk = Tk()
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
pic1 = PhotoImage(file="Pics/computer.gif")
canvas.create_image(200,200,image=pic1)
#TO DO: Create  a Red line that starts at x1,y1 = 5,5 and ends at x2,y2=20,20
canvas.create_line(5,5,200,200,fill="red")

#TO DO: Create a rectangle with the following coordinates:
#       Top left corner (x1,y1): 10,10 Bottom right corner(x2,y2): 100,50
canvas.create_rectangle(10,10,100,50,fill="navyblue",outline="darkgreen")

#TO DO: Create a square with top corner at 200,300 with sides of 50 pixels:
canvas.create_rectangle(200,300,250,350,fill="navyblue",outline="darkgreen")

#TO DO: Create an arc that fits inside a rectangle at x1,y1,x2,y2 = 60,50,80,100
#       The arc should measure 180 degrees:
canvas.create_arc(200,50,380,290,extent=90,fill="turquoise",outline="")

#TO DO: Create an a quarter circle with a radius of 100 pixels:

canvas.create_arc(350,350,550,550,extent=359.99999999,fill="#696969", outline="")
#TO DO: Create an a  circle with a radius of 50 pixels:
canvas.move(6,100,200)
#TO DO: Make the above circle move 100 pixels to the right:


#TO DO: Create a variable that will hold a gif image that you have saved
#       in a folder called pics INSIDE your Python 1 folder, call it pic:

#TO DO: Create the image on your canvas at x1,y1 = 10,200


#TO DO: Create text with your first and last name
canvas.create_text(100,400,text="The quick brown fox jumps over the lazy dog.",font=("Roboto",30))




    
