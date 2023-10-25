# 숫자 1개를 입력 받아
# 4의 배수인지 확인하는 코드를 작성하시오
Number = input('숫자를 입력하세요 : ')

Number = int(Number)

print('입력한 숫자는 4의 배수', end ='')
if Number%4 != 0 or Number == 0:
    print('가 아닙니다')
else :
    print('입니다')