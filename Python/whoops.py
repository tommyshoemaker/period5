from tkinter import *
import time
import random

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_oval(20, 100, 120, 200, fill="#654321", outline="")
canvas.create_oval(20, 200, 120, 300, fill="#654321", outline="")

x1 = 70
while True:
    x1 += 1
    x2 = x1 + 50
    canvas.create_oval(x1, 175, x2, 225, fill="#654321", outline="")
    tk.update()
