import pygame
########01234567890123456789####
Map0 = "####################" #0
Map1 = "#                  #" #1
Map2 = "#     ##    #      #" #2
Map3 = "#     ##    #      #" #3
Map4 = "#      #    #      #" #4
Map5 = "#           #      #" #5
Map6 = "#    #         #   #" #6
Map7 = "#              #   #" #7
Map8 = "#                  #" #8
Map9 = "####################" #9

def drawMap():
    global TileX, TileY, Screen, Tile, Wall
    global TileSizeW, TileSizeH
    global ScreenSizeW, ScreenSizeH
    for xCount in range(0, TileX):
        if Map6[xCount] == '#':
            Screen.blit(Wall, (xCount*TileSizeW, 0))
        elif Map6[xCount] == ' ':
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