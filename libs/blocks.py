from enum import Enum
import random
import pygame as pg

class Blocks(Enum):
    DIRT = 1
    ICE = 2
    
img = lambda x: pg.image.load(x)
    
Sprites = {
    Blocks.DIRT : img("assets/dirt.jpg"),
    Blocks.ICE : img("assets/ice.jpg")
}

SpriteSize = (160, 160)

Rules = {
    Blocks.DIRT : {
        70: Blocks.DIRT,
        30: Blocks.ICE
    },
    Blocks.ICE : {
        90: Blocks.ICE,
        10: Blocks.DIRT
    }
}

def RandomBlock(options):
    rand_list = []
    
    for key, value in options.items():
        rand_list += [value] * key
        
    return random.choice(rand_list)