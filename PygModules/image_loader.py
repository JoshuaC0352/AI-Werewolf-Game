import pygame
from globals import DEFAULT_W, DEFAULT_H
from PIL import Image




class PygameImage():
    image_location = None
    image = None
    position = [] #position[0] is x-axis, position[1] is y-axis

    def __init__(self, image_location, position):
        self.image_location = image_location
        self.position = position
    
    def load_image(self, GameObject):
        #TODO make the loaded image dynamically adjust to the screen resoultion with 1920x1080 as base 1:1 resolution
        height_factor = GameObject.screen_height / DEFAULT_H
        width_factor = GameObject.screen_width / DEFAULT_W

        new_width = 0
        new_height = 0

        #Get resolution
        with Image.open(self.image_location) as img:
            width, height = img.size
            new_width = width * width_factor
            new_height = height * height_factor
        
        try:
            #self.image = pygame.image.load('Images/test_sprite.png')
            load_image = pygame.image.load(self.image_location)
            self.image = pygame.transform.scale(load_image, (new_width, new_height))
        except pygame.error as e:
            print(f"Error loading image: {e}")
            pygame.quit()
            exit()
        
    def draw_image(self, screen):
        image_rect = self.image.get_rect()
        image_rect.center = (self.position[0], self.position[1])
        screen.blit(self.image, image_rect)
        #pygame.display.flip()
