from tkinter import *
import time
import random

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

counter = 0

print (format(325, 'b'))

while True:
        #Create BG
        canvas.create_rectangle(0, 0, 400, 400, fill="white")
        #Increase counter by 1
        counter += 1
        #Display variable "counter"
        canvas.create_text(200, 100, text=format(counter, 'b'), fill="#000000", font=("roboto", 30))

        tk.update()
        time.sleep(0.05)
