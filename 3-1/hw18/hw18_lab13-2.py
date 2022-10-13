def fibo(num):
    if num <= 1:
        return numo
    return fibo(num-1) + fibo(num-2)

def fibo_dp(num):
    c = [ 0 for index in range(num+1)]
    c[0]=0
    c[1]=1

    for index in range(2, num +1):
        c[index] = c[index -1] + c[index -2]
    return c[num]

num= 10
print("계산 by 순환 알고리즘 = %d" %fibo(num))

fibo_dp(num)
print("계산 by 동적프로그래밍= %d" %fibo_dp(num))