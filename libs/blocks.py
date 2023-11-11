from enum import Enum
from libs.rules import rules

class Blocks(Enum):
    DIRT = 1
    ICE = 2
    
class Block():
    def __init__(self, type: Blocks = Blocks.DIRT) -> None:
        self.type = type
        self.x = 0
        self.y = 0
        self.options = rules[self.type]
        self.collapsed = False
        
    def __repr__(self) -> str:
        return f"{str(self.type).split('.')[1]}"