#tkinter Counter

from tkinter import *
import time
import random
          
#The task block  

tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()

#Crete a Variable Called COunter and Set its Value to 0:
Counter = 0

#Create Variables for x1 at 10,200:
x1 = 10
y1 = 200

#Create Variables for xSquare and ySquare at 200,300:
xSquare = 200
ySquare = 200

#Create a Variable Called z Starting at 50:
z = 50

#Create a variable With the Name of Your Image and asign a PhotoImage to it:
Sun = PhotoImage(file="pics/Sun.gif")

#Create Variables Called xImage With a Value of 10 and yImage With a Value of 300
xImage = 10
yImage = 300

while 1:
    #Create Background:
    canvas.create_rectangle(0,0,450,450,fill="lightblue",outline="")

    #Increase Counter By 1 Using the Counter Pattern:
    Counter = Counter + 1

    #Display the Value of the Variables:
    canvas.create_text(200,25,text=("Counter:",Counter),fill="black",font=("arial",30))
    canvas.create_text(200,50,text=("z:",z),fill="black",font=("arial",30))
    canvas.create_text(200,75,text=("x1:",x1),fill="black",font=("arial",30))
    canvas.create_text(200,100,text=("y1:",y1),fill="black",font=("arial",30))
    canvas.create_text(200,125,text=("xSquare:",xSquare),fill="black",font=("arial",30))
    canvas.create_text(200,150,text=("ySquare:",ySquare),fill="black",font=("arial",30))
    

    #Increase x1 By 1 Using the Counter Pattern:
    x1 = x1 + 1

    #Increase y1 By 1 Using the Countre Pattern:
    y1 = y1 + 1
    
    canvas.create_oval(x1,y1,x1+20,y1+20,fill="#696969",outline="")

    #Create a Square at xSquare,ySquare With a Width of 30;
    canvas.create_rectangle(xSquare,ySquare,xSquare+30,ySquare+30,fill="#696969",outline="")

    #Make the Square Move Down Using the Counter pattern:
    ySquare = ySquare + 1

    #Place Your Image On the Canvas at xInage, yImage:
    
    
    tk.update()
    time.sleep(0.001)














