# Example file showing a circle moving on screen
import pygame as pg
import time 
from libs.blocks import Sprites, SpriteSize, Blocks
from libs.tile import Tile

DIM = 20

# pg setup rb
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

    # grid[3][3] = Tile(Blocks.ICE)
    # grid[3][3].collapsed = True
    
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

while running:
    dt = clock.tick(60) / 1000.0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    if pg.key.get_pressed()[pg.K_SPACE]:
        grid = GenerateGrid()

    if pg.mouse.get_pressed()[0] == True:
        print(pg.mouse.get_pos())
        x , y = pg.mouse.get_pos()
        print(int(x/80),int(y/80))
        time.sleep(1)
        print("Tu nie powino być zadnego błendu")
        print("Tu nie powino być zadnego błendu")
        print("Tu nie powino być zadnego błendu")
        print("Tu nie powino być zadnego błendu")
        print("Tu nie powino być zadnego błendu")
        
        
    for row_index, row in enumerate(grid):
        for column_index, item in enumerate(row):
            screen.blit(Sprites[item.type], ((column_index * size_w), (row_index * size_h)))

    pg.display.flip()

pg.quit()