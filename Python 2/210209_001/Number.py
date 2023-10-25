a = 123
a = a + 1 
print(type(a)) #a의 자료형 출력 -> <class 'int'>
print(a) #124
a = a + 3.14 # 윗부분 까지는 정수형, 여기서부터 실수형
print(type(a)) # <class 'float'>
print(a) # 127.14
a = '지옥으로 키티' # 윗부분 까지는 실수형, 여기서부터 문자열
print(type(a)) # <class 'str'> -> 문자열 타입
print(a) #지옥으로 키티

#a에 입력받기
# a = input()     #안녕    333    333 222
# print(type(a))  #str     str     str   
# print(a)        #안녕    333    333 222    
# input()으로 입력받으면 전부 str형으로 들어가짐

#a에 입력받기
a = int(input())#333  -> 입력받은 것(str)을 int형으로     3.14  ㅇㅇ
print(type(a))  #<class 'int'>                           에러  에러
print(a)        #333


