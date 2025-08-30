import sys
from enum import Enum
from inquisitor_init import Game

class ButtonActions(Enum):
    INQUIRE = 1
    DISABLE = 2
    QUIT = 3
    GAMESCENE = 4

def swapScene(next_scene : str, GameObject : Game):

    print(next_scene)
    for scene in GameObject.all_scenes:
        
        if type(scene).__name__ == next_scene:
            GameObject.active_scene.stop()
            GameObject.next_scene = scene

def button_actions(button_action : ButtonActions, GameObject : Game, arguments : list):
    
    if button_action == ButtonActions.INQUIRE:

        GameObject.selected_villager = arguments[0]
        swapScene("InterrogateScene", GameObject)
                
    if button_action == ButtonActions.GAMESCENE:
        
        swapScene("GameScene", GameObject)
    
    elif button_action == ButtonActions.QUIT:
        sys.exit()
    
    else:
        print("Button Inactive")
        pass
