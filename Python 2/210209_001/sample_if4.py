#점수 1개를 입력 받아 학점을 출력하시오
#90점 이상은 A
#80점 이상은 B
#70점 이상은 C
#60점 이상은 D
#나머지는 F

Score = input('점수를 입력하세요 : ')
Score = int(Score)

print('학점은', end = ' ')
if 90 <= Score :
    print('A 입니다')
elif 80 <= Score : #elif = else if
    print('B 입니다')
elif 70 <= Score :
    print('C 입니다')
elif 60 <= Score :
    print('D 입니다')
else :
    print('F 입니다')
