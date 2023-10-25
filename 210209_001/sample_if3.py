Number = input('속도를 입력하세요 : ')

Number = int(Number)

if 80 < Number:
    print('고속 주행입니다')
elif 60 < Number:
    print('일반 주행입니다')
else :
    print('저속 주행입니다')