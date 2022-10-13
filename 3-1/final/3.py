def reverse(str):
    list=[]
    for i in range(len(str)):
        list.append(str[-1-i])
    x = ''
    for i in list:
        x += i
    return x

print(reverse('abcde'))