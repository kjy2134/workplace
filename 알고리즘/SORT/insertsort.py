def insertsort(list):
    for i in range(1 ,len(list)): #두번째 인덱스부터 시작해서 비교를 하여 처음 인덱스에 할당을 하기 때문에 1부터 시작
        key = list[i] #index 1부터 끝까지 key값을 두고 key를 기준으로 비교 연산 시작
        j = i-1 #
        print("key=",key)
        print("list0:",list)
        while j >=0 and key < list[j]: # 정렬하는 연산
            list [ j+1] = list [ j] #key보다 큰수를 뒤로 끌어옴 
            print("list:", list)
            j -= 1 #j가 음수가 될때 까지 반복
        list [j+1] = key #key값을 탐색범위 앞에 넣음. 반복문 탈출할 땐 j=-1이기에 항상 맨 앞에 넣어버림 해당 없을 시 list[j+1]은 list[i]이므로 원래자리에 이씀
        #key값보다 크지 않으면 앞 뒤 인덱스값 동일하게 만들고 앞 인덱스에 key값 삽입
        print("list2:", list)

list =[15,2,14,11,23,6]
insertsort(list)
print(list)