list = []
for i in range(1,10):
    if(i*i*i <= 500):
        list.append(i)
    else:
        break
cubic = [x*x*x for x in list]
print(cubic)
