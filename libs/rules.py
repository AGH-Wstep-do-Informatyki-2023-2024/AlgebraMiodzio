from libs.blocks import Blocks

rules = {
    Blocks.DIRT : {
        Blocks.DIRT : 0.8,
        Blocks.ICE : 0.2
    },
    Blocks.ICE : {
        Blocks.DIRT : 0.2,
        Blocks.ICE : 0.8
    }
}