#Add to all tKinter programs:
from tkinter import *
import time
import random

#Canvas() height and width changed as needed
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

hexred = "#ff0000"
hexgreen = "#00ff00"
hexblue = "#0000ff"
student = PhotoImage(file="computer.gif")
#Code part:

while 1:
    picX = random.randint(1,400)
    r = lambda: random.randint(0,255)
    hexcolor = '#%02X%02X%02X' % (r(),r(),r())
    x1 = random.randint(0,400)
    y1 = random.randint(0,400)
    x2 = x1 + 100
    y2 = y1 + 100
    canvas.create_rectangle(0,0,450,450,fill="black",outline="")
    canvas.create_oval(x1,y1,x2,y2,fill=hexcolor,outline="")
    canvas.create_image(picX,200,image=student)
    tk.update()
    time.sleep(0.5)
