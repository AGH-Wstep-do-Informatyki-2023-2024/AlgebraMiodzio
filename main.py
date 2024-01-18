import pygame as pg
import time 
from libs.blocks import Sprites, SpriteSize, Printable, SpriteSize
from libs.tile import Tile

DIM = 30

width, height = SpriteSize * DIM, SpriteSize * DIM

pg.init()
pg.display.set_caption("AlgebraMiodzio - Test")
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
running = True
dt = 0

def GenerateGrid():    
    grid = [[Tile() for x in range(0, DIM)] for y in range(0, DIM)]
    
    for row_index, row in enumerate(grid):
        for tile_index, tile in enumerate(row):
            if tile_index > 0:
                left = grid[row_index][tile_index - 1]
                left.ApplyRules(tile)    
            if tile_index < DIM - 1:
                right = grid[row_index][tile_index + 1]
                right.ApplyRules(tile)
            if row_index > 0:
                up = grid[row_index - 1][tile_index]
                up.ApplyRules(tile)
            if row_index < DIM - 1:
                down = grid[row_index + 1][tile_index]
                down.ApplyRules(tile)                
                    
    return grid

grid = GenerateGrid()

#Block info text
font = pg.font.SysFont("Comic Sans MS", 20)
text = font.render("", False, [128, 64, 255])

def info(x,y,grid):
    tile = grid[y][x]

    data = {
        "name": tile.name,
        "type": str(tile),
        "options": [f"{Printable[x]} : {y}%" for x,y in tile.options.items()],
        "collapsed": tile.collapsed
    }
    return str(data["options"])

while running:
    dt = clock.tick(60) / 1000.0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    #reset grid
    if pg.key.get_pressed()[pg.K_SPACE]:
        grid = GenerateGrid()
        time.sleep(1)

    for row_index, row in enumerate(grid):
        for column_index, item in enumerate(row):
            screen.blit(Sprites[item.type], ((column_index * SpriteSize), (row_index * SpriteSize)))

    #show info about blocks
    if pg.mouse.get_pressed()[0] == True:
        x , y = pg.mouse.get_pos()
        time.sleep(0.2)
        msg = info(int(x/SpriteSize),int(y/SpriteSize),grid)
        text = font.render(msg, False, [188, 184, 184],[87, 86, 86]) 
    screen.blit(text, [0, 0])

    pg.display.flip()

pg.quit()