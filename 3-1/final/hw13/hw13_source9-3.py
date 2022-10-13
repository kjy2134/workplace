class bank:
    def __init__(self,name,number,balance):
        self.balance = balance
        self.name = name
        self.number = number
    
    def withdraw(self, amount):
        self.balance -=amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class saving(bank):
    def __init__(self, name, number, balance, interest):
        super().__init__(name,number,balance)
        self.interest = interest
    
    def set_inter(self,interest):
        self.interest = interest
    
    def get_inter(self):
        return self.interest
    
    def add_inter(self):
        self.balance += self.balance*self.interest

class checking(bank):
    def __init__(self,name,number,balance):
        super().__init__(name,number,balance)
        self.withdraw_charge = 10000
    def withdraw(self, amount):
        return bank.withdraw(self, amount + self.withdraw_charge)
    
print("(1)----은행계좌 클래스 및 클래스 상속-----")

a1 = saving("홍길동",123456,10000,0.05)
a1.add_inter()
print("저축예금 잔액=", a1.balance)

a2=checking("김철수",123457,20000000)
a2.withdraw(100000)
print("당좌예금의 잔액=", a2.balance)
