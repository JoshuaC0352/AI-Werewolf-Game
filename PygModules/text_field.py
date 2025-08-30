import pygame

class PygameTextField():
    position = [] # 0 index is x-axis, 1 index is y-axis
    # width = None
    # height = None
    font = None
    input_box = None # x, y, width, height
    color_inactive = None
    color_active = None
    background_color = None
    active = True
    text = ""
    
    def __init__(self, position=[0,0], width=0, height=0, font=32, screen=None, color_inactive=(pygame.Color('lightskyblue3')), 
                 color_active=(pygame.Color('dodgerblue2')), background_color=(30,30,30)):

        
        
        pygame.init()
        self.font = font
        self.color_inactive = color_inactive
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.background_color = background_color
        self.font=pygame.font.Font(None, 32)
        self.input_box = pygame.Rect(position[0], position[1], width, height)
        #active = False
        text = ''


    def activate_text_field(self, event, screen):
        
        
        color = self.color_inactive
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            
            if self.active:
                print(f"Key pressed {event.unicode}")
                if event.key == pygame.K_RETURN:
                    print(self.text) # Process input when Enter is pressed
                    self.text = '' # Clear text or handle as needed
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    print(self.text)

        
        
        # Drawing
        
        
        #screen.fill(self.background_color) # Background color
        
        
        
        #Fill rectangle with background color
        pygame.draw.rect(screen, self.background_color, self.input_box, 0)
        #Draw the box outline
        #TODO: When the text box is selected, change the border color to a highlight color
        pygame.draw.rect(screen, color, self.input_box, 2) # Draw outline

        #Fill box with text
        
        txt_surface = self.font.render(self.text, True, color)
        if txt_surface.get_width() > self.input_box.w:
            self.text += "\n"
        screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
        

        
        #pygame.display.flip()

