import pygame

Map0 = "WWWWWWWWWWWWWWWWWWWW" #0
Map1 = "W                  W" #1
Map2 = "W     WW    W      W" #2
Map3 = "W     WW    W      W" #3
Map4 = "W      W    W      W" #4
Map5 = "W           W      W" #5
Map6 = "W    W         W   W" #6
Map7 = "W              W   W" #7
Map8 = "W                  W" #8
Map9 = "WWWWWWWWWWWWWWWWWWWW" #9

def drawMap():
    global TileX, TileY, Screen, Tile, Wall
    global TileSizeW, TileSizeH
    global ScreenSizeW, ScreenSizeH
    for xCount in range(0, TileX):
        if Map2[xCount] == 'W':
            Screen.blit(Wall, (xCount*TileSizeW, 0))
        else:
            Screen.blit(Tile, (xCount*TileSizeW, 0))

def gameRun():
    stateExit = False
    while not stateExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stateExit = True
        drawMap()
        pygame.display.update()
    pygame.quit()

def gameInit():
    global TileX, TileY, Screen, Tile, Wall
    global TileSizeW, TileSizeH
    global ScreenSizeW, ScreenSizeH
    pygame.init()
    Tile = pygame.image.load('image\Tile.png')
    Wall = pygame.image.load('image\Wall.png')
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