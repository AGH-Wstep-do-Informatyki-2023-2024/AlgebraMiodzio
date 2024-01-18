import pygame as pg
from libs.blocks import Sprites, SpriteSize
from libs.grid import GenGrid, GetInfo
import sys
from time import sleep

sys.setrecursionlimit(5000)

DIM = 60
DIM = DIM + 1 # :)

screen_size = SpriteSize * DIM

pg.init()
pg.display.set_caption("AlgebraMiodzio")
screen = pg.display.set_mode((screen_size, screen_size))
screen_w, screen_h = screen.get_size()
clock = pg.time.Clock()
running = True
dt = 0

font = pg.font.SysFont("Comic Sans MS", 20)

grid = GenGrid(DIM)

texts = []

while running:
    dt = clock.tick(60) / 1000.0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    if pg.key.get_pressed()[pg.K_SPACE]:
        grid = GenGrid(DIM)
        texts = []
        sleep(0.2)
   
    for row_index, row in enumerate(grid):
        for column_index, item in enumerate(row):
            screen.blit(Sprites[item.type], ((column_index * SpriteSize), (row_index * SpriteSize)))
            
    if pg.mouse.get_pressed()[0] == True:
        texts = []
        x,y = pg.mouse.get_pos()
        x,y = int(x/SpriteSize), int(y/SpriteSize)
        print(x,y)
        sleep(0.2)
        data = GetInfo(x, y, grid)
        for element in data["options"]:
            texts.append(font.render(element, False, [188, 184, 184],[87, 86, 86]))
            
    if pg.mouse.get_pressed()[2] == True:
        texts = []
    
    for index, text_entry in enumerate(texts):
        screen.blit(text_entry, [0,index*26])
        

    pg.display.flip()

pg.quit()

#       _                        
#       \`*-.                    
#        )  _`-.                 
#       .  : `. .                
#       : _   '  \               
#       ; *` _.   `*-._          
#       `-.-'          `-.       
#         ;       `       `.     
#         :.       .        \    
#         . \  .   :   .-'   .   
#         '  `+.;  ;  '      :   
#         :  '  |    ;       ;-. 
#         ; '   : :`-:     _.`* ;
#[bug] .*' /  .*' ; .*`- +'  `*' 
#      `*-*   `*-*  `*-*'