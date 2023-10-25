import pygame

pygame.init()
screen = pygame.display.set_mode((800,300))
pygame.display.set_caption('그림 이동 테스트')
Human = pygame.image.load('image\HumanF.png')
screen.fill(color='white')
HumanX = 100
HumanY = 100
screen.blit(Human, (HumanX, HumanY))


stateExit = False
while not stateExit:
    for event in pygame.event.get(): # event/interrupt/message 방식
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                HumanY = HumanY - 30
            elif event.key == pygame.K_DOWN:
                HumanY = HumanY + 30
            elif event.key == pygame.K_LEFT:
                HumanX = HumanX - 30
            elif event.key == pygame.K_RIGHT:
                HumanX = HumanX + 30
            screen.fill(color='white')
            screen.blit(Human, (HumanX, HumanY))
        elif event.type == pygame.QUIT:
            stateExit = True
    pygame.display.update()

pygame.quit()
