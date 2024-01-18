# Example file showing a circle moving on screen
import pygame as pg
from libs.blocks import Sprites, SpriteSize, Blocks,Rules, RandomBlock
from libs.tile import Tile, AltTile, ApplyRules
from random import randint, choice
import sys

sys.setrecursionlimit(5000)

DIM = 61 #Musi być nieparzyste


# pg setup r
pg.init()
pg.display.set_caption("AlgebraMiodzio - Test")
screen = pg.display.set_mode((1280, 1280))
screen_w, screen_h = screen.get_size()
clock = pg.time.Clock()
running = True
dt = 0

size_w, size_h = SpriteSize

scale = 10#
scaled_width = int(160 / scale)  
scaled_height = int(160 / scale)  








def TryCollapse(x, y, act_num, num, up_right_down_left, grid):


    grid[x][y].type = choice(grid[x][y].possible_block)
    print(str(grid[x][y].possible_block)+ " " + str(grid[x][y].power)+  " " + str(grid[x][y].type) + " dla : " + str(x) + " " + str(y) +" " +str(up_right_down_left))
    

    def Powering(x,y, base):
        if(y <= DIM-1 and y >= 0 and x <= DIM-1 and x >= 0):
            if(grid[x][y].collapsed == False):
                grid[x][y].possible_block.append(base.type)
                base.Set_Power_M
                #print (grid[x][y].possible_block)
                grid[x][y].power = base.power - randint(10,20)/base.power_multipler 

    def Normaling(x,y, base):
            if(y <= DIM-1 and y >= 0 and x <= DIM-1 and x >= 0):
                if(grid[x][y].collapsed == False):
                    grid[x][y].possible_block.append(RandomBlock(Rules[base.type]))
                    #print (grid[x][y].possible_block)
                    grid[x][y].power = 100 

    
    if(grid[x][y].power > 0):
        Powering(x,y+1, grid[x][y])
        Powering(x,y-1, grid[x][y])
        Powering(x+1,y, grid[x][y])
        Powering(x-1,y, grid[x][y])

    else:
       Normaling(x,y+1,grid[x][y])
       Normaling(x,y-1,grid[x][y])
       Normaling(x+1,y,grid[x][y])
       Normaling(x-1,y,grid[x][y])

    grid[x][y].collapsed = True

  
    if(act_num == num):
        act_num = 1
        up_right_down_left += 1

        if(up_right_down_left == 5):
            up_right_down_left = 1
            
        if(up_right_down_left % 2 == 1):
            num += 1

    else:
        act_num += 1

    if(up_right_down_left == 1):
        y += 1
    if(up_right_down_left == 2):
        x += 1
    if(up_right_down_left == 3):
        y -= 1
    if(up_right_down_left == 4):
        x -= 1

   

    if(y <= DIM-1 and y >= 0 and x <= DIM-1 and x >= 0):
        grid = TryCollapse(x, y, act_num, num, up_right_down_left, grid)
        return grid
    

def AltGenGrid():
    grid = [[AltTile() for x in range(0, DIM)] for y in range(0, DIM)]
    x = int(DIM/2) 
    y = int(DIM/2)
    
    grid[x][y].possible_block = [ Blocks.GRASS]
    TryCollapse(x,y, 0, 1, 1, grid)
    return grid


grid = AltGenGrid()#test

def GenerateGrid():    
    grid = [[Tile() for x in range(0, DIM)] for y in range(0, DIM)]

    grid[0][0] = Tile(Blocks.ICE)
    grid[0][0].collapsed = True
    
    for row_index, row in enumerate(grid):
        for tile_index, tile in enumerate(row):
            
            if tile.collapsed and tile_index != 0 and row_index != 0:
                continue
            else:
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
                    
    return grid

#grid = GenerateGrid()

while running:
    dt = clock.tick(60) / 1000.0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    if pg.key.get_pressed()[pg.K_SPACE]:
        #grid = GenerateGrid()
        grid = AltGenGrid()
   

    for row_index, row in enumerate(grid):
        for column_index, item in enumerate(row):
            
            scaled_sprite = pg.transform.scale(Sprites[item.type], (scaled_width, scaled_height))
            screen.blit(scaled_sprite, ((column_index * size_w/scale), (row_index * size_h/scale)))
            #screen.blit(Sprites[item.type], ((column_index * size_w/2), (row_index * size_h/2)))

    pg.display.flip()

pg.quit()