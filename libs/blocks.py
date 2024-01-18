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
    WATER = 10
    GRASS = 11
    
SpriteSize = 10
    
def img(path):
    tmp = pg.image.load(path)
    tmp = pg.transform.scale(tmp, (SpriteSize, SpriteSize))
    return tmp

Sprites = {
    Blocks.DIRT : img("assets/dirt.jpg"),
    Blocks.ICE : img("assets/ice.jpg"),
    Blocks.COAL : img("assets/coal.jpg"),
    Blocks.DIAMOND : img("assets/diamond.jpg"),
    Blocks.GLOWSTONE : img("assets/glowstone.jpg"),
    Blocks.OBSIDIAN : img("assets/obsidian.jpg"),
    Blocks.PUMPKIN : img("assets/pumpkin.jpg"),
    Blocks.SNOW : img("assets/snow.jpg"),
    Blocks.STONE : img("assets/stone.jpg"),
    Blocks.WATER: img("assets/water.jpg"),
    Blocks.GRASS: img("assets/grass.jpg")
}

Rules = {
    Blocks.DIRT: {
        #70: Blocks.DIRT,
        70: Blocks.GRASS,
        5: Blocks.ICE,
        10: Blocks.STONE,
        5: Blocks.OBSIDIAN,
        2: Blocks.PUMPKIN,
        8: Blocks.WATER
        
        
    },
    Blocks.ICE: {
        60: Blocks.DIRT,
        20: Blocks.STONE,
        5: Blocks.OBSIDIAN,   
        25: Blocks.WATER
    },
    Blocks.COAL: {
        #50: Blocks.COAL,
        100: Blocks.STONE
    },
    Blocks.DIAMOND: {
        100: Blocks.STONE
    },
    Blocks.GLOWSTONE: {
        #60: Blocks.GLOWSTONE,
        2: Blocks.PUMPKIN,
        90: Blocks.DIRT,
        100: Blocks.GRASS,
        28: Blocks.WATER
    },
    Blocks.OBSIDIAN: {
        #25: Blocks.OBSIDIAN,
        20: Blocks.SNOW,
        50: Blocks.DIRT,
        30: Blocks.WATER
    },
    Blocks.PUMPKIN: {
        #50: Blocks.PUMPKIN,
        10: Blocks.GLOWSTONE,
        90: Blocks.GRASS
    },
    Blocks.SNOW: {
        #70: Blocks.SNOW,
        80: Blocks.ICE,
        20: Blocks.WATER
    },
    Blocks.STONE: {
        #60: Blocks.STONE,
        15: Blocks.COAL,
        5: Blocks.OBSIDIAN,
        10: Blocks.DIAMOND,
        70: Blocks.GRASS
    },
    Blocks.WATER: {
        #60: Blocks.STONE,
        98: Blocks.WATER,
        1: Blocks.GRASS,
        1: Blocks.ICE
    },
    Blocks.GRASS: {
        #60: Blocks.STONE,
        10: Blocks.ICE,
        30: Blocks.STONE,
        20: Blocks.OBSIDIAN,
        2: Blocks.PUMPKIN,
        23: Blocks.WATER,
        
    }
}

def RandomBlock(options):
    rand_list = []
    
    for key, value in options.items():
        rand_list += [value] * key
        
    return random.choice(rand_list)

