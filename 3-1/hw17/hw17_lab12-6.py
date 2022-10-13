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
    
list = [10,7,3,9,1,5]
print("orginal list= %s" %list)
heapsort(list)
print("sorted list by heapsort method: %s" %list)

