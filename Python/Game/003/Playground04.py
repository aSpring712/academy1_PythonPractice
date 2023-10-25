import pygame

Map = [ "####################",
        "#     B     .      #",
        "#     ##    #      #",
        "#     ##    #      #",
        "#      #    #      #",
        "#    @      #      #",
        "#    #         #   #",
        "#              #   #",
        "#                  #",
        "####################"]

def drawMap():
    global TileX, TileY, Screen, Tile, Wall
    global TileSizeW, TileSizeH, Human, Box
    global ScreenSizeW, ScreenSizeH, Dot
    for yCount in range(0, TileY):
        for xCount in range(0, TileX):
            if Map[yCount][xCount] == '#':
                Screen.blit(Wall, (xCount*TileSizeW, yCount*TileSizeH))
            elif Map[yCount][xCount] == ' ':
                Screen.blit(Tile, (xCount*TileSizeW, yCount*TileSizeH))
            elif Map[yCount][xCount] == '@':
                Screen.blit(Human, (xCount*TileSizeW, yCount*TileSizeH))
            elif Map[yCount][xCount] == 'B':
                Screen.blit(Box, (xCount*TileSizeW, yCount*TileSizeH))
            elif Map[yCount][xCount] == '.':
                Screen.blit(Dot, (xCount*TileSizeW, yCount*TileSizeH))


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
    global TileSizeW, TileSizeH, Human, Box
    global ScreenSizeW, ScreenSizeH, Dot
    pygame.init()
    Tile = pygame.image.load('image\Tile.png')
    Wall = pygame.image.load('image\Wall.png')
    Human = pygame.image.load('image\HumanF.png')
    Box = pygame.image.load('image\Box.png')
    Dot = pygame.image.load('image\Dot.png')
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