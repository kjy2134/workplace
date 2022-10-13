def insert(list):
    for i in range(1,len(list)):
        key = list[i]
        j= i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -=1
        list[j+1]= key

list = [12,11,13,5,6]
print("orginal list = %s" %list)

insert(list)

print("sorted list by insertion method:", list)
