from enum import Enum
import random
import pygame as pg

class Blocks(Enum):
    DIRT = 1
    ICE = 2
    COAL = 3
    DIAMOND = 4
    GLOWSTONE = 5
    OBSIDIAN = 6
    PUMPKIN = 7
    SNOW = 8
    STONE = 9
    
img = lambda x: pg.image.load(x)
    
Sprites = {
    Blocks.DIRT : img("assets/dirt.jpg"),
    Blocks.ICE : img("assets/ice.jpg"),
    Blocks.COAL : img("assets/coal.jpg"),
    Blocks.DIAMOND : img("assets/diamond.jpg"),
    Blocks.GLOWSTONE : img("assets/glowstone.jpg"),
    Blocks.OBSIDIAN : img("assets/obsidian.jpg"),
    Blocks.PUMPKIN : img("assets/pumpkin.jpg"),
    Blocks.SNOW : img("assets/snow.jpg"),
    Blocks.STONE : img("assets/stone.jpg")
}

SpriteSize = (160, 160)

Rules = {
    Blocks.DIRT: {
        70: Blocks.DIRT,
        5: Blocks.ICE,
        5: Blocks.COAL,
        5: Blocks.STONE,
        5: Blocks.OBSIDIAN,
        1: Blocks.DIAMOND,
        3: Blocks.PUMPKIN,
        1: Blocks.GLOWSTONE,
    },
    Blocks.ICE: {
        90: Blocks.ICE,
        10: Blocks.DIRT
    },
    Blocks.COAL: {
        50: Blocks.COAL,
        50: Blocks.STONE
    },
    Blocks.DIAMOND: {
        10: Blocks.DIAMOND,
        40: Blocks.OBSIDIAN,
        50: Blocks.GLOWSTONE
    },
    Blocks.GLOWSTONE: {
        60: Blocks.GLOWSTONE,
        40: Blocks.PUMPKIN
    },
    Blocks.OBSIDIAN: {
        25: Blocks.OBSIDIAN,
        25: Blocks.SNOW,
        50: Blocks.GLOWSTONE
    },
    Blocks.PUMPKIN: {
        50: Blocks.PUMPKIN,
        50: Blocks.GLOWSTONE
    },
    Blocks.SNOW: {
        70: Blocks.SNOW,
        30: Blocks.ICE
    },
    Blocks.STONE: {
        60: Blocks.STONE,
        25: Blocks.COAL,
        15: Blocks.OBSIDIAN,
    }
}


#Revers Rules
ReRules = {
    Blocks.DIRT: {
        Blocks.DIRT: 70,
        Blocks.ICE: 5,
        Blocks.COAL:     5,
        Blocks.STONE:    5,
        Blocks.OBSIDIAN: 5,
        Blocks.DIAMOND:  1,
        Blocks.PUMPKIN:  3,
        Blocks.GLOWSTONE : 1, 
    }
}















def RandomBlock(options):
    rand_list = []
    
    for key, value in options.items():
        rand_list += [value] * key
        
    return random.choice(rand_list)