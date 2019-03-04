''' Copyright 2008 Joseph Bergin
License: Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License

This is the graphics layer for pygtk graphics. 
'''
import pygtk
pygtk.require('2.0')
import gtk
import gobject
import pango
import threading
from time import sleep
from os.path import *

gtk.gdk.threads_init()

from karel.basicdefinitions import North
from karel.basicdefinitions import East
from karel.basicdefinitions import South
from karel.basicdefinitions import West
from karel.basicdefinitions import _nextDirection

_moveParameters = {North: (1, 0), West: (0, -1), South: (-1, 0), East:(0, 1) }

pixmap = None    
    
class RobotImage:
    def __init__(self, street, avenue, direction, window, fill, outline):
        ''' note that outline color is ignored in this version
        '''
        self._street = street

        self._avenue = avenue
        self._running = True
        self._direction = direction
        self._scaler = window._scaleToPixels
        self._scale_factor = window._scaleFactor
        self._layout = window._pangolayout
        self._window = window
        self._fill = fill
        self._outline = outline
        self._setup()
        self._backset = int(self._imageSize/2)
        # map to tuples of on/off images
        self.show()

    def _setup(self):
        global pixmap
        pixmap.new_gc()
        _our_dir = dirname(abspath(normpath(__file__)))
        localpath = "/figs/"
        path = _our_dir + localpath
        white = gtk.gdk.color_parse("white")
        
        self._imageSize = 25 #pixels
    
        self._clear_image, mask = gtk.gdk.pixmap_create_from_xpm(self._window._area.window,
                                    white, normpath(path  + "clear.xpm"))
    
        image, mask = gtk.gdk.pixmap_create_from_xpm(self._window._area.window,
                                    white, normpath(path  + "karele.xpm"))
        imageOff, mask = gtk.gdk.pixmap_create_from_xpm(self._window._area.window,
                                    white, normpath(path  + "kareleOff.xpm"))
        self._east = (image, imageOff)
        image, mask = gtk.gdk.pixmap_create_from_xpm(self._window._area.window,
                                    white, normpath(path  + "kareln.xpm"))
        imageOff, mask = gtk.gdk.pixmap_create_from_xpm(self._window._area.window,
                                    white, normpath(path  + "karelnOff.xpm"))
        self._north = (image, imageOff)
        image, mask = gtk.gdk.pixmap_create_from_xpm(self._window._area.window,
                                    white, normpath(path  + "karels.xpm"))
        imageOff, mask = gtk.gdk.pixmap_create_from_xpm(self._window._area.window,
                                    white, normpath(path  + "karelsOff.xpm"))
        self._south = (image, imageOff)
        image, mask = gtk.gdk.pixmap_create_from_xpm(self._window._area.window,
                                    white, normpath(path  + "karelw.xpm"))
        imageOff, mask = gtk.gdk.pixmap_create_from_xpm(self._window._area.window,
                                    white, normpath(path  + "karelwOff.xpm"))
        self._west = (image, imageOff)
    
        self._imageChooser = {North: self._north, East: self._east, South: self._south, West: self._west}
        
    def turnOff(self):
        self._running = False
        self._window.update()
    
    
    def show(self):
        images = self._imageChooser[self._direction]
        if self._running :
            image = images[0]
        else :
            image = images[1]
        global pixmap
        gc = pixmap.new_gc()
        (x,y) = self._scaler(self._street, self._avenue)
        pixmap.draw_drawable(gc, image, 0, 0, x-self._backset, y-self._backset, -1, -1)
        try:
            color = gtk.gdk.color_parse(self._fill)
            gc.set_rgb_fg_color(color)   
            pixmap.draw_rectangle(gc, True, x-3, y-3, 7, 7)
        except Exception :
            pass
        
    def erase(self):
        images = self._imageChooser[self._direction]
        if self._running :
            image = images[0]
        else :
            image = images[1]
        global pixmap
        gc = pixmap.new_gc()
        gc.set_function(gtk.gdk.XOR)
        (x,y) = self._scaler(self._street, self._avenue)
#        image, mask =  image.get_image()285
        pixmap.draw_drawable(gc, image, 0, 0, x-self._backset, y-self._backset, -1, -1)
        
    def move(self, amount):
        ''' Moves a robot by an arbitrary amount in pixels, not streets, but in forward direction''' 
        global _moveParameters
        self.erase()
        
        global pixmap
        gc = pixmap.new_gc()
        (x,y) = self._scaler(self._street, self._avenue)
        pixmap.draw_drawable(gc, self._clear_image, 0, 0, x-self._backset, y-self._backset, -1, -1)
        
        self._street += _moveParameters[self._direction] [0]  
        self._avenue += _moveParameters[self._direction] [1]  
        self.show()
        
    def rotate(self):
        ''' 90 degrees to the left'''
        self.erase()
        self._direction = _nextDirection[self._direction]
        self.show()
        self._window.update()
    
    def moveScale(self):
        self.show()



