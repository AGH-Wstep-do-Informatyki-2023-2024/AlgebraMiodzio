from libs.blocks import Blocks

# TODO: Review those values, make them add to 100 and create realistic map

Rules = {
    Blocks.DIRT: {
        #70: Blocks.DIRT,
        Blocks.GRASS: 70,
        Blocks.ICE: 5,
        Blocks.STONE: 10,
        Blocks.OBSIDIAN: 5,
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
    Blocks.OBSIDIAN: {
        #Blocks.OBSIDIAN: 25,
        Blocks.SNOW: 20,
        Blocks.DIRT: 50,
        Blocks.WATER: 30,
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
        Blocks.WATER: 23,
    }
}
