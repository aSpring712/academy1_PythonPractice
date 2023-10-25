aTuple = 0, '할룽', '여보세욤', 3.14
#       int   str    str       float
#서로 다른 자료형을 넣어도 된다

print(aTuple)
print(type(aTuple[0]))  # 0 출력 - 정수형
print(type(aTuple[1]))  # '할룽' 출력 - 문자열형
print(type(aTuple[3]))  # 3.14 출력 - float형
print(aTuple[2][3])     # '욤' 출력 - 문자열형
#이차원 배열
print(aTuple[2][-1])    # '욤' 출력 - 문자열형

#aTuple = 0, 1, 2
#print(aTuple)