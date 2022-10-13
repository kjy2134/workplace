from multiprocessing import heap
from random import*
def heapify(list,n,i):#i에 해당하는 부모-자식node별 heapify 즉, 큰값을 부모 node로 올림.
    large_root=i
    left=2*i+1
    right=2*i+2

    if left < n and list[left] > list[large_root]:
        large_root = left
    if right < n and list[right] > list[large_root]:
        large_root = right
    
    if large_root != i:
        list[i],list[large_root]=list[large_root],list[i]
        heapify(list,n,large_root)

def heapsort(list):
    n = len(list)
    for i in range(n,-1,-1):
        heapify(list,n,i) #heapify를통해 큰값이 부모 node로 올라와있음. 이 반복문을 통해 가장 큰값을 위로 빼줌.
        #하지만 자식노드 사이에서 크기순 정렬을 하는것은 아님.
    
    for i in range(n-1,0,-1): #맨 위로 빠진 큰 값을 뒤로 뺸 후, 규모를 -1씩 줄여가며 다시 heapify
        list[0],list[i] = list[i],list[0]
        heapify(list,i,0) #맨위로 간 원소가 나머지 원소중 가장 큰 원소라는 법이 없음. 나머지 이진트리는 정렬되어있으니, 맨윗원소만 heapify되면 됌.
        #그래서 뒤부터 훑는게 아닌 맨 위부터 해버림. 따라서 i자리에 0이 온것.
list = []
n = int(input())
for i in range(1,n):
    list.append(randint(1,n))
    
print(list)
heapsort(list)
print(list)
