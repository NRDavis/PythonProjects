import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
DISPLAYSURF= pygame.display.set_mode((820, 820), 0, 32)         # sets border to 10 pixels
pygame.display.set_caption("NCSU Monopoly")

board0 = pygame.image.load("Images/originalBoard.png")

while True:
 
    DISPLAYSURF.blit(board0, (10,10))               # draw board
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()










''''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            # translations x,y
            if event.key == pygame.K_w:
                print("W")
'''