class KarelWindow:
    ui_menu = '''<ui>
        <menubar name="MenuBar">
            <menu action="File">
                <menuitem name="Quit"/>
                <menuitem action="Quit"/>
            </menu>
        </menubar>
    </ui>'''


    
    def __init__(self, streets, avenues, speedCallback):
        self._window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self._window.set_title("Karel's World")
        self._window.connect("delete_event", self.delete_event)
        self._window.connect("destroy", self.destroy)
        self._min_size = 500
        self._window.set_size_request(self._min_size, self._min_size)
        
        self.__streets = streets
      
        uimanager = gtk.UIManager()

        # Add accelerator group
        accelgroup = uimanager.get_accel_group()
        self._window.add_accel_group(accelgroup)

        # Create an ActionGroup
        actiongroup = gtk.ActionGroup('KarelWindow')
        self.actiongroup = actiongroup

        # Create actions
        actiongroup.add_actions(
            [
                ('Quit', gtk.STOCK_QUIT, '_Quit', None,
                'Quit the Program', self.quitter),
                ('File', None, '_File')
            ]
        )

        actiongroup.get_action('Quit').set_property('short-label', '_Quit')
        uimanager.insert_action_group(actiongroup, 0)
        uimanager.add_ui_from_string(self.ui_menu)
        menubar = uimanager.get_widget('/MenuBar')                           
        menubar.show()
        
        
        _box = gtk.VBox(homogeneous = False)
        _box.pack_start(menubar, False, True, 0)

        self._window.add(_box)
        _top_panel = gtk.HBox(False)
        _box.pack_start(_top_panel, False, False, 0)
        _speed_label = gtk.Label("Speed")
#        _speed_label.set_size_request(60, 20)
        _top_panel.pack_start(_speed_label, False, True, 5)
        self._speed_adjustment = gtk.Adjustment(20, 0, 100, 1)
        self._speed_adjustment.connect("value_changed", self.setSpeed, None)
        _scroller = gtk.HScale(self._speed_adjustment)
        _scroller.set_digits(0)
        _scroller.set_update_policy(gtk.UPDATE_DELAYED)
        _top_panel.pack_start(_scroller, True, True, 5)
        _speed_label.show()
        _scroller.show()
        _top_panel.show()
        
        self._area = gtk.DrawingArea()
        self._area.connect("expose_event", self.expose)
        self._area.connect("configure_event", self.configure)
       
        self._area.set_size_request(400, 400)
        self._pangolayout = self._area.create_pango_layout("")
        _scroll_window = gtk.ScrolledWindow()
        _scroll_window.add_with_viewport(self._area)
        self._inset = 30
        
        self._area.show()
        _scroll_window.show()
        self._speeder = speedCallback
        
        _box.pack_start(_scroll_window, True, True, 5)
        self._scaleFactor = 1
        self.geometry(400)
#        print "scaling with " + str(self._scaleFactor)

        self.__gBeepers = {}
        self.__contents = []
        self.__robots = []
        _box.show()
        
        self._window.show_all()
        self.config()
        self.setSize(self.__streets)
        
        
    def reset(self):
        
        self.__gBeepers = {}
        self.__contents = []
        self.__robots = []
        global pixmap
        x, y, width, height = self._area.get_allocation()
        pixmap = gtk.gdk.Pixmap(self._area.window, width, height, depth = -1)
        if self._area.window == None:
            map = self._area.get_colormap()
            pixmap.set_colormap(map)
        self.update()
        
    def clearScreen(self):
        global pixmap
        x, y, width, height = self._area.get_allocation()
        pixmap = gtk.gdk.Pixmap(self._area.window, width, height, depth = -1)
        if self._area.window == None:
            map = self._area.get_colormap()
            pixmap.set_colormap(map)
        pixmap.draw_rectangle(self._area.get_style().white_gc,True, 0, 0, width, height)
        
    def setDelay(self, amount):
        self._speed_adjustment.set_value(100 - amount)       
        
    def expose(self,widget, event):
        if event != None :
            x, y, width, height = event.area
        #    print "expose " + str(x) + " " + str(y) + " "#        pixmap.gtk_drawable_set_colormap(map) + str(width) + " " + str(height)
            window = event.window
        else :
           window = self._area.window
           x, y = 0, 0
           width, height = self._area.get_size_request()
