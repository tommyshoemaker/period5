
from tkinter import Tk
from tkinter import mainloop
from tkinter import Label
from karel.SimpleDialog import Dialog
from tkinter import Entry
from tkinter import Button
from tkinter.constants import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

from os.path import basename

from karel.tkwindow import KarelWindow
#from karel.tkworldadapter import window

class WorldMaker(Dialog):
    def __init__(self, master = None, world = None):
        self.karelWindow = master
        self.world = world
        self._canvas = master._canvas
        self.current_tool = None
        self.karelWindow.bind_all('<Command-q>', self.cancel) # Mac standard
        self.karelWindow.bind_all('<Control-q>', self.cancel) # Windows
        
        Dialog.__init__(self, master, title = " Tools ", x = 80, y = 20)
        
                
    def place(self, x, y):
        self.geometry("+%d+%d" % (self.parent.winfo_rootx()+x,
                                  self.parent.winfo_rooty()+y))

    def body(self, master):
        self.master = master
        toolLabel = Label(master, text = "Tool Selection")
        toolLabel.grid(row = 0, column = 0, sticky=N+E+S+W)
        self.streetEntry = Entry(master)
        self.streetEntry.grid(row = 1, column = 0)
        streetLabel = Button(master, text = "Streets", command = self.streets)
        streetLabel.grid(row = 1, column = 1, sticky=N+W+E+S)
        
        self.toolLabel = Label(master, text = "current tool")
        self.toolLabel.grid(row = 2, column = 0, columnspan = 2) #, sticky = N+E+W+S)
                

        horizontalWall = Button(master, text = "Horizontal Wall", command = self.h_wall, width = 20)
        horizontalWall.grid(row = 4, column = 0 )

        verticalWall = Button(master, text = "Vertical Wall", command = self.v_wall, width = 20)
        verticalWall.grid(row = 5, column = 0 )
        
        beeper = Button(master, text = "Beeper", command = self.beeper, width = 20)
        beeper.grid(row = 6, column = 0 )       

        save = Button(master, text = "Save", command = self.save, width = 20)
        save.grid(row = 7, column = 0 )

        open = Button(master, text = "Open", command = self.open, width = 20)
        open.grid(row = 8, column = 0 )
  
        defaultFileText = "untitled.txt"
        self.locationLabel = Label(master, text = defaultFileText)
        self.locationLabel.grid(row = 9, column = 0, columnspan = 2 ) #, sticky = N+E+W+S)
      
        clear = Button(master, text = "Clear", command = self.clear, width = 20)
        clear.grid(row = 10, column = 0 )
#        horizontalWall.invoke()
        return self.streetEntry

    def streets(self):
        self.forgetBindings()
        try:
            val = self.streetEntry.get()
            ival = int(val)
        except Exception :
            ival = 10
            self.streetEntry.delete(0, len(val))
            self.streetEntry.insert(0, '10')
        newSize = int(ival)
        self.world.setSize(newSize, newSize)
        
    class HWallTool :
        def __init__(self, master):
            self.master = master
        
        def scale(self, x, y):
            return self.master.karelWindow._scaleFromPixels(x, y) + \
                self.master.karelWindow._downScaleFromPixels(x, y)
        
        def apply(self, event):
#            print str(event.x) + ' ' + str(event.y)
            dummy1, self.avenue, self.street, dummy2 = self.scale(event.x, event.y)
            try :
                self.master.world.placeWallNorthOf(self.street, self.avenue)
            except Exception :
                pass
