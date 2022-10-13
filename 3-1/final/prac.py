num1 = 30;
num2 = 18;

def gcd(x,y):
    while 1:
        if(x > y): 
            x = x-y
        elif(x<y):
            y = y-x
        else:
            break
            
    return x
    
print("최대공약수 :" , gcd(num1,num2))