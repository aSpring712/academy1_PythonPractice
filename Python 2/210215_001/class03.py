#p.102 class02.py 예제
class AutoMobile:
    name = ""
    velocity = 0
    def __init__(self, str):#객체 생성 시 호출되는 특수 내장 함수, self는 객체 자신을 의미
        self.name = str #str 문자열을 03라인의 name에 대입
    def velocityPlus(self):
        self.velocity = self.velocity + 1
    def velocityDw(self):
        self.velocity = self.velocity - 1
        if self.velocity < 0:
            self.velocity = 0
ac = AutoMobile("소나타") #문자열을 매개변수로 객체를 생성 -> name, velocity가 생성됨, 내부적으로는 __init__() 함수 호출 -> "소나타"는 name 변수의 값으로 대입됨
ac.velocity = 20
ac.velocityPlus() #클래스의 함수를 선언할 때 첫 번째 인자는 self라고 선언하는 것이 원칙이나 사용할 때는 self는 무조건 주어지는 것이 파이썬의 원칙이므로 그냥 () 해줌
print(ac.name + "의 속도는 %d 입니다." % ac.velocity) #소나타의 속도는 21 입니다.