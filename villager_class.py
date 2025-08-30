from enum import Enum

class VillagerType(Enum):
    WEREWOLF = 1 #is the werewolf
    VILLAGER = 2 #wants to find the werewolf
    DISTURBED = 3 #wishes to die
    AGENT = 4 #wants to help the werewolf survive


class Villager:
    villager_type = None
    name = None
    position = [] #position[0] is x axis, position[1] is y axis
    image = "" #disk location of villager
    
    def __init__(self, villager_type, name, position, image):
        self.villager_type = villager_type
        self.name=name
        self.position = position
        self.image = image

    def describe_role(self):
        role_description = ""
        if self.villager_type == VillagerType.WEREWOLF:
            role_description = "The inquisitor has been summoned to find out who the werewolf is, and have him hung in the"
            "village square before nightfall."
            "You are the werewolf.  Your primary purpose is to survive until nightfall, so you can slay the inquisitor."
            "You will use any means necessary to conceal your identity.  Ideally you would like to convince to inquisitor that"
            "another villager is in fact the werewolf."
        elif self.villager_type == VillagerType.AGENT:
            role_description = "You are the agent.  Your primary purpose is the protect the werewolf at all costs.  You will use any"
            "means at your disposal to do so, even if it means convincing the inquistor that you are the werewolf instead.  Or you may"
            "convince the inquisitor that another villager is the werewolf."
        elif self.villager_type == VillagerType.VILLAGER:
            role_description = "You are a villager.  You are innocent.  Others may accuse you of being a werewolf, you must successfully"
            "deflect their accusations.  You don't want to be accused of a werewolf, but you also want the werewolf to be exposed for the"
            "safety of the village."
        elif self.villager_type == VillagerType.DISTURBED:
            "You are depressed and suicidal.  You do not care about the safety of the village.  Your only goal is to convince the rest of"
            "the village that you are in fact the werewolf.  That way they will hang you at nightfall, you will use any means to convice"
            "the village that you are the werewolf."

    