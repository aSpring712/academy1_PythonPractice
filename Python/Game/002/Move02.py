import pygame

pygame.init()
screen = pygame.display.set_mode((800,300))
pygame.display.set_caption('그림 이동 테스트')
Human = pygame.image.load('image\HumanF.png')
screen.fill(color='white')
screen.blit(Human, (100,100))


stateExit = False
while not stateExit:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print('키 눌림')
        elif event.type == pygame.QUIT:
            stateExit = True
    pygame.display.update()

pygame.quit()
