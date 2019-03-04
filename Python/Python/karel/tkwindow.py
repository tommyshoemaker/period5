""" Copyright 2008 Joseph Bergin
License: Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License
"""
from tkinter import Tk
from tkinter import mainloop
from tkinter import Label
from tkinter import Frame
from tkinter import Button
#from Tkinter import PhotoImage
from tkinter import Canvas
from tkinter import Scale
from tkinter import IntVar
from tkinter import Menu

from karel.basicdefinitions import North
from karel.basicdefinitions import East
from karel.basicdefinitions import South
from karel.basicdefinitions import West
from karel.basicdefinitions import _nextDirection

from tkinter.font import Font

from time import sleep
import threading

from tkinter.constants import *

_moveParameters = {North: (0, -1), West: (-1, 0), South: (0, 1), East:(1, 0) }

_windowBottom = 800
_inset = 30

class RobotImage:
    rNumber = 0
    def __init__(self, street, avenue, direction, window, fill='blue', outline='black'):
        self._canvas = window._canvas
        self._street = street
        self._avenue = avenue
        self.scaleFactor = window.scaleFactor
        self._scaler = window._scaleToPixels
#        self.__configControl = window._KarelWindow__configControl
        self._place = self._scaler(street, avenue)
        self.karelPackage = {"size":23, "draw":self.showKarel, "figure":RobotImage.karelRobot}
        self.alienPackage = {"size":6, "draw":self.showAlien, "figure":RobotImage.alienRobot}
        self.crabPackage = {"size":6, "draw":self.showAlien, "figure":RobotImage.crabRobot}

        # the next statement defines which figure will be drawn
        package = self.karelPackage
        
        self._basicSize = package["size"] # the size of the bounding box of the figure
        self.show = package["draw"] # the drawing method
        self.__north = package["figure"] # the list of component listss

        self.__setup()  # compute rotations
        self.__imageChooser = {North: self.__north, East: self.__east, South: self.__south, West: self.__west}
        # maps karel directions to the image maps. 
        
        self._direction = direction
        if fill == None:
            fill = "yellow"
        self._fill = fill
        self._outline = outline
        self.tag = "r"+str(RobotImage.rNumber)
        RobotImage.rNumber += 1
        self.__buildImage()
        
        
    def deleteAll(self):
        self._canvas.delete(self.tag)
        
    # A robot image is defined by a list of lists keyed to a drawing (show) method
    # The drawing method knows how to render each element of the list
    # The pixels named (in the tuples) are within a bounding box of a certain size that
    #  can vary. It is listed as part of the drawing "package" for this figure. This one is in 
    # a square 23 pixels on a side. The simpler ones are in a 6 pixel box. This is needed for scaling.     
    karelRobot = [ # use _basicSize = 23
            [   
                (-6,-10), #poly grey head
#                (0, -8),
                (6,-10),
                (6,-3),
                (-6,-3)
            ],
            [
                (-4,-3), #poly fill color body
                (4,-3),
                (4, -2),
                (6, -2),
                (6,8),
                (-6,8),
                (-6, -2),
                (-4, -2)
            ],
            [
                (-6,8), #poly red foot
                (-2,8),
                (-2,11),
                (-6,11)
            ],
            [
                (2,8), #poly red
                (6,8),
                (6,11),
                (2,11)
            ],
            [
                (-8,-1), #poly green arm
                (-6,-1),
                (-6,6),
                (-8,6)
            ],
            [
                (8,-1), #poly green
                (6,-1),
                (6,6),
                (8,6)
            ],
            [ (-3, -7), (-1, -5)], #oval eye blue
             
            [ (1, -7), (3, -5)], #oval eye blue
            [(-2, -1), (-2, 7)], # K in black
            [(-2, 3), (3, -1)],
            [(-2, 3), (3, 7)]
    ]
    
    alienRobot = [ # use _basicSize = 6
          [
              (0, -1), # pixel polsitions in a (0,0) centered square of size _basicSize
              (0, 1), # the first list here is the basic outline - polygon
              (-3, 3), 
              (0, 1),
              (3, 3),
              (0, 1),
              (0, -1),
              (2, -1),
              (2, -2),
              (0, -3),
              (-2, -2),
              (-2, -1)
            ],
            [(-1, -2), (0, -1)], #left eye - circle
            [(0, -2), (1, -1)] #right eye - circle                
    ]
    
    crabRobot = [ # use _basicSize = 6
             [
                (0,-3), #Alternate robot image
                (-3,-1),
                (-2,-1),
                (-2,0),
                (-3,0),
                (-1,3),
                (-1,0),
                (1,0),
                (1,3),
                (3,0),
                (2,0),
                (2,-1),
                (3,-1)
             ],
             [(-1, -2), (0, -1)], #left eye - circle
             [(0, -2), (1, -1)] #right eye - circle                               
    ]
                  
    def __setup(self): 
        ''' Define the robot rotations from the basic north facing version'''
        result = []
        for list in self.__north :
            item = []       
            for (x,y) in list :
                item.append((y, -x))
            result.append(item)     
        self.__west = result
        
        result = []
        for list in self.__west :
            item = []
            for (x,y) in list :
                item.append((y, -x))
            result.append(item)
        self.__south = result
        
        result = []
        for list in self.__south :
            item = []
            for (x,y) in list :
                item.append((y, -x))
            result.append(item)
        self.__east = result

        
    def greyOut(self):
        self._outline = "grey"
        self.show()
       
        
    def move(self, amount):
        ''' Moves a robot by an arbitrary amount in pixels, not streets, but in forward direction'''        
