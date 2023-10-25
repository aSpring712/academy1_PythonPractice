import pygame

def gameRun():
    stateExit = False
    while not stateExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stateExit = True
        pygame.display.update()
    pygame.quit()


def gameInit():
    global TileX, TileY, Screen
    global TileSizeW, TileSizeH
    global ScreenSizeW, ScreenSizeH
    pygame.init()
    TileX = 20
    TileY = 10
    TileSizeW = 60
    TileSizeH = 60
    ScreenSizeW = TileSizeW * TileX
    ScreenSizeH = TileSizeH * TileY
    Screen = pygame.display.set_mode((ScreenSizeW, ScreenSizeH))
    pygame.display.set_caption('배경 출력 테스트')

gameInit()
gameRun()
