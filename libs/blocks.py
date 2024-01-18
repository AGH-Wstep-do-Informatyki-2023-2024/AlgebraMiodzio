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

Printable = {
    Blocks.DIRT : "Dirt",
    Blocks.ICE : "Ice",
    Blocks.COAL : "Coal",
    Blocks.DIAMOND : "Diamond",
    Blocks.GLOWSTONE : "Glowstone",
    Blocks.OBSIDIAN : "Obsidian",   
    Blocks.PUMPKIN : "Pumpkin",
    Blocks.SNOW : "Snow",
    Blocks.STONE : "Stone",
    Blocks.WATER: "Water",
    Blocks.GRASS: "Grass",
}

Rules = {
    Blocks.DIRT: {
        #70: Blocks.DIRT,
        Blocks.GRASS: 70,
        Blocks.ICE: 5,
        Blocks.STONE: 10,
        Blocks.OBSIDIAN: 5,
        Blocks.PUMPKIN: 2,
        Blocks.WATER: 8,
    },
    Blocks.ICE: {
        Blocks.DIRT: 60,
        Blocks.STONE: 20,
        Blocks.OBSIDIAN: 5,   
        Blocks.WATER: 25,
    },
    Blocks.COAL: {
        #Blocks.COAL: 50,
        Blocks.STONE: 100,
    },
    Blocks.DIAMOND: {
        Blocks.STONE: 100,
    },
    Blocks.GLOWSTONE: {
        #Blocks.GLOWSTONE: 60,
        Blocks.PUMPKIN: 2,
        Blocks.DIRT: 90,
        Blocks.GRASS: 100,
        Blocks.WATER: 28,
    },
    Blocks.OBSIDIAN: {
        #Blocks.OBSIDIAN: 25,
        Blocks.SNOW: 20,
        Blocks.DIRT: 50,
        Blocks.WATER: 30,
    },
    Blocks.PUMPKIN: {
        #Blocks.PUMPKIN: 50,
        Blocks.GLOWSTONE: 10,
        Blocks.GRASS: 90,
    },
    Blocks.SNOW: {
        #Blocks.SNOW: 70,
        Blocks.ICE: 80,
        Blocks.WATER: 20,
    },
    Blocks.STONE: {
        #Blocks.STONE: 60,
        Blocks.COAL: 15,
        Blocks.OBSIDIAN: 5,
        Blocks.DIAMOND: 1,
        Blocks.GRASS: 70,
    },
    Blocks.WATER: {
        #Blocks.STONE: 60,
        Blocks.WATER: 98,
        Blocks.GRASS: 1,
        Blocks.ICE: 1,
    },
    Blocks.GRASS: {
        #Blocks.STONE: 60,
        Blocks.ICE: 10,
        Blocks.STONE: 30,
        Blocks.OBSIDIAN: 20,
        Blocks.PUMPKIN: 2,
        Blocks.WATER: 23,
        
    }
}

def RandomBlock(options):
    rand_list = []
    
    for key, value in options.items():
        rand_list += [key] * value
        
    return random.choice(rand_list)

