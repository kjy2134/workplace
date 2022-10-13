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

list = [10,7,3,9,1,5 ]
print("orginal list= %s"%list)

merge(list) 
print("sorted list by mergesort :")
print(list)