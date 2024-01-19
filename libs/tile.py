from libs.blocks import Blocks
from libs.weights import Weights

class Tile():
    def __init__(self, type: Blocks = Blocks.DIRT) -> None:
        self.type = type
        self.collapsed = False
        self.possible_block = []
        self.power = 100
        self.power_multipler = 1
    
    def Set_Power_M(self):
        if self.type in Weights:
            self.power_multipler = Weights[self.type]