from libs.blocks import Blocks, Rules, RandomBlock

class AltTile():
    def __init__(self, type: Blocks = Blocks.DIRT) -> None:
        self.type = type
        self.collapsed = False
        self.possible_block = []
        self.power = 100
        self.power_multipler = 1
    
    def Set_Power_M():
        if(type == Blocks.WATER):
            power_multipler = 100
        if(type == Blocks.GLOWSTONE):
            power_multipler = 0.1
        if(type == Blocks.ICE):
            power_multipler = 0.05
        if(type == Blocks.GRASS):
            power_multipler = 20
        if(type == Blocks.DIAMOND):
            power_multipler = 0.01
        if(type == Blocks.COAL):
            power_multipler = 0.01
    
           

        

class Tile():
    def __init__(self, type: Blocks = Blocks.DIRT) -> None:
        self.type = type
        self.options = Rules[self.type]
        self.collapsed = False
        
    def __repr__(self) -> str:
        return f"{str(self.type.name)}"
    
    def ApplyType(self, type: Blocks):
        self.type = type
        self.options = Rules[type]
        
    # def ApplyRules(self, origin):
    #     if self.collapsed:
    #         return
        
    #     self.ApplyType(RandomBlock(origin.options))
    #     self.collapsed = True
        
def ApplyRules(tile: Tile, target: Tile):
    if target.collapsed:
        return
        
    target.ApplyType(RandomBlock(tile.options))
    target.collapsed = True