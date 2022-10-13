def merge(list):
    if len(list) >1:
        mid = len(list) //2
        l = list [:mid]
        r = list [mid:]

        merge(l)
        merge(r)

        list.clear()
        while len(l) > 0 and len(r) >0:
            if l[0] <= r[0]:
                list.append(l[0])
                l.pop(0)
            else:
                list.append(r[0])
                r.pop(0)
            
        for i in l:
            list.append(i)
        for i in r:
            list. append(i)

def partition(list, low, high):
    i = low -1 
    pivot = list[high]

    for j in range(low, high) :
        if list[j] < pivot:
            i = i+1
            list [ i], list [j]  = list[j], list[i]
    list[i+1], list[high] = list[high],list[i+1]
    return (i+1)

def quick(list, low, high):
    if low < high :
        pi =  partition(list,low, high)
        quick(list, low, pi-1)
        quick(list, pi+1, high)

def heapify(list, n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and list[i] < list [l]:
        largest = l
    
    if r < n and list[largest] < list [r]:
        largest = r
    
    if largest != i:
        list[i], list[largest] = list[largest], list [i]

        heapify(list,n,largest)

def heapsort(list):
    n = len(list)
    for i in range(n//2-1,-1,-1):
        heapify(list,n,i)
    
    for i in range(n-1,0,-1):
        list[i], list[0] = list[0], list[i]
        heapify(list,i,0)


import random,time,sys
sys.setrecursionlimit(10**4)
list1=list(i for i in range(10000))
random.shuffle(list1)
a=time.time()
merge(list1)
b=time.time()
print("=====time table=====")
print("merge method : %.3f" %(b-a))

a=time.time()
heapsort(list1)
b=time.time()
print("heapsort method: %.3f" %(b-a))


a=time.time()
list1.sort()
b=time.time()
print("using sort function: %.3f" %(b-a))

a=time.time()
n=len(list1)
quick(list1,0,n-1)
b=time.time()
print("quick method: %.3f" %(b-a))




