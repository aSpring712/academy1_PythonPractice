class AutoMobile:
    # name = ""     -> public 멤버
    # velocity = 0

    __name = ""     # -> private 멤버
    __velocity = 0  # -> private 멤버

    #def getName(): self를 지우면 에러 -> getName() takes 0 positional arguments but 1 was given -> 클래스의 메소드 호출 시 1개의 인자를 반드시 준다! -> class안의 메소드는 무조건 첫 번째 인자로 self를 받아야 함
    def getName(self): #실행되는 객체의 정보를 가지고있기 때문에 반드시 self 적어주어야 함
        return self.__name #내부에 접근할 때도 반드시 self.

    def getVelocity(self):
        return self.__velocity

    def __init__(self, Temp): #인자에 접근하기 위해 반드시 self가 필요
        self.__name = Temp #self.name은 class 내부에 있는 name를 말하는 것

    def velocityPlus(self): 
        self.__velocity = self.__velocity + 1 

    def velocityDw(self): 
        self.__velocity = self.velo__velocitycity - 1
        if self.__velocity < 0 :
            self.__velocity = 0

aAutoMobile = AutoMobile('나의 자동차') #객체참조변수 = AutoMobile(Temp) -> name에 '나의 자동차'가 들어감
#print('차이름 : ', aAutoMobile.__name) -> class 밖에서 private 멤버에 접근 -> 에러
print('차이름 : ', aAutoMobile.getName()) #객체지향 기법 - getter, setter 이용
#print('차속도 : ', aAutoMobile.__velocity) -> 에러
print('차속도 : ', aAutoMobile.getVelocity())
aAutoMobile.velocityPlus()

# 자바 접근속성 : public, private, protected, default .. -> 파이톤은 3가지만 있음(default 없음)
# 그냥 적으면 : public
# __ : private -> 자바에서는 getter, setter로 접근했었음
# _ : protected