#        self.__configControl.acquire()
        (dx,dy) = _moveParameters[self._direction]
        self._street -= dy
        self._avenue += dx
        self.translate(amount*dx, amount*dy)
        if self._canvas != None :
            self._canvas.move(self.tag, amount*dx, amount*dy)
#        self.__configControl.notify()
#        self.__configControl.release()
            
    def _dumpImage(self):
        print("[")
        for alist in self.image :
            print('  [')
            for (x,y) in alist :
                print('  (' + str(x) +', ' + str(y) + '),') 
            print('  ]')
        print("]")
        
    def rotate(self):
        ''' image turns left'''
        if self._canvas != None :
            self._canvas.delete(self.tag)
        result = []
#        print str(self._direction)
#        print str(self.__imageChooser[self._direction])
        for list in self.__imageChooser[self._direction] :
            item = []
            for (x,y) in list :
                item.append((y*self.__scale, -x*self.__scale)) #rotate AND scale
            result.append(item)
        self.image = result
        
        self._direction = _nextDirection[self._direction] #(self._direction + 1) % 4

        self.__translate(self.__translate_x, self.__translate_y)
        if self._canvas != None :
            self.show()
                
    def scale(self, mult):
        ''' scale the image up from the basic 6 (or 23...) pixel version'''
        self.__scale = mult
        result = []
        for list in self.__imageChooser[self._direction] :
            item = []
            for (x,y) in list :
                item.append((x*mult, y*mult))
            result.append(item)
        self.image = result
                    
    def __translate(self, horiz, vert):
        ''' move a robot an aribitrary amount and direction'''
        result = []
        for list in self.image :
            item = []
            for (x,y) in list :
                item.append((x + horiz, y + vert))
            result.append(item)
        self.image = result        
        
    def translate(self, horiz, vert):
        ''' remember a translateion and perform it'''
        self.__translate_x += horiz
        self.__translate_y += vert
        self.__translate(horiz, vert)
        
    def showKarel(self):
        ''' create the graphic object and make it visible'''
        self._canvas.delete(self.tag)
        result = self._canvas.create_polygon( self.image[0], # head
                              outline = self._outline,
                              fill = "grey",
                              width=2,
                              smooth = True,
                              tags = self.tag
                              )
        result = self._canvas.create_polygon( self.image[1], # body
                              outline = self._outline,
                              fill = self._fill,
                              width=2,
                              smooth = False,
                              tags = self.tag
                              )
        for i in range(2, 4): # two feet
            result1 = self._canvas.create_polygon( self.image[i],
                              outline = self._outline,
                              fill = "red",
                              width=2,
                              smooth = True,
                              tags = self.tag
                              )
#        result1 = self._canvas.create_polygon( self.image[3],
#                              outline = self._outline,
#                              fill = "red",
#                              width=2,
#                              smooth = True,
#                              tags = self.tag
#                              )
        for i in range(4, 6) : # two arms
            result1 = self._canvas.create_polygon( self.image[i],
                              outline = self._outline,
                              fill = "green",
                              width=2,
                              smooth = False,
                              tags = self.tag
                             )
