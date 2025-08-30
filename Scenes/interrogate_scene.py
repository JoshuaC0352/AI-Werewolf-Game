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
        
        tf_position = [250*width_scale, 250*height_scale]
        tf_width = 500 * width_scale
        tf_height = 500 * height_scale
        text_field = PygameTextField(position=tf_position, width=tf_width, height=tf_height)

        self.running = True

        while self.running:
            
            for event in pygame.event.get():
                returnButton.activate_button(event, GameObject.screen)
                text_field.activate_text_field(event, GameObject.screen)
                
            
            villager_image.draw_image(GameObject.screen)

            pygame.display.flip()

    def stop(self):
        self.running = False



