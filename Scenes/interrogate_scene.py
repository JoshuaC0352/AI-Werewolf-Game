from inquisitor_init import Game
from villager_class import Villager
from Scenes.pygame_scene import PygameScene
from PygModules.image_loader import PygameImage
from PygModules.pygame_button import PygameButton
from button_actions import ButtonActions
from globals import BURGENDY, GRAY_1, GRAY_2, DEFAULT_H, DEFAULT_W
from PygModules.text_field import PygameTextField
import pygame

class InterrogateScene(PygameScene):

    def __init__(self):
        super().__init__()

        self.response_text = "I'm innocent, I swear.  I'm not a werewolf.  I would never eat another human being.  I promise.  Why won't you believe me?  Didn't everyone tell you how trustworthy I am!"

    def start(self, GameObject):
        print("Interrogate Scene Started>")
        self.GameObject = GameObject

        villager_portrait_pos = [GameObject.screen_width * .1, GameObject.screen_height * .1]

        villager_image = PygameImage(image_location=GameObject.selected_villager.image, position=villager_portrait_pos)
        villager_image.load_image(GameObject)

        height_scale = GameObject.screen_height / DEFAULT_H
        width_scale = GameObject.screen_width / DEFAULT_W

        
        GameObject.screen.fill((210, 180, 140)) # Black background
        #background_image.draw_image(GameObject.screen)
        returnButtonPos = [GameObject.screen_width * .1, GameObject.screen_height - (GameObject.screen_height *.1)]
        returnButtonWidth = 100*height_scale
        returnButtonHeight = 40*width_scale
        returnButton = PygameButton(position=returnButtonPos, width=returnButtonWidth, height=returnButtonHeight, font=0, 
                                    button_text="Back", background_color=BURGENDY, font_color=GRAY_1, button_color=GRAY_2, 
                                    call_action=ButtonActions.GAMESCENE, GameObject=GameObject)

        interrogate_button_pos = [GameObject.screen_width * .18, GameObject.screen_height - (GameObject.screen_height * .275)]
        interrogate_button_width = 200*height_scale
        interrogate_button_height = 45*width_scale

        


        
        tf_position = [250*width_scale, 250*height_scale]
        rf_position = [1000*width_scale, 250*height_scale]
        tf_width = 500 * width_scale
        tf_height = 500 * height_scale
        rf_width = 500 * width_scale
        rf_height = 500 * height_scale

        text_field = PygameTextField(position=tf_position, width=tf_width, height=tf_height)
        
        
        res_text_field = PygameTextField(position=rf_position, width=rf_width, height=rf_height)
        res_text_field.active = False
        #Unlock text adding
        #TODO: Investigate why this isn't working.
        res_text_field.text_lock = False

        interrogate_button = PygameButton(position=interrogate_button_pos, width=interrogate_button_width, 
                             height=interrogate_button_height, font=0, button_text="INTERROGATE", background_color=BURGENDY, 
                             font_color=GRAY_1, button_color=GRAY_2, call_action=ButtonActions.SEND_QUERY, GameObject=GameObject,
                             call_arguments=[res_text_field, text_field])

        self.running = True

        while self.running:
            
            for event in pygame.event.get():
                returnButton.activate_button(event=event, screen=GameObject.screen)
                text_field.activate_text_field(event=event, screen=GameObject.screen)
                interrogate_button.activate_button(event=event, screen=GameObject.screen)
            
            
            #res_text_field.activate_text_field(event=None, add_text=self.response_text, screen=GameObject.screen)
            res_text_field.activate_text_field(event=None, add_text=None, screen=GameObject.screen)
            
            
            villager_image.draw_image(GameObject.screen)

            pygame.display.flip()

    def stop(self):
        self.running = False



