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
    
Printable = {
    Blocks.DIRT : "Dirt",
    Blocks.ICE : "Ice",
    Blocks.COAL : "Coal",
    Blocks.DIAMOND : "Diamond",
    Blocks.GLOWSTONE : "Glowstone",
    Blocks.OBSIDIAN : "Obsidian",   
    Blocks.PUMPKIN : "Pumpkin",
    Blocks.SNOW : "Snow",
    Blocks.STONE : "Stone"
}
    
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
        Blocks.DIRT : 70,
        Blocks.ICE : 5,
        Blocks.COAL : 5,
        Blocks.STONE : 5,
        Blocks.OBSIDIAN : 5,
        Blocks.DIAMOND : 1,
        Blocks.PUMPKIN : 3,
        Blocks.GLOWSTONE : 1,
    },
    Blocks.ICE: {
        Blocks.ICE : 90,
        Blocks.DIRT : 10,
    },
    Blocks.COAL: {
        Blocks.COAL : 50,
        Blocks.STONE : 50,
    },
    Blocks.DIAMOND: {
        Blocks.DIAMOND : 10,
        Blocks.OBSIDIAN : 40,
        Blocks.STONE : 50,
    },
    Blocks.GLOWSTONE: {
        Blocks.GLOWSTONE : 60,
        Blocks.PUMPKIN : 40,
    },
    Blocks.OBSIDIAN: {
        Blocks.OBSIDIAN : 25,
        Blocks.SNOW : 25,
        Blocks.GLOWSTONE : 50,
    },
    Blocks.PUMPKIN: {
        Blocks.PUMPKIN : 50,
        Blocks.GLOWSTONE : 20,
        Blocks.DIRT : 30
    },
    Blocks.SNOW: {
        Blocks.SNOW : 70,
        Blocks.ICE : 30,
    },
    Blocks.STONE: {
        Blocks.STONE : 60,
        Blocks.COAL : 25,
        Blocks.OBSIDIAN : 10,
        Blocks.DIAMOND : 5
    }
}

def RandomBlock(options):
    rand_list = []
    
    for key, value in options.items():
        rand_list += [key] * value
        
    return random.choice(rand_list)