#        print 'update' + str(x) + ' ' + str(y) + ' ' + str(width) + ' ' + str(height)
        gc = window.new_gc()
        self.simple_setSize(self.__streets)
        widget.window.draw_drawable(gc, pixmap, x, y, x, y, width, height)
        widget.queue_draw_area(x, y, width, height)
        return True

    def configure(self, widget, event):
        global pixmap
#        print str(widget)
        _streets = self.__streets
        x, y, width, height = widget.get_allocation()
#        print "configure " + str(x) + " " + str(y) + " " + str(width) + " " + str(height)
        pixmap = gtk.gdk.Pixmap(widget.window, width, height, depth = -1)
        if widget.window == None:
#            pixmap = gtk.gdk.Pixmap(widget.window, width, height, depth = -1)
            map = self._area.get_colormap()
            pixmap.set_colormap(map)
        pixmap.draw_rectangle(widget.get_style().white_gc,True, 0, 0, width, height)
        self.geometry(height)
#        if _window != None:
#        if height != self.height :
        self.setSize(_streets)
        return True

    def geometry(self, height):
        self.height = height
        self._bottom = height - self._inset
        self._left = self._inset
        self._top = self._inset
        self._right = height
        self._scaleFactor = (self._bottom - self._top)/self.__streets
        
            
    def quitter(self, x):
        gtk.main_quit()
        
    def delete_event(self, widget, event, data=None):
        return False
    
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def setSpeed(self, adjustment, other):
        value = int(adjustment.get_value())
#        print value
        self._speeder(value)
    
    def setSize(self, streets):
        self.simple_setSize(streets)
        self.labelStreetsAndAvenues(streets)
        return True
    
    def repaint(self):
        simple_setSize(self.__streets)
    
    def simple_setSize(self, streets):
        if streets > 0 :
            self.__streets = streets
        self.geometry(self.height)
        self.makeBoundaryWalls()
        self.makeStreetsAndAvenues(streets)
#        self.labelStreetsAndAvenues(streets)
        for item in self.__contents + self.__robots :
            item.moveScale()
        return True
            
    def update(self):
        self._area.emit("expose_event", None)
#        print "update"

    def config(self):
        self.configure(self._area, None)
        
    
    def run(self, task, *pargs):
#        try :
#            gobject.timeout_add(10, self.update)
            main_thread = threading.Thread(target = task, args=pargs)
            main_thread.start()
            gtk.main()
#        except Exception :
#            print "done"
            
    class Beeper:
        
        def __init__(self, street, avenue, number, window):
            self._street = street
            self._avenue = avenue
            self._number = number
            self._scaler = window._scaleToPixels 

            self._scale_factor = window._scaleFactor
            self._layout = window._pangolayout
            self._window = window
            self._size = 25 #pixels
            self._backset = int(self._size / 2)
        
        def place(self):
#            print "placing " + str(self._scale_factor)
#            sizeFactor = .5 #Change this to change beeper size. The others scale from it. 
#            placeFactor = .5 * sizeFactor
            val = str(self._number)
            if self._number < 0 :
                val = "oo"
            (x,y) = self._scaler(self._street, self._avenue)
            global pixmap
            gc = pixmap.new_gc()
#            diameter = int(self._window._scaleFactor*sizeFactor)
#            print #str(diameter
            pixmap.draw_arc(gc, True, x-self._backset, y-self._backset, self._size, self._size, 0, 64*360)
            white = gtk.gdk.color_parse("white")
            gc.set_rgb_fg_color(white)
#            font = pango.FontDescription("Geneva") #TODO fix this
#            font.set_absolute_size(18)
#            self._layout.set_font_description(font)
            
            self._layout.set_text(val)
            (x,y) = self._scaler(self._street, self._avenue)
            pixmap.draw_layout(gc, x-5,y-5, self._layout)

        
        def moveScale(self):
            self.place()
            
    class Wall:
        def __init__(self, street, avenue, isVertical,  window):
            self._street = street
            self._avenue = avenue
            self._is_vertical = isVertical
            self._scaler = window._scaleToPixels
            self._scale_factor = window._scaleFactor
            self._window = window
            self.moveScale()

        def moveScale(self):
            global pixmap
            
            factor = self._window._scaleFactor 
            gc = pixmap.new_gc()
            gc.set_line_attributes(2, gtk.gdk.LINE_SOLID, gtk.gdk.CAP_BUTT, gtk.gdk.JOIN_MITER)
            if self._is_vertical:
                (x, y) = self._scaler(self._street - .5, self._avenue + .5)
                pixmap.draw_line(gc, x, y, x, y - factor)
            else:
                (x, y) = self._scaler(self._street + .5, self._avenue - .5)
                pixmap.draw_line(gc, x, y, x + factor, y)
    
    def placeBeeper(self,street, avenue, number):
        beeper = self.Beeper(street, avenue, number, self)
        beeper.place()
        self.__gBeepers[(street, avenue)] = beeper
        self.__contents.append(beeper)
        self._area.queue_draw()
    
    def deleteBeeper(self, beeperlocation):
        beeper = self.__gBeepers.get(beeperlocation, None)
        if beeper != None :
