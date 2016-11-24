import pygame
from pygame.locals import *
import sys
from board import Board
from socketclient import ServerClient
import SocketServer

# initialie the pygame engine
pygame.init()

# first we need a screen to display all the thins, 800x800 is the resolution
screen = pygame.display.set_mode((800, 800))


# This class is a request handler
# It has the handle method that fires when we recieve something from game server
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = self.request.recv(1024)
            print data
        except:
            print "Exception at server"


# Make new instance of the serverclient class
sc = ServerClient(ThreadedTCPRequestHandler)
# start our listening server on port 7000
sc.start_server()
# connect to the game server, remember to replace the IP with 127.0.0.1
# if you are using the same machine
sc.connect_client("192.168.1.5", 6000)
# send the JOIN command
sc.send_message("JOIN#")

# create a new board instane
board = Board()

board.set_terrain([(0, 0), (0, 1), (0, 2), (0, 3),
                   (10, 0), (11, 15), (11, 16), (10, 12),
                   (17, 17), (18, 18), (19, 19), (1, 1), ], -1)

board.draw_board()

board.cells.draw(screen)

# This is called the Game Loop [VERY IMPORTANT]
# This is where all the game updates, input handling happends
while 1:
    # Here's how we handle keyboard input
    # This code simply check if we pressed something and end the program
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

            # THIS LINE IS CRITICAL
            # if you dont include this line, nothing will be printed on screen
pygame.display.update()