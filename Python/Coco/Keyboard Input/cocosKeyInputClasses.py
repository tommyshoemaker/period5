import cocos
from cocos.director import director
import pyglet



class KeyDisplay(cocos.layer.Layer):
    #Must have in order to enable mouse and keyboard events. 
    is_event_handler = True  

    def __init__(self):

        super(KeyDisplay, self).__init__()

        #Create  an empty text label at x,y
        self.text = cocos.text.Label("", x=100, y=280)
        #Add the text label to the KeyDisplay Layer
        self.add(self.text)
        #Create a variable to store the value of the key pressed
        self.key_pressed = None


    def display_text(self):
        '''This is called by on_key_press. It displays which key has been
        pressed after it is translated by piglet.
        '''
        #Translate key code to key name
        key_name = pyglet.window.key.symbol_string(self.key_pressed)
        text = 'Key Pressed is: ' + key_name + '   Code is: ' + str(self.key_pressed)
        # Update self.text
        self.text.element.text = text #Why the extra element.text?
        

    def on_key_press(self, key, modifiers):
        """This function is called when a key is pressed.
        'key' indicates which key was pressed.
        'modifiers' is a bitwise  of several constants indicating which
           modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
        """
        #sets key_pressed to the value of the key pressed
        self.key_pressed=key
        self.display_text()
        