#            beeper.deleteAll()
            self.__gBeepers.pop(beeperlocation)
            i = 0
            for b in self.__contents :
                if b == beeper :
                    break
                i+=1
            self.__contents.pop(i)
#        else:
#            print "no beeper here: " + str(beeperlocation)
        self._area.queue_draw()

    
    def placeWallNorthOf(self, street, avenue):
        self.__contents.append(self.Wall(street, avenue, False, self))
        
    def removeWallNorthOf(self, street, avenue):
        i = 0
        for wall in self.__contents:
            if wall.__class__ is self.Wall and wall._street == street and wall._avenue == avenue and not wall._is_vertical :
                self.__contents.pop(i)
#                print "gone"
                break
            i += 1           
        
    def placeWallEastOf(self, street, avenue):
        self.__contents.append(self.Wall(street, avenue, True, self))
        
    def removeWallEastOf(self, street, avenue):
        i = 0
        for wall in self.__contents:
            if wall.__class__ is self.Wall and wall._street == street and wall._avenue == avenue and wall._is_vertical :
                self.__contents.pop(i)
                break
            i += 1

    def makeBoundaryWalls(self):
        global pixmap
        (x, y) = self._scaleToPixels(.5, .5) # hardcode ok. Half way between streets
        gc = pixmap.new_gc()
        gc.set_line_attributes(2, gtk.gdk.LINE_SOLID, gtk.gdk.CAP_BUTT, gtk.gdk.JOIN_MITER)
        pixmap.draw_line(gc, x, self._inset/2, x, y) # should width depend on number of streets?
        pixmap.draw_line(gc, x, y, self._right - self._inset/2, y)
        
    def makeStreetsAndAvenues(self, streets):
        global pixmap
        red = gtk.gdk.color_parse("red")
        gc = pixmap.new_gc(foreground = red)
        gc.set_rgb_fg_color(red)
        for i in range(0, streets) :
            (x, y) = self._scaleToPixels(i+1, .5)
            (tx, ty) = self._scaleToPixels(i+1, streets + .5)
#            print "make  " + str(x) + ' ' + str(y) + ' ' + str(tx) + ' ' + str(ty)
            pixmap.draw_line(gc, x, y, tx, ty)
            (x,y) = self._scaleToPixels(.5, i + 1)
            (tx, ty) = self._scaleToPixels(streets + .5, i + 1)
            pixmap.draw_line(gc, x, y, tx, ty)
        
    def labelStreetsAndAvenues(self, streets):
        global pixmap
        gc = pixmap.new_gc()
        for i in range(streets):
            (x, y) = self._scaleToPixels(i + 1, 0)
            self._pangolayout.set_text(str(i+1))
            pixmap.draw_layout(gc, x-3,y-5, self._pangolayout)
            (x,y) = self._scaleToPixels(0, i + 1)
            pixmap.draw_layout(gc, x-3,y, self._pangolayout)
    
    def addRobot(self, street, avenue, direction, fill, outline):
        #        fill and outline are colors, default to blue, black
        robot = RobotImage(street, avenue, direction, 
                           self, fill, outline)
        self.__robots.append(robot)
        return robot # the world matches these with the actual robot objects in the model. 
    
    def moveRobot(self, robot, amount = -1):
        #If no amount is specified then it moves one block, Otherwise amount pixels, not blocks
        if amount < 0 :
            amount = self._scaleFactor
        robot.move(amount)
#        self._area.queue_draw()
        self.update()
    
    def _scaleToPixels(self, street, avenue): # origin is at corner (0,0) outside the world
        return (int(self._left + avenue*self._scaleFactor),int(self._bottom - street*self._scaleFactor))
    
    def _scaleFromPixels(self, x, y):
        scale = self._scaleFactor
        return (int(round((self._right - y)/scale))-1, int(round((x - self._left)/scale)))

    def _downScaleFromPixels(self, x, y):
        scale = self._scaleFactor
        return (int((self._right - y)/scale)-1, int((x - self._left)/scale))
    