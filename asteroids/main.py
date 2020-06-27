'''
Asteroids implementation

https://www.pygame.org/docs/ref/key.html
'''
import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Animation')
BLACK = (0, 0, 0)


shipImg0 = pygame.image.load('ship2small.png')
shipImg = pygame.transform.rotate(shipImg0, 0)
#shipImg.convert()


# initial position of the ship
shipx = 270
shipy = 270
angle = 0



while True:
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            
            # translations x,y
            if event.key == pygame.K_w:
                #print("W")
                shipy = shipy - 5
            if event.key == pygame.K_a:
                #print("A")
                shipx = shipx - 5
            if event.key == pygame.K_s:
                #print("S")
                shipy = shipy + 5
            if event.key == pygame.K_d:
                #print("D")
                shipx = shipx + 5
    
            # rotations
            if event.key == pygame.K_q:
                #print("Q")
                shipImg = pygame.transform.rotozoom(shipImg0, angle+45, 1)
                angle += 45
            if event.key == pygame.K_e:
                #print("E")
                shipImg = pygame.transform.rotozoom(shipImg0, angle-45, 1)
                angle -= 45
    
    
   
    DISPLAYSURF.blit(shipImg, (shipx, shipy))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()