#        result1 = self._canvas.create_polygon( self.image[5],
#                              outline = self._outline,
#                              fill = "green",
#                              width=2,
#                              smooth = False,
#                              tags = self.tag
#                              )
        for i in range(6, 8): # two eyes
            result1 = self._canvas.create_rectangle(self.image[i], fill = "blue", width = 2, outline = self._outline, tags = self.tag) #left eye
        for i in range(8, 11) : # letter k (three lines)
            result1 = self._canvas.create_line(self.image[i], width = 2, fill = self._outline, tags = self.tag)
        return result
    
    def showAlien(self): # works for crabRobot also
        ''' create the graphic object and make it visible'''
        self._canvas.delete(self.tag)

        result = self._canvas.create_polygon( self.image[0],
                              outline = self._outline,
                              fill = self._fill,
                              smooth = 1,
#                              stipple = self._stipple,
                              splinesteps = 10,
                              width = 2, tags = self.tag)
        color = "green"
        if self._fill == "green" :
            color = "magenta"
        result1 = self._canvas.create_oval(self.image[1], fill = color, tags = self.tag) #left eye
        result1 = self._canvas.create_oval(self.image[2], fill = color, tags = self.tag) # right eye
        return result
    
    def moveScale(self): # used to move the object after the size of world is changed
        self._canvas.delete(self.tag)
        self.image = self.__imageChooser[self._direction]
        self.__buildImage()

    def __buildImage(self):
        self.__translate_x = 0
        self.__translate_y = 0
        self.scale(self.scaleFactor()/(self._basicSize*1.0))
        (x,y) = self._scaler(self._street, self._avenue)
        self.translate(x, y)
        self.show()
         

class KarelWindow(Frame):

    def geometry(self, height):
#        print "gemo " + str(self._oldHeight) + ' ' + str(height)
        self._oldHeight = self._height
        self._height = height
        self.__bottom = height - self._inset
        self.__left = self._inset
        self.__top = self._inset
        self.__right = height
#        self.__scaleFactor = ((self.__bottom - self.__top)*1.0/self.__streets)

    def __init__(self, streets, avenues, size = 800, callback = None): # avenues is ignored in this version
#        self.__configControl = threading.Condition()
        self.__root = root = Tk(className=" Karel's World ") # , geometry='800x600+60+10'
        global _windowBottom
        _windowBottom = size
        geometryString = '820x' + str(_windowBottom + 65) + "+55+25"
        root.geometry(newGeometry= geometryString) #'820x865+55+25') # placement of window on desktop
