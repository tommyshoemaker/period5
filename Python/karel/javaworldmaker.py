
''' Copyright 2008 Joseph Bergin
License: Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License

Demonstrates a direct connection to the KJR code. Works only in JYthon
Creates and shows the KJR world builder.
Note that this worldbuilder makes world files compatible with the Python version
Requires the kareltherobot.jar fils.
'''
from kareltherobot import WorldBuilder
from kareltherobot import World

class WorldMaker:
    
    def show(self):
        World.setVisible(1)
        builder = WorldBuilder(0)
        
    def setSize(self,streets, avenues):
        World.setSize(streets, avenues)

def task():
    builder = WorldMaker()
    builder.setSize(12, 12)
    builder.show()       
        
if __name__ == '__main__' :
    builder = WorldMaker()
    builder.setSize(12, 12)
    builder.show()