from libs.blocks import Block, Blocks

DIM = 5

grid = [[Block() for x in range(0, DIM)] for y in range(0, DIM)]

grid[0][0] = Block(Blocks.ICE)

# for row in grid:
#     for block in row:
        

for row in grid:
    print(row)
    