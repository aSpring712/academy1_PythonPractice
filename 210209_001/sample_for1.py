for Number in range(0, 5):
    print(Number)

for Number in range(0, 50, 10):
    print(Number)

for Number in range(0, -5, -1):
    print(Number)

sum = 0
for i in range(1, 11, 1) :     #초기값은 1, 증감값은1, 조건값 11로 for문 선언
    sum+=i                      #i변수 값을 sum변수에 더함
print("sum : %d" % sum)