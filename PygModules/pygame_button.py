import pygame
import time
from button_actions import button_actions, ButtonActions
from inquisitor_init import Game

class PygameButton:
    
    position = [] #Position 0 is x axis, position 1 is y axis
    width = None
    height = None
    font = None #Color of the button's font
    button_text = None
    button_dimensions = None
    button_color = None #Default color of button
    background_color = None #Color that will display when mousing over button
    pyg_text = None
    call_action = None
    call_arguments = None
    temp_enable = True
    GameObject = None

    def __init__(self, position=[0,0], width=0, height=0, font=0, button_text="", button_color=(0,0,0), font_color=(0,0,0), 
                 background_color=(0,0,0), call_action=ButtonActions.DISABLE, call_arguments=None, GameObject=None):
        
        self.position = position
        self.width = width
        self.height = height
        self.font = font
        self.button_text = button_text
        #Centering the old fashioned way, since this seems the be the only thing that is working.
        self.button_dimensions = pygame.Rect(position[0] - (width/2), position[1] - (height/2), self.width, self.height)
        self.button_color = button_color
        self.background_color = background_color
        font = pygame.font.Font(None, 36)
        self.pyg_text = font.render(button_text, True, font_color)
        self.call_action = call_action
        self.call_arguments = call_arguments
        self.GameObject = GameObject
    
    def activate_button(self, event, screen):
        
        current_color = self.button_color
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_dimensions.collidepoint(event.pos):
                #Added the sleep so the button press doesn't spam
                if self.temp_enable:
                    button_actions(self.call_action, GameObject=self.GameObject, arguments = self.call_arguments)
                #Without this, the button will spam action calls on a single button click
                self.temp_enable = False

        if event.type == pygame.MOUSEBUTTONUP:
            #re-enables the button for the next click
            self.temp_enable = True
            
        if event.type == pygame.MOUSEMOTION:
            if self.button_dimensions.collidepoint(event.pos):
                current_color = self.background_color
                #else
        
        
        pygame.draw.rect(screen, current_color, self.button_dimensions)
        
        text = self.pyg_text.get_rect(center=self.button_dimensions.center)

        screen.blit(self.pyg_text, text)
        #pygame.display.flip()
        