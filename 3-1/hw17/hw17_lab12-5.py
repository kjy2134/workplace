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

list = [ 10,7,3,9,1,5]
print("orginal list = %s" %list)
n = len(list)
quick(list, 0, n)
print("sorted list by quicksort method:")
print(list)

























        































































        