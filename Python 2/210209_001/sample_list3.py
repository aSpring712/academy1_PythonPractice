#가변 배열 -> 배열이 늘어남
array = [] #[] 배열형 array는 객체를 가지지 않음, 비어있는 list를 만들고 append로 추가
array.append(101) #append -> 배열에 101이 추가됨
array.append(202) #append -> 배열에 202이 추가됨
array.append(303) 
array.append(404) 

for i in array : #i에 101이 담김 -> 202 -> 303 -> 404
    print(i)     # 101             202    303    404

print("=============remove 후===============")

array.remove(202) #배열에서 제거할 값 : 202 제거 -> array[0] 이런식으로는 접근이 안되는건가?
for i in array :
    print(i) #101 303 404