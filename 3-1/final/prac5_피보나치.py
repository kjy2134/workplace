def fib(n):
    result = [0 for index in range(n)]
    result[0]=1
    result[1]=1
    for i in range(2,n):
        result[i] = result[i-1] + result[i-2]
    return result

print(fib(10))