#            print str(self.street) + ' ' + str(self.avenue)

        def remove(self, event):
            dummy1, self.avenue, self.street, dummy2 = self.scale(event.x, event.y)
            try :
                self.master.world.removeWallNorthOf(self.street, self.avenue)
            except Exception :
                pass
    
    def h_wall(self):
        self.current_tool = self.HWallTool(self)
        self._canvas.bind('<Button-1>', self.current_tool.apply)
        self._canvas.bind('<Button-3>', self.nothing)
        self._canvas.bind('<Button-2>', self.current_tool.remove)
        self._canvas.config(cursor = 'top_side')
        self.toolLabel.grid_forget()
        self.toolLabel = Label(self.master, text = "Horizontal Wall")
        self.toolLabel.grid(row = 2, column = 0, columnspan = 2) #, sticky = N+E+W+S)
        
    class VWallTool :
        def __init__(self, master):
            self.master = master
        
        def scale(self, x, y):
            return self.master.karelWindow._scaleFromPixels(x, y) + \
                self.master.karelWindow._downScaleFromPixels(x, y)
        
        def apply(self, event):
            self.street, dummy1, dummy2, self.avenue  = self.scale(event.x, event.y)
            try :
                self.master.world.placeWallEastOf(self.street, self.avenue)
            except Exception :
                pass
            
        def remove(self, event):
            self.street, dummy1, dummy2, self.avenue  = self.scale(event.x, event.y)
            try :
                self.master.world.removeWallEastOf(self.street, self.avenue)
            except Exception :
                pass
    
    def v_wall(self):
        self.current_tool = self.VWallTool(self)
        self._canvas.bind('<Button-1>', self.current_tool.apply)
        self._canvas.bind('<Button-3>', self.nothing)
        self._canvas.bind('<Button-2>', self.current_tool.remove)
        self._canvas.config(cursor = 'right_side')
        self.toolLabel.grid_forget()
        self.toolLabel = Label(self.master, text = "Vertical Wall")
        self.toolLabel.grid(row = 2, column = 0, columnspan = 2) #, sticky = N+E+W+S)
        
    class BeeperTool:
        def __init__(self, master):
            self.master = master
            
        def scale(self, x, y):
#            print "raw " + str(x) + " " + str(y)
            return self.master.karelWindow._scaleFromPixels(x, y)
        
        def apply(self, event):
#            x = self.master._canvas.canvasx(event.x)
#            y = self.master._canvas.canvasy(event.y)
            self.street, self.avenue = self.scale(event.x, event.y)
#            print "scaled " + str(self.street) + " " + str(self.avenue)
            try :
                self.master.world.placeBeepers(self.street, self.avenue, 1)
            except Exception :
                pass
            
        def applyinfinite(self, event):
            self.street, self.avenue = self.scale(event.x, event.y)
            try :
                self.master.world.placeBeepers(self.street, self.avenue, -1)
            except Exception :
                pass

        def remove(self, event):
            self.street, self.avenue = self.scale(event.x, event.y)
            try :
                self.master.world.removeAllBeepers(self.street, self.avenue)
            except Exception :
                pass
            
    def nothing(self, event):
        pass
    
    def beeper(self):
        self.current_tool = self.BeeperTool(self)
        self._canvas.bind('<Button-1>', self.current_tool.apply)
        self._canvas.bind('<Button-3>', self.current_tool.applyinfinite)
        self._canvas.bind('<Button-2>', self.current_tool.remove)
        self._canvas.config(cursor = 'circle')
#        self._canvas.focus_set()
        self.toolLabel.grid_forget()
        self.toolLabel = Label(self.master, text = "Beeper")
        self.toolLabel.grid(row = 2, column = 0, columnspan = 2) #, sticky = N+E+W+S)
    
    def save(self):
        self.forgetBindings()
        saveFile = asksaveasfilename()
#        print saveFile
        if saveFile != '' :
            self.world.saveWorld(saveFile)        
            self.locationLabel.grid_forget()
            self.locationLabel = Label(self.master, text = basename(saveFile))
            self.locationLabel.grid(row = 9, column = 0, columnspan = 2) #, sticky = N+E+W+S)
    
    def open(self):
        self.forgetBindings()
        openFile = askopenfilename()
#        print openFile
        if openFile != '' :
            self.world.readWorld(openFile)
            self.locationLabel.grid_forget()
            self.locationLabel = Label(self.master, text = basename(openFile))
            self.locationLabel.grid(row = 9, column = 0, columnspan = 2) #, sticky = N+E+W+S)
        
    def cancel(self, event = None):
        Dialog.cancel(self, event)
        exit()

    def forgetBindings(self):        
        self._canvas.unbind('<Button-1>')
        self._canvas.unbind('<Button-2>')
        self._canvas.unbind('<Button-3>')
        self._canvas.config(cursor = '') # standard cursor
        self.toolLabel.grid_forget()
        self.toolLabel = Label(self.master, text = "current tool")
        self.toolLabel.grid(row = 2, column = 0, columnspan = 2) #, sticky = N+E+W+S)
    
    def clear(self):
        self.forgetBindings()
        self.world.reset()

    def buttonbox(self):
        pass
            
 
def task():
    world._showBuilder()
    
if __name__ == '__main__' :
    from karel.robota import world
    world.setSize(10, 10)
    world.getWindow().run(task)
    
