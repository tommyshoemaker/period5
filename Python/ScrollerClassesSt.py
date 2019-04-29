#
# Graphic Classes
#
from tkinter import *
import time
class Sprite ():
    def __init__(self,canvas,x,y,pic):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.image = self.canvas.create_image(x,y,image=pic)
        self.width = pic.width()
        self.height = pic.height()
                
    def velocityX(self,speed):
        self.x = self.x + speed
        self.canvas.coords(self.image,self.x,self.y)

    #define the velocityY method:
    def velocityY(self,speed):
        self.y = self.y + speed
        self.canvas.coords(self.image,self.x,self.y)

    def changeImage(self,pic):
        self.canvas.delete(self.image)
        self.image = self.canvas.create_image(self.x,self.y,image=pic)

    def getX (self):
        spriteCoords = self.canvas.coords(self.image)  #[x,y]
        return spriteCoords[0]                         # 0,1

    def getY (self):
        spriteCoords = self.canvas.coords(self.image)  #[x,y]
        return spriteCoords[1]                         # 0,1


    def draw(self):
        #set the velocityX of the sprite so it moves to the left:
        self.velocityX(-5)
        #if sprite reaches left edge, reset it back to the right edge:
        #AFTER YOU FINISH THIS METHOD, SAVE AND TEST THE THE MAIN PROGRAM
class PlayerSprite(Sprite):
    def __init__(self,canvas,x,y,pic):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.image = self.canvas.create_image(x,y,image=pic)
        
        self.width = pic.width()
        self.height = pic.height()
        
        self.direction = 0  #Used to control up/down direction
        self.jumping = False  #state of player sprite
        
        
    def isTouching(self,target):
        
        spriteCoords = self.canvas.coords(self.image)  #0 is x,  1 is y
        #sprite's left and right edge coordinates (on x axis)
        spriteLeft = spriteCoords[0] - self.width/2
        spriteRight = spriteCoords[0] + self.width/2
        #sprite's top and bottom edge coordinates (on y axis)
        spriteTop = spriteCoords[1] - self.height/2
        spriteBottom = spriteCoords[1] + self.height/2

        targetCoords = self.canvas.coords(target.image)
        #target's left and right edge coordinates (on x axis)
        targetLeft = targetCoords[0] - target.width/2
        targetRight = targetCoords[0] + target.width/2
        #target's left and right edge coordinates (on x axis)
        targetTop = targetCoords[1] - target.height/2
        targetBottom = targetCoords[1] + target.height/2
       
        #Check if any sprite coordinates are within target coords,
        # return True:
        if ((spriteLeft <= targetRight and spriteLeft >= targetLeft) \
        or (spriteRight >= targetLeft and spriteRight <= targetRight) \
        or (spriteLeft < targetLeft and spriteRight > targetRight)) \
        and (( spriteTop <= targetBottom and spriteTop >= targetTop) \
        or ( spriteBottom >= targetTop and spriteBottom <= targetBottom) \
        or ( spriteBottom > targetBottom and spriteTop < targetTop)):
            return True

    def key_control(self,event):
        #Add events to move left, right, up, and down:
        if event.keysym =="a":
            self.velocityX(-5)
        elif event.keysym =="d":
            self.velocityX(5)
        elif event.keysym =="w":
            self.jump()

    def jump(self):
        if self.y >= 325: #on ground
            self.velocityY(-15)
            self.jumping = True
            

    def draw(self):
        self.canvas.bind_all("<KeyPress-a>",self.key_control)
        self.canvas.bind_all("<KeyPress-d>",self.key_control)
        self.canvas.bind_all("<KeyPress-w>",self.key_control)

        #direction of velocityY is controled by its sign
        self.velocityY(5*self.direction)

        #if player sprite is jumping, change direction to -1
        #so that it goes up:

        
        #if player sprite has reached maximum height of the jump
        #  1)change direction to 1 so that it starts going down
        #  2) change self.jumping to False

        
        #if player has come back down to the ground (based on it's y),
        # change direction to 0 so it doesn't move
        
            


    
