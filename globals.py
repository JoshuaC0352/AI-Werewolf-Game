import random
import tkinter
import globals

DEFAULT_W = 1920
DEFAULT_H = 1080
VILLAGER_COUNT = 6


#COLORS
HILIGHT_GREEN = (50,255,50)
GRAY_1 = (50,50,50)
GRAY_2 = (180, 180, 180)
BURGENDY = (120,50,75)

LOCAL_LLM = None

"""
    This function will create a list of unique int in the provided range.
    The list size will be the provided size.
"""
def create_random_list(list_size : int, range_count : int):
    
    #list size and range should be of type int
    
    i = 1
    num_list = []
    while(i<=range_count):
        
        random_integer = random.randint(0, list_size-1)
        if random_integer not in num_list:
            num_list.append(random_integer)
            i+=1
    
    return num_list

        