#        print str(root.tk_menuBar())
        Frame.__init__(self, master=root, cnf={})
        
        bar = Menu()        
        def endProgram(menu): exit()
        
        fil = Menu()
        fil.add_command(label = 'Quit   ^Q', command=lambda x='Quit':endProgram(x))
        bar.add_cascade(label='File', menu=fil)
        root.config(menu=bar)
        self.bind_all('<Command-q>', exit) # Mac standard
        self.bind_all('<Control-q>', exit) # Windows
        self.__streets = streets
        self.__avenues = streets # sic Avenues ignored
        self.__gBeepers = {} #locations of the beeper imagess
        self.__contents = [] # , walls, beepers that need to move on a rescale
        self.__robots = []
        self.__beeperControl = threading.Condition() # helps multi threaded programs avoid anomalies
        self.__walls = [] # all the basic visual elements (boundary, streets, street labels, etc. 
        
        top = self.winfo_toplevel()
        top.rowconfigure(2, weight = 1)
        top.columnconfigure(0, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.columnconfigure(0, weight = 1)
        root.rowconfigure(2, weight = 1)
        root.columnconfigure(0, weight = 1)
        
        speedLabel = Label(text = "Speed")
        speedLabel.grid(row = 0, column = 0, sticky=N+W+E+S)

        if callback != None : # this makes the speed slider work. 
            from tkinter import IntVar
            self.iv = IntVar()
            self.iv.trace('r', callback)
        
            self.scale = Scale(orient = HORIZONTAL, variable = self.iv)
            self.scale.set(20)
            self.scale.grid(row = 1, column = 0, sticky=N+S)
#        self.__callback = callback
#        global _windowRight
        global _inset
#        root.minsize(_windowBottom, _windowRight)
        self._height = self._oldHeight = _windowBottom
        self.__bottom = _windowBottom - _inset #770
        self.__left = _inset #30
        self.__top = _inset #30
        self.__right = self._height #_windowRight - _inset #770
        self._inset = _inset
        
#        print str(speedLabel.config())
#        print str(self.scale.config())
        self._canvas = Canvas(root, height = _windowBottom, width = _windowBottom,bg = 'white')
        self._canvas.grid(row = 2, column = 0, sticky=N+E+W+S)
        self.geometry(self._height)
        self.setSize(streets)

#        self._canvas.bind_all('<Expose>', self.expose)
#        self._canvas.bind('<Configure>', self.configure)

        

#    def expose(self, event):
##        print 'expose ' + str(event.width)+ ' ' + str(event.height)
#        pass
    
#    def configure(self, event):
##        print str(self._canvas.config())
##        print "config " + str(event.height)
##        self.__configControl.acquire()
#        self.geometry(event.height)
#        delta = (self._oldHeight - self._height)*1.0/self._oldHeight
#        scale = self._height*1.0/self._oldHeight
#        self._canvas.scale('all', 0, 0, scale, scale)
#        self._canvas.move('all', delta, delta)
##        print "config " + str(event.widget)+ ' ' +str(event.x)+ ' ' + str(event.y)+' ' + str(event.width)+ ' ' + str(event.height)
##        self.__configControl.notify()
##        self.__configControl.release()
#        pass
        
    def clear(self):
        for item in self.__contents + self.__robots :
            item.deleteAll()
        
    def setSize(self, streets):     #streets can change    
        self.__streets = streets

        for x in self.__walls : # boundary walls and street lines
            self._canvas.delete(x)
        self.makeStreetsAndAvenues()
        self.makeBoundaryWalls()
        self.labelStreetsAvenues()
        for item in self.__contents + self.__robots : #rebuild the contents of the world
            item.moveScale()
            
            
    def scaleFactor(self):
        self.geometry(self._height)
#        print "in scaler " + str(self.__bottom) + " " + str(self.__top) + ' ' + str(self.__streets)
        return ((self.__bottom - self.__top)*1.0/self.__streets)#self.__scaleFactor
                   
    class Beeper:
        bNumber = 0
        def __init__(self, street, avenue, number, window):
            self._street = street
            self._avenue = avenue
            self._number = number
            self._scaler = window._scaleToPixels
            self.scaleFactor = window.scaleFactor
            self._canvas = window._canvas
            self.tag = "b" + str(KarelWindow.Beeper.bNumber)
            KarelWindow.Beeper.bNumber += 1
            
        def place(self):
            sizeFactor = .5 #Change this to change beeper size. The others scale from it. 
            placeFactor = .5 * sizeFactor
            val = str(self._number)
            if self._number < 0 :
                val = "oo"
            (x,y) = self._scaler(self._street+placeFactor, self._avenue-placeFactor)
#            print 'beeper ' + str(x) + ' ' + str(y)
#            print 'factor ' + str(self.scaleFactor())
#            
            # circular beepers
#            self._canvas.create_oval(x, y, x + self.__scaleFactor*sizeFactor, y + self.__scaleFactor*sizeFactor, fill= 'black', tags = self.tag)
            # triangular beepers
            where = []
            where.append(self._scaler(self._street+sizeFactor, self._avenue))
            where.append(self._scaler(self._street-placeFactor, self._avenue-placeFactor))
            where.append(self._scaler(self._street-placeFactor, self._avenue+placeFactor))
            self._canvas.create_polygon(where, fill = "black", smooth = False, tags=self.tag)
            self._canvas.create_text(x + self.scaleFactor()*placeFactor, y+ self.scaleFactor()*placeFactor, text=val, 
                                      font = Font(size = int(-self.scaleFactor()*placeFactor)), fill = 'white', tags=self.tag)
            
        def deleteAll(self):
            self._canvas.delete(self.tag) 
            
        def moveScale(self):
            self._canvas.delete(self.tag)
            self.place()
            
    class Wall:
        def __init__(self, street, avenue, isVertical, window):
            self._street = street
            self._avenue = avenue
            self._isVertical = isVertical
            self.scaleFactor = window.scaleFactor
            self._scaler = window._scaleToPixels
            self._canvas = window._canvas
            if self._isVertical:
                (x, y) = self._scaler(street - .5, avenue + .5)
                self._code = self._canvas.create_line(x, y, x, y - self.scaleFactor(), width = 2)
            else:
                (x, y) = self._scaler(street + .5, avenue - .5)
                self._code = self._canvas.create_line(x, y, x + self.scaleFactor(), y, width = 2)
                # _code identifies the wall segment image in the tk layer
            
        def moveScale(self):
            self._canvas.delete(self._code) #erase the current figure in prep to draw a new one
            if self._isVertical:
                (x, y) = self._scaler(self._street - .5, self._avenue + .5)
                self._code = self._canvas.create_line(x, y, x, y - self.scaleFactor(), width = 2)
            else:
                (x, y) = self._scaler(self._street + .5, self._avenue - .5)
                self._code = self._canvas.create_line(x, y, x + self.scaleFactor(), y, width = 2)
                
        def deleteAll(self):
            self._canvas.delete(self._code)
                   
            
    def placeBeeper(self,street, avenue, number):
#        self.__beeperControl.acquire() # sync was moved to tkworldadapter
        beeper = self.Beeper(street, avenue, number, self)
        beeper.place()
        self.__gBeepers[(street, avenue)] = beeper
        self.__contents.append(beeper)
#        self.__beeperControl.notify()
#        self.__beeperControl.release()
#        return beeper
    
    def deleteBeeper(self, beeperlocation):
#        self.__beeperControl.acquire()
        beeper = self.__gBeepers.get(beeperlocation, None)
        if beeper != None :
            beeper.deleteAll()
            self.__gBeepers.pop(beeperlocation)
            i = 0
            for b in self.__contents :
                if b == beeper :
                    break
                i+=1
            self.__contents.pop(i)
#        self.__beeperControl.notify()
#        self.__beeperControl.release()
    
    def placeWallNorthOf(self, street, avenue):
        self.__contents.append(self.Wall(street, avenue, False, self))
        
    def removeWallNorthOf(self, street, avenue):
        i = 0
        for wall in self.__contents :
            if wall.__class__ is self.Wall and wall._street == street and wall._avenue == avenue and not wall._isVertical:
                wall.deleteAll()
                self.__contents.pop(i)
#                print 'h gone'
                break
            i += 1

    def placeWallEastOf(self, street, avenue):
        self.__contents.append(self.Wall(street, avenue, True, self))
    
    def removeWallEastOf(self, street, avenue):
        i = 0
        for wall in self.__contents :
            if wall.__class__ is self.Wall and wall._street == street and wall._avenue == avenue and wall._isVertical :
                wall.deleteAll()
                self.__contents.pop(i)
#                print 'v gone'
                break
            i +=1
        
    def makeBoundaryWalls(self):
        (x, y) = self._scaleToPixels(.5, .5) # hardcode ok. Half way between streets
        self.__walls.append(self._canvas.create_line(x, 0, x, y, width = 2)) # should width depend on number of streets?
        global _inset
        self.__walls.append(self._canvas.create_line(x, y, self.__right + _inset, y, width = 2))
        
    def makeStreetsAndAvenues(self):
        for i in range(0, self.__streets) :
            (x, y) = self._scaleToPixels(i+1, .5)
            (tx, ty) = self._scaleToPixels(i+1, self.__streets + .5)
            self.__walls.append(self._canvas.create_line(x, y, tx, ty, fill="red"))
            (x,y) = self._scaleToPixels(.5, i + 1)
            (tx, ty) = self._scaleToPixels(self.__streets + .5, i + 1)
            self.__walls.append(self._canvas.create_line(x, y, tx, ty, fill= "red"))
        
    def labelStreetsAvenues(self):
        for i in range(self.__streets):
            (x, y) = self._scaleToPixels(i + 1, .25)
            self.__walls.append(self._canvas.create_text(x,y, fill = 'black', text = str(i+1)))
            (x,y) = self._scaleToPixels(.25, i + 1)
            self.__walls.append(self._canvas.create_text(x,y, fill = 'black', text = str(i+1)))
    
    def addRobot(self, street, avenue, direction, fill, outline):
        #        fill and outline are colors, default to blue, black
        robot = RobotImage(street, avenue, direction, self, fill, outline)
        self.__robots.append(robot)
        return robot # the world matches these with the actual robot objects in the model. 
    
    def moveRobot(self, robot, amount = -1):
        #If no amount is specified then it moves one block, Otherwise amount pixels, not blocks
        if amount < 0 :
            amount = self.scaleFactor()
        robot.move(amount)
    
    def _scaleToPixels(self, street, avenue): # origin is at corner (0,0) outside the world
        scale = self.scaleFactor()
        return (self.__left + avenue*scale, self.__bottom - street*scale)
    
    def _scaleFromPixels(self, x, y):
        scale = self.scaleFactor()
        return (int(round((self.__bottom - y)/scale)), int(round((x - self.__left)/scale)))

    def _downScaleFromPixels(self, x, y):
        scale = self.scaleFactor()
        return (int((self.__bottom - y)/scale), int((x - self.__left)/scale))
    
    def run(self, task, *pargs): # this is the actual graphic main. 
       mainThread = threading.Thread(target = task, args=pargs)
       mainThread.start()
       self.mainloop()
        
    def _test(self):
        pass

       
if __name__ == '__main__': # this is to run test code only. Not normally used
    window = KarelWindow(12, 12)
    
    mainThread = threading.Thread(target = window._test)
    mainThread.start()
    
    window.mainloop()
#    for i in range(10):
#        sleep(1.0)
#        window.canvas.move("foo", 10, 10)

