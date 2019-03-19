from tkinter import *
import time

#Add to all tKinter programs:
#Canvas() height and width changed as needed
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

#Shapes:
#sky
canvas.create_rectangle(0,0,400,200,fill="#6dd0f7",outline="")
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
canvas.create_arc(170,90,195,115,fill="#000000",outline="",extent="359.999")
#right eye
canvas.create_arc(215,90,240,115,fill="#000000",outline="",extent="359.999")
#mouth red part
canvas.create_arc(180,115,230,165,fill="#ff0000",outline="",extent="359.999")
#mouth white cover circle
canvas.create_arc(180,110,230,160,fill="#ffffff",outline="",extent="359.999")
#left arm horizontal part
canvas.create_rectangle(80,195,150,205,fill="#8c6238",outline="")
#left arm vertical part
canvas.create_rectangle(80,135,90,205,fill="#8c6238",outline="")
#right arm horizontal part
canvas.create_rectangle(280,220,355,230,fill="#8c6238",outline="")
#right arm vertical part
canvas.create_rectangle(345,220,355,255,fill="#8c6238",outline="")
#top button
canvas.create_arc(190,200,215,225,fill="#ff0000",outline="",extent="359.999")
#middle button
canvas.create_arc(190,250,215,275,fill="#ff0000",outline="",extent="359.999")
#bottom button
canvas.create_arc(190,300,215,325,fill="#ff0000",outline="",extent="359.999")
#signature
canvas.create_text(325,390,text="Tommy Shoemaker",font=("Roboto",16))
