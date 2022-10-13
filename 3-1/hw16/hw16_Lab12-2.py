def bubble(list):
    n = len(list)

    for i in range(n):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            
list =[ 64,35,25,12,22,11,90]
print("orginal list = %s" %list)

bubble(list)

print("sorted list by bubble method:",list)