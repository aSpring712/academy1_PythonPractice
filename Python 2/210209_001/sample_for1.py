for Number in range(0, 5) : #변수 선언을 여기에서 바로 함, range(시작, 끝) -> Number가 5보다 작을 때까지 증가한다 -> 기본으로 1씩 증가
    print(Number) #0 1 2 3 4
#중괄호가 없는 대신 tab으로 들여쓰기 -> for문에 속한 문장

for Number in range(0, 50, 10) : #0~49 즉, 50보다 작을 때까지 도는데 10씩 증가함
    print(Number) #0 10 20 30 40

for Number in range(0, -5, -1) :
    print(Number) #0 -1 -2 -3 -4