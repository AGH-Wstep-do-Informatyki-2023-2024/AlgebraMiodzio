from libs.blocks import Blocks

class Tile():
    def __init__(self, type: Blocks = Blocks.DIRT) -> None:
        self.type = type
        self.collapsed = False
        self.possible_block = []
        self.power = 100
        self.power_multipler = 1
    
    def Set_Power_M(self):
        
        if(self.type == Blocks.WATER):
            self.power_multipler = 1
        if(self.type == Blocks.GLOWSTONE):
            self.power_multipler = 0.1
        if(self.type == Blocks.ICE):
            self.power_multipler = 0.05
        if(self.type == Blocks.GRASS):
            self.power_multipler = 2
        if(self.type == Blocks.DIAMOND):
            self.power_multipler = 0.01
        if(self.type == Blocks.COAL):
            self.power_multipler = 0.01