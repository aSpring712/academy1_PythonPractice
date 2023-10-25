# 점수 1개를 입력 받아 학점을 출력하시오
# 90점 이상은 A
# 80점 이상은 B
# 70점 이상은 C
# 60점 이상은 D
# 나머지는 F

Number = input('점수를 입력하세요 : ')

Number = int(Number)

if 90 <= Number:
    print('A 입니다')
elif 80 <= Number:
    print('B 입니다')
elif 70 <= Number:
    print('C 입니다')
elif 60 <= Number:
    print('D 입니다')
else:
    print('F 입니다')
    