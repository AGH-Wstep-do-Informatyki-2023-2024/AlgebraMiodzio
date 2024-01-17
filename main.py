import pygame as pg
import time 
from libs.blocks import Sprites, SpriteSize, Blocks
from libs.tile import Tile
from libs.blocks import Printable

DIM = 20

# xd

pg.init()
pg.display.set_caption("AlgebraMiodzio - Test")
screen = pg.display.set_mode((1000, 750))
screen_w, screen_h = screen.get_size()
clock = pg.time.Clock()
running = True
dt = 0

size_w, size_h = SpriteSize

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
font = pg.font.SysFont("Comic Sans MS", 24)
text = font.render("", False, [128, 64, 255])

def info(x,y,grid):
    print(x,y)
    tile = grid[y][x]

    data = {
        "name": tile.name,
        "type": str(tile),
        "options": [f"{Printable[x]} : {y}%" for x,y in tile.options.items()],
        "collapsed": tile.collapsed
    }
    
    print(data)

while running:
    dt = clock.tick(60) / 1000.0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    #reset grid
    if pg.key.get_pressed()[pg.K_SPACE]:
        grid = GenerateGrid()

    for row_index, row in enumerate(grid):
        for column_index, item in enumerate(row):
            screen.blit(Sprites[item.type], ((column_index * size_w), (row_index * size_h)))

    #show info about blocks
    if pg.mouse.get_pressed()[0] == True:
        print(pg.mouse.get_pos())
        x , y = pg.mouse.get_pos()
        time.sleep(0.2)
        info(int(x/160),int(y/160),grid)
        text = font.render("to jest"+str(x)+"a to jest"+str(y)+"prawda", False, [128, 64, 255]) 
    screen.blit(text, [0, 0])

    pg.display.flip()

pg.quit()