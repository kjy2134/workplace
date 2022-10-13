from logging import root
import random
def heapify(list,n,i):
    root_large = i
    left = 2*i+1
    right = 2*i+2

    if left < n and list[root_large] < list[left]:
        root_large = left
    if right < n and list[root_large] < list[right]:
        root_large = right
    
    #root보다 큰 node를 발견
    if root_large != i:
        list[root_large],list[i] = list[i], list[root_large]
        heapify(list,n,root_large) #재귀함수를 활용한 heap을 크기순 정렬 //루트 따라 쭉 내려가며 해당 루트내 정렬만 실행(전체 heapify되려면 반복문 필요)

def heapsort(list):
    n = len(list)
    #마지막node부터 탐색하여 heap형식으로 정렬
    for i in range(n,-1,-1): #n~0까지
        heapify(list,n,i)  #heap트리 아래부터 탐색하여 올라가며 heap정렬
        print(list)
    
    #정렬 후 마지막 노드와 가장큰 첫노드 스왑
    for i in range(n-1,0,-1): #n-1~1까지
        list[i],list[0]=list[0],list[i]
        heapify(list,i,0)#스왑 후, 가장 높은 root에 가장 작은값이 배치되므로, root가 0일때부터 heap정렬 시작하는것.
        print(list)
        #이 함수를 통해 root보다 큰 노드가 root로 다시 재설정되며 heap정렬 계속 진행
list= [13,3,23,14,512,32,12]
heapsort(list)
print(list)