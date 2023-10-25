def spring(Num1, Num2): #인자 2개
    return Num1 + 1000, Num2 + 2000 #return 값이 2개 -> tuple형으로 반환 -> 다른 언어에서는 없음

Temp = spring(100, 200) #Temp : tuple형태
RetVal1, RestVal2 = spring(111,222) #return 값이 2개 -> tuple형태로 받아와야 함
print(type(Temp)) #tuple
print(Temp)
print(RetVal1)
print(RestVal2)
