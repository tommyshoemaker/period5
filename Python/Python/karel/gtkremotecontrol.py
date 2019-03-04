
import tkinter
import gtk

from karel.robota import world
from karel.robotworldbase import East
from karel.robota import UrRobot
from karel.basicdefinitions import infinity

from karel.gtkwindow import KarelWindow
from karel.gtkworldadapter import window

offset = 0

class RemoteControl:
    def __init__(self, name, street, avenue, direction, beepers, fill = None, outline = None):
        self.karel = UrRobot(street, avenue, direction, beepers, fill, outline)
#        self.window = window()
        world.setDelay(0)
        self.fill = fill
        self.name = name
        global offset
        offset += 20
        window = gtk.Dialog()
        window.set_has_separator(False)
        try: 
            color = gtk.gdk.color_parse(fill)
            window.modify_bg(gtk.STATE_NORMAL, color)
        except:
            pass

        window.connect("destroy", self.destroy)
        window.set_title(name)
        window.set_size_request(100, 150)

        moveButton = gtk.Button("Move")
        moveButton.connect("clicked", self.move)
        moveButton.show()
        window.vbox.pack_start(moveButton, True, False, 0)

        turnButton = gtk.Button("TurnLeft")
        turnButton.connect("clicked", self.turnLeft)
        turnButton.show()
        window.vbox.pack_start(turnButton, True, False, 0)

        pickButton = gtk.Button("PickBeeper")
        pickButton.connect("clicked", self.pickBeeper)
        pickButton.show()
        window.vbox.pack_start(pickButton, True, False, 0)

        putButton = gtk.Button("PutBeeper")
        putButton.connect("clicked", self.putBeeper)
        putButton.show()
        window.vbox.pack_start(putButton, True, False, 0)
        
        
        turnOffButton = gtk.Button("TurnOff")
        turnOffButton.connect("clicked", self.turnOff)
        turnOffButton.show()
        window.vbox.pack_start(turnOffButton, True, False, 0)
        window.show()   
        window.move(500 + offset, 20 + offset)
        
    def move(self, widget):
        if not self.karel.isRunning() :
            print (self.name + " tried to move when it wasn't running.")
            return
        try :
            self.karel.move()
            print (self.name + ".move()")
        except :
            print (self.name + " tried to walk through a wall.")
             
    def turnLeft(self, widget):
        try :
            self.karel.turnLeft()
            print (self.name + ".turnLeft()")
        except :
            print (self.name + " tried to turnLeft when it wasn't running.")
             
    def pickBeeper(self, widget):
        if not self.karel.isRunning() :
            print (self.name + " tried to pickBeeper when it wasn't running.")
            return
        try :
            self.karel.pickBeeper()
            print (self.name + ".pickBeeper()")
        except :
            print (self.name + " tried to pickBeeper when none are present.")
             
    def putBeeper(self, widget):
        if not self.karel.isRunning() :
            print (self.name + " tried to putBeeper when it wasn't running.")
            return
        try :
            self.karel.putBeeper()
            print (self.name + ".putBeeper()")
        except :
            print ( self.name + " tried to putBeeper when none available." )                         
        
    def turnOff(self, widget):
        self.karel.turnOff()
        print (self.name + ".turnOff()")

        
    def destroy(self, widget):
        gtk.main_quit()
        
def task(): # this is just a sample of what you can do
    world.setSize(10, 10)
    control = RemoteControl("karel", 1, 1, East, infinity, 'blue')
    control = RemoteControl("carol", 1, 2, East, 0)

    
if __name__ == '__main__' :
    window().run(task)
