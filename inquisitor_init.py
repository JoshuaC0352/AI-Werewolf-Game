from villager_class import Villager
from villager_class import VillagerType
#from pygame_button import PygameButton
#from image_loader import PygameImage
#from button_actions import ButtonActions
from AI_Interface.ai_interface import load_local_model, load_chatGPT
from globals import create_random_list
from globals import VILLAGER_COUNT


import pygame
import os
import string
import sys
import tkinter

START_PROMPT = """
A woman came shouting and crying in the village center.  Her husband was out late
the night before and never came home.  She found him the next morning brutally
mauled to death.  After inspecting the body, it was clear.  There is a werewolf
among them.  They must discover who it is before nightfall.  They pick their
fastest horse, and send a messanger to summon "The Inquisitor."  If anyone can
find out who the werewolf is, it would be him!
"""

INSTRUCTIONS = """
You are the Inquisitor, you are arrive at the village shortly after noon.  Time is of the essence.
You must discover the werewolf, and expose him before nightfall.  If you don't you may not
survive to see the next sunrise.  If you incorrectly accuse an innocent villager, you will hang
next.  The stakes are high, and time is short.  All of the villagers have gathered, and it is time
to start your questioning.
"""

MENU_ITEMS = """
INQUIRE - Ask a villager a question
LOG - see the conversation log up to this point
QUIT - exit the game
VILLAGERS - list all villagers
"""

ALL_VILLAGERS = []

def clear_screen():
    #for windows
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def valid_string(check_string):
    for char in check_string:
        if not (char.isalnum() or char in string.punctuation):
            return False
    
    return True

def isVillager(villager_name):
    for villager in ALL_VILLAGERS:
        if villager.name.upper() == villager.upper():
            return True
    
    return False

def accuse_player(accused_player):
    for villager in ALL_VILLAGERS:
        if villager.name == accuse_player:
            if villager.villager_type == VillagerType.WEREWOLF:
                print("VICOTRY!")
            else:
                print("FAIL!")
    
    sys.exit()



class Game:
    screen = None
    
    villager_images = []
    active_vilagers = []
    start_positions = []

    screen_width = 1920
    screen_height = 1080

    all_scenes = []

    selected_villager = None #Pointer to villager selected for interrogation

    active_scene = None
    next_scene = None
        
    #Get the resolution of the screen app is launching from
    def set_resolution(self):
        
        try:
            root = tkinter.Tk()
            
            self.screen_width = root.winfo_screenwidth()
            self.screen_height = root.winfo_screenheight()

            print("**************************", self.screen_width, self.screen_height)

        except:
            print("ERROR: Failed to detect screen resolution, using default 1920x1080")
    
    def __init__(self, all_scenes):

        self.all_scenes = all_scenes

        self.set_resolution()
        
        
        #create villager positions
        self.start_positions.append([self.screen_width * .25, self.screen_height * .5])
        self.start_positions.append([self.screen_width * .75, self.screen_height * .5])
        self.start_positions.append([self.screen_width * .38, self.screen_height * .2])
        self.start_positions.append([self.screen_width * .63, self.screen_height * .2])
        self.start_positions.append([self.screen_width * .38, self.screen_height * .75])
        self.start_positions.append([self.screen_width * .63, self.screen_height * .75])
        
        load_local_model()
        #load_chatGPT()
        
        # Initialize Pygame
        pygame.init()

        print("****************************", self.screen_width, self.screen_height)
        # Set up the display
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("PNG Image Example")

        #Create villagers

        ALL_VILLAGERS.append(Villager(villager_type=VillagerType.WEREWOLF, name="Farmer",
                            position = [0, 0],
                            image="Images/Male Villager.png"))
        ALL_VILLAGERS.append(Villager(villager_type=VillagerType.AGENT, name="Farmer's Wife",
                            position = [0, 0],
                            image="Images/Female Villager.png"))
        ALL_VILLAGERS.append(Villager(villager_type=VillagerType.VILLAGER, name="Farmer's Daughter",
                            position= [0, 0],
                            image="Images/Daughter Villager.png"))
        ALL_VILLAGERS.append(Villager(villager_type=VillagerType.VILLAGER, name="Farmer's Son",
                            position=[0, 0],
                            image="Images/Villager Son.png"))
        ALL_VILLAGERS.append(Villager(villager_type=VillagerType.VILLAGER, name="Blacksmith",
                            position=[0, 0],
                            image="Images/Blacksmith.png"))
        ALL_VILLAGERS.append(Villager(villager_type=VillagerType.VILLAGER, name="Old Hag",
                            position=[0, 0],
                            image="Images/Old Hag.png"))
        ALL_VILLAGERS.append(Villager(villager_type=VillagerType.VILLAGER, name="Vilalge Elder",
                            position=[0, 0],
                            image="Images/Village Elder.png"))
        ALL_VILLAGERS.append(Villager(villager_type=VillagerType.VILLAGER, name="Bailiff",
                            position=[0, 0],
                            image="Images/Bailiff.png"))
        ALL_VILLAGERS.append(Villager(villager_type=VillagerType.VILLAGER, name="Mayor",
                            position=[0, 0],
                            image="Images/Village Mayor.png"))
        ALL_VILLAGERS.append(Villager(villager_type=VillagerType.VILLAGER, name="Barmaid",
                            position=[0, 0],
                            image="Images/Barmaid.png"))
        ALL_VILLAGERS.append(Villager(villager_type=VillagerType.VILLAGER, name="Innkeeper",
                            position=[0, 0],
                            image="Images/Innkeeper.png"))

        villager_selection = create_random_list(len(ALL_VILLAGERS), VILLAGER_COUNT)
        
        #Add the selected villagers to the game play list
        position = 0
        for number in villager_selection:
            self.active_vilagers.append(ALL_VILLAGERS[number])
            ALL_VILLAGERS[number].position = self.start_positions[position]
            position += 1

        #Load the model at initialization
        
    
    def run(self):

        running = True

        while running:
            if self.active_scene != self.next_scene:

                
                self.active_scene = self.next_scene
                self.active_scene.start(self)

        pygame.quit()
        

if __name__ == '__main__':
    
    #Put this here to prevent circular import
    from Scenes.game_scene import GameScene
    from Scenes.interrogate_scene import InterrogateScene

    scene_list = []
    scene_list.append(GameScene())
    scene_list.append(InterrogateScene())
    game = Game(scene_list)
    #Set the main game scene to the starting scene
    game.next_scene = scene_list[0]
    game.run()
    #game.load_images()
