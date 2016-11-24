import pygame
from pygame.locals import *
import sys
from board import Board
from socketclient import ServerClient
import SocketServer


pygame.init()
screen = pygame.display.set_mode((601, 601))

brickList = [(0,0),(0,1),(0,9),(19,19)]
stoneList = [(10,5),(7,5)]
waterList = [(0,5),(7,1),(3,9),(18,19)]
#create a new board instane
board = Board()

#see how our set_terrain method is useful
board.set_terrain(brickList,-1)
board.set_terrain(stoneList,-2)
board.set_terrain(waterList,-3)
board.draw_board()

board.cells.draw(screen)

x,y = 5,5
newcor = []

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type in (QUIT, KEYDOWN):
            if event.key == pygame.K_UP:
                newcor = board.move_tank(1,x,y)
                x,y = newcor[0],newcor[1]
                print x,y,"a"
    pygame.display.update()
    
