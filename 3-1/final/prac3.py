def sum(a):
    b = list(a)
    sum =0
    for i in b:
        sum += int (i)
    
    return sum

x = input("정수 입력:")
print("각자리수 합:" ,str(sum(x)))
