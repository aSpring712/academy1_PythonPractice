class Car2: #파이썬은 다중상속 가능(cf.자바는 불가능)
    color = ''
    velocity = 0
    def __init__(self, color, velocity): #Car2 class의 생성자
        self.color = color
        self.velocity = velocity

class Car:
    name = ""
    velocity = 0
    def __init__(self, name, velocity): #Car class의 생성자
        self.name = name
        self.velocity = velocity

class Sonata(Car, Car2): #Sonata 클래스는 Car 클래스와 Car2 클래스를 상속받음(다중상속)
    vender = ""
    velocity = 0
    def __init__(self):
        self.vender = "Hundai"
        #super().__init__('소나타', 30) #부모의 init을 호출 -> 이걸 해주지 않으면 velocity는 0, name은 ""가 나옴
        #자바는 super를 생성자의 가장 처음에 적어줘야 하는데, 파이썬은 순서 상관 없음 & import 위치도 꼭 맨 위에 해줘야되는건 아님
        #super().__init__('소나타', 30) -> 다중상속 시 super를 사용하면 가장 처음 상속받은 Car의 __init__만 호출
        Car.__init__(self, '소나타', 30) #self를 반드시 넣어주어야 함
        Car2.__init__(self, '푸르스름한', 20)
        Car2.__init__(self, '파랑', 80) #또 써주면 이게 출력됨

aSonata = Sonata()
print(aSonata.vender) #자식의 init은 구동됨 -> Hundai
print(aSonata.velocity) #Car, Car2의 velocity 중 마지막에 접근한 velocity가 출력됨
print(aSonata.name) 
print(aSonata.color)