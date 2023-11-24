# Example file showing a circle moving on screen
import pygame as pg
from test import grid, GenerateGrid
from libs.blocks import Sprites

print(grid)

# pg setup
pg.init()
pg.display.set_caption("AlgebraMiodzio - Test")
screen = pg.display.set_mode((1280, 800))
screen_w, screen_h = screen.get_size()
clock = pg.time.Clock()
running = True
dt = 0

import random

# show dirt block in the middle

dirt = pg.image.load("assets/dirt.jpg")
dirt_w, dirt_h = dirt.get_size()
ice = pg.image.load("assets/ice.jpg")
ice_w, ice_h = ice.get_size()

matrix = [[random.randint(0,1) for x in range(0, 10)] for y in range(0, 10)]

while running:
    dt = clock.tick(60) / 1000.0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    # # change matrix after spacebar
    # if pg.key.get_pressed()[pg.K_SPACE]:
    #     matrix = [[random.randint(0,1) for x in range(0, 10)] for y in range(0, 10)]

    # if pg.key.get_pressed()[pg.K_SPACE]:
    #     GenerateGrid()
    
    for row_index, row in enumerate(grid):
        for column_index, item in enumerate(row):
            screen.blit(pg.image.load(Sprites[item.type]), ((column_index * dirt_w), (row_index * dirt_w)))
            

    # for index, row in enumerate(matrix):
    #     amount = 0
    #     for column in row:
    #         if column:
    #             screen.blit(dirt, ((amount * dirt_w),(index * dirt_h)))
    #         else:
    #             screen.blit(ice, ((amount * ice_w), (index * ice_h)))
    #         amount += 1

    pg.display.flip()

pg.quit()