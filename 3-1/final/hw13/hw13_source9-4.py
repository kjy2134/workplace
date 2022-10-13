
class car:
    def __init__(self, speed, maker, color, price):
        self.speed = speed
        self.maker = maker
        self.color = color
        self.price = price
    def setmaker(self,maker):
        self.maker=maker

    def setspeed(self, speed):
        self.speed = speed


    def getmaker(self):
        return "브랜드" + self.maker

    def getdesc(self):
        return "차량 (속도:" + str(self.speed) + " 브랜드:" + self.maker \
            +" 색깔:"+ self.color + " 가격:"+ str(self.price)
    
class sportscar(car):
    def __init__(self,speed,turbo):
        super().__init__(speed)
        self.turbo=turbo
    
    def setturbo(self, turbo):
        self.turbo=turbo

class truck(car):
    def __init__(self, speed, maker, color, price, payload):
       super().__init__(speed, maker, color, price)
       self.payload = payload
    
    def setpayload(self,payload):
        self.payload= payload
     
    def getpayload(self):
        return "적재량:" + self.payload +")"

class bus(car):
    def __init__(self, speed, maker, color, price, num_of_seats):
        super().__init__(speed, maker, color, price)
        self.num_of_seats=num_of_seats
    
    def set_num(self, num):
        self.num_of_seats = num
    
    def get_num(self):
        return "탑승인원:" + self.num_of_seats + ")"

print("Truck 기반 클래스 객체 생성")
t = truck(100,"benz","black",10000000,"1톤")
print(t.getdesc(),t.getpayload())

print("bus클래스 기반 객체 생성")
b = bus(130,"bmw","blue",200000000, "40석")
print(b.getdesc(),b.get_num())
