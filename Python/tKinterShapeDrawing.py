from tkinter import *
import time

#Add to all tKinter programs:
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

#Shapes:
#sky
canvas.create_rectangle(0,0,400,400,fill="#6dd0f7",outline="")
#snow
canvas.create_rectangle(0,200,400,400,fill="#ffffff",outline="")
#outline of head
canvas.create_arc(135,50,275,190,fill="#000000",outline="",extent="359.999")
#head
canvas.create_arc(140,55,270,185,fill="#ffffff",outline="",extent="359.999")
#outline of body
canvas.create_arc(105,180,305,380,fill="#000000",outline="",extent="359.999")
#body
canvas.create_arc(110,185,300,375,fill="#ffffff",outline="",extent="359.999")
#hat bottom
canvas.create_rectangle(130,50,280,75,fill="#000000",outline="")
#hat top
canvas.create_rectangle(180,0,230,75,fill="#000000",outline="")
#left eye

#right eye

#mouth red part

#mouth white cover circle

#left arm horizontal part

#left arm vertical part

#right arm horizontal part

#right arm vertical part

#top button

#middle button

#bottom button
