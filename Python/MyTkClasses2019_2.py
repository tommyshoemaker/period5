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
        #Add this
        self.width = pic.width()
        self.height = pic.height()

    def velocityX(self, speed):
        self.x = self.x + speed
        self.canvas.coords(self.image, self.x, self.y)

    #define the velocityY method:
    def velocityY(self, speed):
        self.y = self.y + speed
        self.canvas.coords(self.image, self.x, self.y)

    def changeImage(self, pic):
        self.canvas.delete(self.image)
        self.image = self.canvas.create_image(self.x, self.y, image=pic)

    def getX(self):
        spriteCoords = self.canvas.coords(self.image)  #[x, y]
        return spriteCoords[0]                         # 0, 1

    def key_control(self, event):
        #Add events to move left, right, up, and down:
        if event.keysym =="a":
            self.velocityX(-5)
        elif event.keysym =="d":
            self.velocityX(5)
        elif event.keysym =="w":
            self.velocityY(-5)
        elif event.keysym =="s":
            self.velocityY(5)
        elif event.keysym =="q":
            self.velocityX(-5)
            self.velocityY(-5)
        elif event.keysym =="e":
            self.velocityX(5)
            self.velocityY(-5)
        elif event.keysym =="z":
            self.velocityX(-5)
            self.velocityY(5)
        elif event.keysym =="c":
            self.velocityX(5)
            self.velocityY(5)
        

    def isTouching(self, target):
        spriteCoords = self.canvas.coords(self.image)
        spriteLeft = spriteCoords[0] - self.width/2
        spriteRight = spriteCoords[0] + self.width/2
        spriteTop = spriteCoords[1] - self.height/2
        spriteBottom = spriteCoords[1] + self.height/2

        targetCoords = self.canvas.coords(target.image)
        targetLeft = targetCoords[0] - target.width/2
        targetRight = targetCoords[0] + target.width/2
        targetTop = targetCoords[1] - target.height/2
        targetBottom = targetCoords[1] + target.height/2
        
        
        #if self is moving right toward sprite,
        if (spriteLeft <= targetRight and spriteLeft >= targetLeft) \
        or (spriteRight >= targetLeft and spriteRight <= targetRight):
            print("Touching")
        

    #define the getY method:
    

    
