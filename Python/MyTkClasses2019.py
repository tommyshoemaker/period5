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
