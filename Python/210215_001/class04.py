class Car2:
    color = ''
    velocity = 0
    def __init__(self, color, velocity):
        self.color = color
        self.velocity = velocity

class Car:
    name = ""
    velocity = 0
    def __init__(self, name, velocity):
        self.name = name
        self.velocity = velocity

class Sonata(Car, Car2):
    vender = ""
    velocity = 0
    def __init__(self):
        self.vender = "Hundai"
        #super().__init__('소나타', 30)
        Car2.__init__(self, '프르스르한',50)
        Car.__init__(self,'소나타', 30)
        #Car2.__init__(self, '프르스르한',50)


aSonata = Sonata()
print(aSonata.vender)
print(aSonata.velocity)
print(aSonata.name)
print(aSonata.color)
