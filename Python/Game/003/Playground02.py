import pygame

def drawBack():
    global TileX, TileY, Screen, Tile
    global TileSizeW, TileSizeH
    global ScreenSizeW, ScreenSizeH

    for yCount in range(0, TileY):
        for xCount in range(0, TileX):
            Screen.blit(Tile, (xCount*TileSizeW, yCount*TileSizeH))

def gameRun():
    stateExit = False
    while not stateExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stateExit = True
        drawBack()
        pygame.display.update()
    pygame.quit()


def gameInit():
    global TileX, TileY, Screen, Tile
    global TileSizeW, TileSizeH
    global ScreenSizeW, ScreenSizeH
    pygame.init()
    Tile = pygame.image.load('image\Tile.png')
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
