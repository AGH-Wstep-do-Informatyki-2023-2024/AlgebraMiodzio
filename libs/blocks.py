from enum import Enum
import random

class Blocks(Enum):
    DIRT = 1
    ICE = 2
    
Sprites = {
    Blocks.DIRT : "assets/dirt.jpg",
    Blocks.ICE : "assets/ice.jpg"
}

Rules = {
    Blocks.DIRT : {
        95: Blocks.DIRT,
        5: Blocks.ICE
    },
    Blocks.ICE : {
        95: Blocks.ICE,
        5: Blocks.DIRT
    }
}

def RandomBlock(options):
    rand_list = []
    
    for key, value in options.items():
        rand_list += [value] * key
        
    return random.choice(rand_list)