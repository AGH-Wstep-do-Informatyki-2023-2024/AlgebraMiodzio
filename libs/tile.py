from libs.blocks import Blocks

class Tile():
    def __init__(self, type: Blocks = Blocks.DIRT) -> None:
        self.type = type
        self.collapsed = False
        self.possible_block = []
        self.power = 100
        self.power_multipler = 1
    
    def Set_Power_M(self):
        if(type == Blocks.WATER):
            self.power_multipler = 100
        if(type == Blocks.GLOWSTONE):
            self.power_multipler = 0.1
        if(type == Blocks.ICE):
            self.power_multipler = 0.05
        if(type == Blocks.GRASS):
            self.power_multipler = 20
        if(type == Blocks.DIAMOND):
            self.power_multipler = 0.01
        if(type == Blocks.COAL):
            self.power_multipler = 0.01