print("=================1=================")

class bank:
    def __init__(self):
        self._balance =0
    def withdraw(self, amount):
        self._balance -=amount
        print("통장에", amount, "가 출금됨")
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
        print("통장에서", amount, "가 입금됨")
        return self._balance
    
a = bank()
a.deposit(100)
a.withdraw(10)

print("================2=================")
class car:
    def __init__(self, speed=0, gear=1, color="white"):
        self.__speed = speed
        self.__gear = gear
        self.__color = color
    
    def setspeed(self, speed):
        self.__speed = speed

    def setgear(self, gear):
        self.__gear = gear
    
    def setcolor(self, color):
        self.__color = color

    def __str__(self): //문자열이라는 하나의 형태로 통일
        return "(%d,%d,%s)"%(self.__speed, self.__gear, self.__color)
    

mycar = car()
mycar.setgear(3)
mycar.setspeed(100)
print(mycar)


