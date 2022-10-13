def check(x):
    if (x<=15):
        return 0
    elif(x<=30):
        return 3000
    else:
        return (3000+1000*int((x-30)/15))

c = int(input("주차 시간 입력:"))
print("요금: {}" .format(check(c)))
