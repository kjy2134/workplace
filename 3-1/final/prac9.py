list = ['sunday','monday','tuesday','wendesday','thursday','friday','saturday']
result1= []
for day in list:
    x = day[0:3].upper()
    result1.append(x)
print(result1)

result2 = [a[0:3].upper() for a in list]
print(result2)
    