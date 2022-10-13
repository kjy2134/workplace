def bubblesort(arr):
    for i in range(0,len(arr)-1): #두개씩을 비교하기 때문에 마지막 인덱스까지 갈 필요 없음. 첫 순서부터 큰수를 마지막 인덱스에 몰아둠으로 전체(0~4)에서 (0~3)만 
        swap = False #인자로오는 리스트가 이미 정렬되었을 때를 대비한 인자
        for j in range(0,len(arr)-(1+i)): #가장 큰 값을 가장 큰 인덱스에 넣기 위함. i가 올라갈수록 몰아놓은 인덱스는 보지않고 나머지 인덱스에서만 탐색
            if arr[j] > arr[j+1]: #[j+1]로 인해 범위는 계속 줄지만 범위 바로 뒤 인덱스의 값까지 비교하여 마지막 자리에 최종적으로 큰 값을 할당.
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if swap == False  :
            break


list = [ 5,1,4,2,3]
bubblesort(list)
print(list)
                     