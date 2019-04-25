#
# Graphic Classes
#

from tkinter import *
import time

class Sprite():
    def __init__(self, canvas, x, y, pic):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.image = self.canvas.create_image(x, y, image=pic)
    def velocityX(self, speed):
        self.x += speed
        self.canvas.coords(self.image, self.x, self.y)
    def velocityY(self, speed):
        self.y += speed
        self.canvas.coords(self.image, self.x, self.y)
    def changeImage(self, pic):
        self.canvas.delete(self.image)
        self.image = self.canvas.create_image(self.x, self.y, image=pic)
    def getX(self):
        spriteCoords = self.canvas.coords(self.image)
        #[x,y]
        return spriteCoords[0]
        #0,1
    def getY(self):
        spriteCoords = self.canvas.coords(self.image)
        #[x,y]
        return spriteCoords[1]
        #0,1
    def f(self, eventw, canvas):
        if event.keysym == "f":
            canvas.create_rectangle(0, 0, 800, 400, fill = "blue")
            canvas.create_text(0, 0, text = ("Press F To Pay Respects."), fill = "#ffffff", font = ("Times", 40))
    def key_control(self, event):
        if event.keysym == "w":
            self.velocityY(-5)
        elif event.keysym == "a":
            self.velocityX(-5)
        elif event.keysym == "s":
            self.velocityY(5)
        elif event.keysym == "d":
            self.velocityX(5)
