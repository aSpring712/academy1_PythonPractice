import pygame

pygame.init()
screen = pygame.display.set_mode((800,300))
pygame.display.set_caption('그림 이동 테스트')
Human = pygame.image.load('image\HumanF.png')
screen.fill(color='white')
moveUnit = 10
HumanX = 100
HumanY = 100
screen.blit(Human, (HumanX, HumanY))


stateExit = False
while not stateExit:
    for Temp in pygame.event.get():
        if Temp.type == pygame.QUIT:
            stateExit = True

    keys = pygame.key.get_pressed() # polling 방식

    if (keys[pygame.K_UP]):
        HumanY = HumanY - moveUnit
    elif (keys[pygame.K_DOWN]):
        HumanY = HumanY + moveUnit
    elif (keys[pygame.K_LEFT]):
        HumanX = HumanX - moveUnit
    elif (keys[pygame.K_RIGHT]):
        HumanX = HumanX + moveUnit
    screen.fill(color='white')
    screen.blit(Human, (HumanX, HumanY))

    pygame.display.update()
    pygame.time.delay(30)   #pygame.time.Clock().tick(30)

pygame.quit()
