from libs.blocks import Blocks, RandomBlock
from libs.tile import Tile

DIM = 5

grid = [[Tile() for x in range(0, DIM)] for y in range(0, DIM)]

# grid[randint(0,4)][randint(0,4)] = Tile(Blocks.ICE)
grid[0][0] = Tile(Blocks.ICE)
grid[0][0].collapsed = True

def ApplyRules(tile: Tile, target: Tile):
    if target.collapsed:
        return
    
    target.ApplyType(RandomBlock(tile.options))
    target.collapsed = True

for row_index, row in enumerate(grid):
    for tile_index, tile in enumerate(row):
        
        if tile.collapsed and tile_index != 0 and row_index != 0:
            continue
        else:
            # look at neighbors and collapse based on rules
            if tile_index > 0:
                left = grid[row_index][tile_index - 1]
                ApplyRules(tile, left)    
            if tile_index < DIM - 1:
                right = grid[row_index][tile_index + 1]
                ApplyRules(tile, right)
            if row_index > 0:
                up = grid[row_index - 1][tile_index]
                ApplyRules(tile, up)
            if row_index < DIM - 1:
                down = grid[row_index + 1][tile_index]
                ApplyRules(tile, down)

# for row in grid:
#     print(row)