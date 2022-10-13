
#for루프
def fac_for(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
n= int(input("팩토리얼 계산(for루프 이용)): n값 정수 입력:"))
print(n,"!= %d" %(fac_for(n)))

print("---------------------------------------")

#while

def fac_whi(n):
    fact =1
    i=1
    while (i<=n):
        fact =fact*i
        i=i+1
    return fact
n = int(input("factorial계산(while): n!의 n값 입력:"))
print("factorial 계산결과 %d!= %d" %(n,fac_whi(n)))
print("---------------------------------------")

#함수 자기자신 호출

def fac_recursive(n):
    if(n==1): return 1
    return n*fac_recursive(n-1)

n= int(input("factorial 계산(함수 재호출):n값 정수를 입력하시오:"))
print("factorial 계산결과 %d!=%d" %(n,fac_recursive(n)))
