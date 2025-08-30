from PygModules.image_loader import PygameImage
from PygModules.pygame_button import PygameButton
from button_actions import ButtonActions
from Scenes.pygame_scene import PygameScene
from globals import (HILIGHT_GREEN, GRAY_1, BURGENDY, GRAY_2)
import time
import pygame

class GameScene(PygameScene):
    
    def __init__(self):
        super().__init__()

    def start(self, GameObject):
        self.running = True
        self.GameObject = GameObject
        # Game loop
        #STANDARD_BUTTON_WIDTH = GameObject.SC

        screen_width = GameObject.screen_width
        screen_height = GameObject.screen_height


        first_button = PygameButton(position=[screen_width*.05,screen_height*.1], width=screen_height*.1, height=screen_height*.03, 
                                    font=screen_height*.02, button_text="EXIT", button_color=GRAY_2, 
                                    font_color=GRAY_1, background_color=BURGENDY, call_action=ButtonActions.QUIT, 
                                    call_arguments=None)
        
        inquisitor_position = [screen_width * .5, screen_height * .5]
        inquisitor_image = PygameImage(image_location='Images/inquisitor.png', 
                                        position=[inquisitor_position[0], inquisitor_position[1]])
        inquisitor_image.load_image(GameObject)

        background_image = PygameImage(image_location='Images/background.png', 
                                    position=[screen_width * .5, screen_height * .5])
        background_image.load_image(GameObject)

        #generate villager images
        
        player_buttons = []
        i = 0
        for villager in GameObject.active_vilagers:
            
            image = PygameImage(image_location=villager.image, position=villager.position)
            player_buttons.append(PygameButton(position=villager.position, width=screen_width*.11, 
                                height=screen_height*.2, background_color=HILIGHT_GREEN, call_action=ButtonActions.INQUIRE, 
                                call_arguments=[villager], GameObject=GameObject))

            image.load_image(GameObject)
            GameObject.villager_images.append(image)

        # Fill the background
        # GameObject.screen.fill((0, 0, 0)) # White background

        background_image.draw_image(GameObject.screen)

        while self.running:
            
            
            for event in pygame.event.get():
            
                first_button.activate_button(event, GameObject.screen)
            
                #Draw the buttons before the players, so they are behind them.
                for button in player_buttons:
                    button.activate_button(event, GameObject.screen)

            for v_image in GameObject.villager_images:
                v_image.draw_image(GameObject.screen)

            inquisitor_image.draw_image(GameObject.screen)

            #print("Game Scene running")

            pygame.display.flip()
    
    def stop(self):
        
        self.running = False