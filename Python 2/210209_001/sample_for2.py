#for문을 이용하여 1에서 10까지 합을 구하시오.
sum = 0
for i in range(1, 11, 1) : #초기값은 1, 증감값은 1, 조건값 11로 for문 선언
    sum += i    #i변수 값을 sum 변수에 더함
print("sum : %d" % sum) #1~10까지의 합을 출력 -> sum : 55
print("--------------")

#for문을 이용하여 1에서 10까지 식과 합을 구하시오.
sum = 0 #sum 변수를 0으로 초기화
for j in range(1, 11, 1) :
    if j < 10 : #j가 10보다 작은 조건으로 if문 선언
        print("%d + " % j, end = "")
    elif j == 10 : #j가 10인 조건으로 if문 선언
        print("%d = " % j, end = "")
    sum += j
print("%d" % sum) #1~10까지의 합을 출력  55



print("=========== 위가 수업 내용!! /// %없이 적어도 똑같이 나옴 ===============")
#for문을 이용하여 1에서 10까지 합을 구하시오.
sum = 0
for i in range(1, 11, 1) :
    sum += i    #i변수 값을 sum 변수에 더함
print("sum : " + str(sum))
print("--------------")

#for문을 이용하여 1에서 10까지 식과 합을 구하시오.
sum = 0 #sum 변수를 0으로 초기화
for j in range(1, 11, 1) :
    if j < 10 : #j가 10보다 작은 조건으로 if문 선언
        print(str(j) + " + ", end = "")
    elif j == 10 : #j가 10인 조건으로 if문 선언
        print(str(j) + " = ", end = "")
    sum += j
print(sum) #1~10까지의 합을 출력  55