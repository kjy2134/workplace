#lab 1
def selection(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1,len(list)):
            if  list[min_idx] > list[j]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]

#lab2
def bubble(list):
    n = len(list)

    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
#lab3
def insert(list):
    for i in range(1,len(list)):
        key = list[i]
        j= i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -=1
        list[j+1]= key

def sort(list):
    list1 = list.sort()

import time, random

list1 = list(i for i in range(10000))
random.shuffle(list1)

a= time.time()
selection(list1)
b = time.time()
print("selection method:",b-a,"s")

a= time.time()
bubble(list1)
b = time.time()
print("bubble method:",b-a,"s")

a= time.time()
insert(list1)
b = time.time()
print("insert method:",b-a,"s")

a= time.time()
sort(list1)
b = time.time()
print("sort function method:",b-a,"s")