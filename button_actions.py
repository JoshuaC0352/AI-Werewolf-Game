import sys
from enum import Enum
from inquisitor_init import Game
from AI_Interface.ai_interface import query_local_model

class ButtonActions(Enum):
    INQUIRE = 1
    DISABLE = 2
    QUIT = 3
    GAMESCENE = 4
    SEND_QUERY = 5

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
                
    elif button_action == ButtonActions.GAMESCENE:
        
        swapScene("GameScene", GameObject)
    
    elif button_action == ButtonActions.QUIT:
        sys.exit()
    
    elif button_action == ButtonActions.SEND_QUERY:
        
        #NOTE: Hardcoded for now.  Will fix later
        prompt = "You are a werewolf posing as a villager.  The inquisitor is trying to figure out if you are a werewolf.  Answer his question in a way that will convinvce him you are a villager.  Here is his question: \n\n"

        response = query_local_model(prompt + arguments[1].compile_text_lines())
        arguments[0].activate_text_field(event=None, add_text=response, screen=GameObject.screen)
        
    
    else:
        print("Button Inactive")
        pass
