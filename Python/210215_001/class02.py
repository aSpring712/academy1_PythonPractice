class AutoMobile:
    __name = ""     # _ _ 두개를 이름 앞에 붙이면 
    __velocity = 0  # private 선언으로 간주

    def getVelocity(self):
        return self.__velocity

    def getName(self):
        return self.__name

    def __init__(self, Temp):
        self.__name = Temp
        print('__init__ 호출')

    def velocityPlus(self):
        self.__velocity = self.__velocity + 1

    def velocityDw(self):
        self.__velocity = self.__velocity - 1
        if self.__velocity < 0:
            self.__velocity = 0

aAutoMobile = AutoMobile('나의 자동차1')
bAutoMobile = AutoMobile('나의 자동차2')
aAutoMobile.velocityPlus()
#print('차이름 : ', aAutoMobile.__name)
#print('차속도 : ', aAutoMobile.__velocity)
print('차이름 : ', aAutoMobile.getName())
print('차속도 : ', aAutoMobile.getVelocity())
