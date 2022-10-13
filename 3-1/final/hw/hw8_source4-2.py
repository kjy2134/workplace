print("(1)------------------------")
list1=[10,20,4,45,99]
mx = max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n = len(list1)
for i in range(2,n):
    if list1[i] > mx:
        secondmax=mx
        mx=list1[i]
    elif list1[i] > secondmax and mx != list1[i]:
        secondmax = list1[i]

    else :
        if secondmax == mx:
            secondmax = list1[i]
print("두번쨰로 큰 성분:",str(secondmax))
print("(2)-------------------------")
list1 = [10,20,4,45,99]
list1.sort()
print("두번쨰로 큰 성분:",list1[-2])

print("(3)-----------------------")
list1 = [10,20,4,45,99]
new_list = set(list1)
new_list.remove(max(new_list))

print("두번쨰로 큰 성분 : ",max(new_list))