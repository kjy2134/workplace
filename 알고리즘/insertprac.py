def insertsort(list):
    for i in range(1,len(list)):
        key = list[i]
        j = i-1
        while j >=0 and key < list [j]: #key 앞에 자기보다 큰 원소를 쓸어옴(key앞과 key인덱스에 해당하는 곳 둘다를 큰값으로만듦 )
            list[j+1] = list[j] #쓸어오기
            j -= 1 #역순 탐색 0인덱까지
        list[ j+1] = key # insert(큰값이 발견된 곳 앞에 j인덱스가 떨어지므로 j+1하여 삽입)


list = [1,5,3,7,2,8,7]
insertsort(list)
print(list)