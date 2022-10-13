print("(1)=======================")
list1=[10,21,4,45,66,93,1]
even_count, odd_count = 0, 0

for num in list1:
    if num%2 ==0:
        even_count += 1
    else :
        odd_count += 1

print("even numbers in the list:", even_count)
print("odd numbers in the list:", odd_count)

print("(2)======================")
list1=[10,21,4,45,66,93,11]
even_count, odd_count = 0, 0
num = 0

while(num < len(list1)):
    if list1[num] % 2 ==0:
        even_count +=1
    else:
        odd_count += 1
    num += 1

print("짝수:", even_count,"개")
print("홀수:", odd_count, "개")

print("(3)=======================")
list1 = [10,21,4,45,66,93,11]

only_odd = [num for num in list1 if num%2 == 1]
odd_count = len(only_odd)

print("짝수:", len(list1)-odd_count,"개")
print("홀수:", odd_count, "개")
