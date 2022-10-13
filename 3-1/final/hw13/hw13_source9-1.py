class car:
    def __init__(self, speed):
        self.speed = speed

    def setspeed(self, speed):
        self.speed = speed
    def getdesc(self):
        return "차량=(" + str(self.speed) + ")"
    
class sportscar(car):
    def __init__(self,speed,turbo):
        super().__init__(speed)
        self.turbo=turbo
    
    def setturbo(self, turbo):
        self.turbo=turbo

print("(1) car클래스 상속에 의한 sportscar클래스 생성")
o = sportscar(100,True)
print(o.getdesc())
o.setturbo(False)

