import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,300))
screen.fill((255,255,255))
pygame.display.set_caption('지옥으로 키티')

while True:
    for Temp in pygame.event.get():
        if Temp.type == pygame.QUIT: # pygame.QUIT : 256
            pygame.quit()
            sys.exit()
        pygame.display.update()

