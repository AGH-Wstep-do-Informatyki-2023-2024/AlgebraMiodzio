import pygame as pg
from libs.blocks import Sprites, SpriteSize
from libs.grid import GenGrid
import sys

sys.setrecursionlimit(5000)

DIM = 61 #Musi być nieparzyste

screen_size = SpriteSize * DIM

pg.init()
pg.display.set_caption("AlgebraMiodzio - Test")
screen = pg.display.set_mode((screen_size, screen_size))
screen_w, screen_h = screen.get_size()
clock = pg.time.Clock()
running = True
dt = 0

grid = GenGrid(DIM)

while running:
    dt = clock.tick(60) / 1000.0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    if pg.key.get_pressed()[pg.K_SPACE]:
        grid = GenGrid(DIM)
   
    for row_index, row in enumerate(grid):
        for column_index, item in enumerate(row):
            screen.blit(Sprites[item.type], ((column_index * SpriteSize), (row_index * SpriteSize)))

    pg.display.flip()

pg.quit()