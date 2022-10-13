def heapify(list,n,i):  #heap의 모양으로 정렬
    print("list:",list,"n:",n,"i:",i)
    print("heapify")

    root_largest = i
    left = 2*i+1
    right = 2*i + 2

    #왼쪽 노드가 존재하고 왼쪽 노드가 루트보다 더 클때

    if left < n and list[i] < list [left]:
        print("왼쪽 노드가 더 큼")
        print("list[i], list[left]: ",list[i],list[left])

        root_largest = left #큰값을 가진 쪽의 index를 root_largest에 할당
    
    #오른쪽 노드가 존재하고 오른쪽노드가 루트보다 더 클때
    if right < n and list[root_largest] < list[right]:
        print("오른쪽 노드가 더 큼")
        print("list[i], list[right]: ",list[i],list[right])

        root_largest = right
    
    #왼쪽오른쪽(자식노드)에서 바꿔야할 위치를 찾았을 떄
    if root_largest != i: #root_largest(큰값이 할당)가 root와 값이 다를 때
        #찾아낸 값이랑 스왑
        print("swap")
        list[i],list[root_largest] = list[root_largest], list [i]
        print("list:",list,"n:",n,"root_largest:",root_largest) #swap후 list현 상태

        #heap의 형태를 갖출 때 까지 실행
        heapify(list,n,root_largest) #큰값이 가장큰 root에 올라오는 과정 계속
        #여기서 발견된 큰값은 가장 높은 root에 올라가고, 내려간 값의 node에서부터 다시 heapify시작하는 것.

def heapsort(list):
    n = len(list)

    #heap의 형태로 데이터 정렬
    for i in range(n , -1,-1): # n, n-1, n-2, ..., 0
        print("heapsort의 데이터 정렬 for문")
        heapify(list, n,i)

    #루트에 있는 노드랑, 마지막 노드에 있는 애를 바꿔서 정렬, 바뀐 노드를 기준으로 다시 heapify실행
    for i in range(n-1,0,-1): #q바뀐 노드를 기준으로 heapify실행(n-1은 heap트리의 마지막 인덱스)
        print("heapsort의 노드 스왑")
        list[i],list[0] = list[ 0 ],list[i]
        heapify(list,i,0)


list = [4,10,3,5,1]
heapsort(list)
print(list)