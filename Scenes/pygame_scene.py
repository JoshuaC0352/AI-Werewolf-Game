#Used for creating a new PygameScene
class PygameScene:
    running = False #Used to stop rendering a scene that is no longer actinve
    GameObject = None #pygame game object
    draw_changes = True

    def __init__(self):
        pass
    
    #start the scene
    def start(self):
        print("This object has no scene description!")
    def stop(self):
        print("Can't stop the scene.  Override this function")
        