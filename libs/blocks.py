from enum import Enum
import random
import pygame as pg

class Blocks(Enum):
    DIRT = 1
    ICE = 2
    COAL = 3
    DIAMOND = 4
    OBSIDIAN = 5
    SNOW = 6
    STONE = 7
    WATER = 8
    GRASS = 10
    
SpriteSize = 25
    
def img(path):
    tmp = pg.image.load(path)
    tmp = pg.transform.scale(tmp, (SpriteSize, SpriteSize))
    return tmp

Sprites = {
    Blocks.DIRT : img("assets/dirt.jpg"),
    Blocks.ICE : img("assets/ice.jpg"),
    Blocks.COAL : img("assets/coal.jpg"),
    Blocks.DIAMOND : img("assets/diamond.jpg"),
    Blocks.OBSIDIAN : img("assets/obsidian.jpg"),
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
    Blocks.OBSIDIAN : "Obsidian",   
    Blocks.SNOW : "Snow",
    Blocks.STONE : "Stone",
    Blocks.WATER: "Water",
    Blocks.GRASS: "Grass",
}

def RandomBlock(options):
    rand_list = []
    
    for key, value in options.items():
        rand_list += [key] * value
        
    return random.choice(rand_list)

