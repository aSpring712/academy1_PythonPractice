aRange = range(2, 20, 5) #range라는 객체 타입 존재 -> 2부터 20까지 5씩 증가
print(aRange[0])
print(aRange[3])
#aRange[3] = 10 # 'range' object does not support item assignment
#range도 수정 불가
aTuple = tuple(aRange) #range aRange를 튜플로 바꾸어서 aTuple에 저장
print(aTuple)

#aTuple = tuple(range(10))
#print(aTuple)
#print(10 not in aTuple)
#print(10 not in range(10))


#aTuple = '지옥으로 키티'
#aTuple = aTuple * 3
#print(aTuple)

#aTuple = tuple(range(0, 100, 13))
#print(aTuple)
#aList = list(range(0, 100, 13))
#print(aList)

#aTuple = tuple(range(1, 10))
#print(aTuple)