import pygame

class PygameTextField():
    # position = [] # 0 index is x-axis, 1 index is y-axis
    # # width = None
    # # height = None
    # font = None
    # input_box = None # x, y, width, height
    # color_inactive = None
    # color_active = None
    # background_color = None
    # active = True
    # #text = ""
    # text_lines = []
    # line_index = None
    # text_color = None
    # box_active = True # determines whether the user can add text to the box
    # string_index = -1
    # add_text = None
    # text_lock = False
    
    def __init__(self, position=[0,0], width=0, height=0, font=32, screen=None, color_inactive=(pygame.Color('lightskyblue3')), 
                 color_active=(pygame.Color('green')), background_color=(30,30,30), text_color=('lightskyblue3'), box_active=True):

        pygame.init()
        
        #DECLARE INSTANT VARIABLES HERE:
        self.position = [] # 0 index is x-axis, 1 index is y-axis
        self.active = True
        self.text_lines = []
        self.box_active = True # determines whether the user can add text to the box
        self.string_index = -1
        #TODO: This should default to True, but is not updating when being accesed remotely.  Investigate
        self.text_lock = False
        self.add_text = None

        
        self.font = font
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.background_color = background_color
        self.font=pygame.font.Font(None, 32)
        self.input_box = pygame.Rect(position[0], position[1], width, height)
        #active = False
        #self.text = ''
        #initialize the first line for rendering
        self.text_lines.append("")
        self.line_index = 0
        self.text_color = text_color
        self.box_active = box_active

    def compile_text_lines(self):
        compiled_text = ""
        for line in self.text_lines:
            compiled_text += line

        return compiled_text


    def add_character_to_box(self, event=None, new_char=None):
        
            
        line_update = True
        if self.active:
            #print(f"Key pressed {event.unicode}")
            if event.key == pygame.K_RETURN:
                #Ignore the enter key
                pass
            elif event.key == pygame.K_BACKSPACE:
                self.text_lines[self.line_index] = self.text_lines[self.line_index][:-1]
                if self.text_lines[self.line_index] == "":
                    print("Line is empty.")
                    #Do not pop if we are on the first line
                    if self.line_index != 0:
                        self.text_lines.pop()
                        self.line_index -= 1
                        #Don't due a line update when a line is removed, so we don't recreate the the line we just deleted
                        line_update = False
                        
            else:
                self.text_lines[self.line_index] += event.unicode
                print(self.text_lines[self.line_index])
                #print(self.line_index)
        
        elif event == None:
            self.text_lines[self.line_index] += new_char

        return line_update



    def activate_text_field(self, screen, event=None, add_text=None):
        
        line_update = False
        new_char = None
        #If a new block of text needs to be added, this trigger the necessary steps to add it to the text field
        if add_text != None and not self.text_lock:
            #Adding new string
            
            if self.string_index == -1:
                self.string_index = 0
                #if the same text block is added multiple times, this will prevent it from being be reset.
                self.text_lock = True
                self.add_text = add_text
        
        elif self.add_text != None:
            #Check to see if the entire string has been added yet
            if self.string_index == len(self.add_text):
                self.string_index = -1
                self.add_text = None
            else:               
                new_char = self.add_text[self.string_index]
                self.string_index += 1

        
        
        if event != None and event.type == pygame.KEYDOWN:
            line_update = self.add_character_to_box(event=event, new_char=None)
        elif new_char != None:
            line_update = self.add_character_to_box(event=None, new_char=new_char)
        

        color = self.color_inactive
        if event != None:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_box.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
        
        color = self.color_active if self.active else self.color_inactive
        pygame.draw.rect(screen, self.background_color, self.input_box, 0)
        #Draw the box outline
        #TODO: When the text box is selected, change the border color to a highlight color
        pygame.draw.rect(screen, color, self.input_box, 2) # Draw outline
        

        txt_surface = None #used to retain the surface of the final text line
        position = 0
        for line in self.text_lines:
            txt_surface = self.font.render(line, True, self.text_color)
            screen.blit(txt_surface, (self.input_box.x, self.input_box.y + (position * txt_surface.get_height())))
            position += 1
        
        #print(line_update)
        if txt_surface.get_width() > self.input_box.w - 10 and line_update:
            #add a new line to the text lines
            self.text_lines.append("")
            #set the pointer to the next line
            self.line_index += 1
            line_update = False

        #TODO: Implement a check that prevents the text from overfilling the bottom of the text box.
        


