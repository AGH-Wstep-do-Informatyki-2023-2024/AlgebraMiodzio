from libs.tile import Tile
from libs.blocks import Blocks, Rules, RandomBlock, Printable
from random import randint, choice

def TryCollapse(x, y, act_num, num, up_right_down_left, grid, DIM):

    grid[x][y].type = choice(grid[x][y].possible_block)
    # print(f"{grid[x][y].possible_block} {grid[x][y].power} {grid[x][y].type} dla : {x} {y} {up_right_down_left}")
    
    def Powering(x,y, base):
        if(y <= DIM-1 and y >= 0 and x <= DIM-1 and x >= 0):
            if(grid[x][y].collapsed == False):
                grid[x][y].possible_block.append(base.type)
                base.Set_Power_M()
                grid[x][y].power = base.power - randint(10,20)/base.power_multipler 

    def Normaling(x,y, base):
            if(y <= DIM-1 and y >= 0 and x <= DIM-1 and x >= 0):
                if(grid[x][y].collapsed == False):
                    grid[x][y].possible_block.append(RandomBlock(Rules[base.type]))
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
        grid = TryCollapse(x, y, act_num, num, up_right_down_left, grid, DIM)
        return grid
    

def GenGrid(DIM):
    grid = [[Tile() for x in range(0, DIM)] for y in range(0, DIM)]
    x = int(DIM/2) 
    y = int(DIM/2)
    
    grid[x][y].possible_block = [Blocks.GRASS]
    TryCollapse(x,y, 0, 1, 1, grid, DIM)
    return grid

def GetInfo(x, y, grid):
    # trzeba było zamienić x i y bo nie działało
    data = {
        "type": grid[y][x].type,
        "options": [f"{value}% : {Printable[key]}" for key,value in Rules[grid[y][x].type].items()],
    }
    
    return data