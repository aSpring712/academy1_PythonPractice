aDict = {'이름':'홍길동', '나이': 50, 10:"10만원"}

print(aDict)
print(aDict.keys())
print(aDict.values())
del aDict['나이']
print(aDict)
print('이름' in aDict)
print('나이' in aDict)