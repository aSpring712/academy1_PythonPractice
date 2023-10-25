import pygame
import sys

pygame.init() #초기화
screen = pygame.display.set_mode((800,300)) #창의 가로, 세로 크기 지정
screen.fill((255,255,255))
pygame.display.set_caption('지옥으로 키티') #창 제목

while True: #무한반복 -> pygame객체가 살아있는 한 창이 유지되어야 함 -> pygame program자체가 계속 유지되어야 함
    for Temp in pygame.event.get(): #pygame에서 event 발생 시 Temp에 넣어줌 -> event를 기다림
        if Temp.type == pygame.QUIT: #창의 닫기(x) 클릭 -> 256 ==pygame.QUIT -> 종료
            pygame.quit() #pygame 종료
            sys.exit() #창 닫기
        pygame.display.update() #그게 아니면 pygame의 화면을 바꾸어라
#창 띄우기 끝

