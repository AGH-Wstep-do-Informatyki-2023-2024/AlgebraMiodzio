from libs.blocks import Blocks, Rules

class Tile():
    def __init__(self, type: Blocks = Blocks.DIRT) -> None:
        self.type = type
        self.options = Rules[self.type]
        self.collapsed = False
        
    def __repr__(self) -> str:
        return f"{str(self.type.name)}"