from karel.robota import *

def task():
    world.readWorld("test.kwld")
    world.setDelay(30)
if __name__ == '__main__' :
    world.setDelay(30)
    window().run(task)
