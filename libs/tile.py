from libs.blocks import Blocks, Rules, Printable, RandomBlock

class Tile():
    def __init__(self, type: Blocks = Blocks.DIRT) -> None:
        self.type = type
        self.options = Rules[self.type]
        self.name = Printable[self.type]
        self.collapsed = False
        
    def __repr__(self) -> str:
        return f"{str(self.type.name)}"
    
    def ApplyType(self, type: Blocks):
        self.type = type
        self.options = Rules[type]
        self.name = Printable[self.type]
        
    def ApplyRules(self, origin):
        if self.collapsed:
            return
        
        self.ApplyType(RandomBlock(origin.options))
        self.collapsed = True