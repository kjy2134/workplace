def zzongaeggi(list,low,high): #작은값 정렬과 리스트를 쪼개는 연산을 하는 함수
    #pivot값 정하기 
    pivot = list[high]

    #i는 pivot을 기준으로 list를 정렬하는 역할

    i = low - 1 #pivot보다 작은 값이 들어갈 인덱스(처음인덱스부터 pivot보다 작은값이 나올걸 대비하여 -1로 한것)

     #j를 통해서 list를 훑음.
    for j in range(low,high): # list 처음부터 pivot전까지를 훑음. j는 pivot과 크기연산을 하는 자리
        if list[j] < pivot: #pivot보다 작은 경우의 연산
            i = i+1 #처음인덱스부터 pivot보다 작은 값이 나오게 된다면 작은 값을 넣을 인덱스를 0으로 하기 위하여 바로 +1한다.
            #swap
            list[i],list[j] = list [j], list[i] #다시 말해 , 루프가 돌면서 pivot보다 작은 값은 맨앞에 배치하기 위해, 루프 한 턴 돌 때 i는 0부터 시작하는 것.
            # for루프가 한턴 돌면서 pivot보다 작은 값을 앞부터 배치하기 위해 i가 한턴마다 +1 되며 작은값이 들어갈 자리를 마련해 주는 것이다.\
            #그리고 j는 그 작은 값이 발견된 인덱스를 반환해주어 
    #pivot들어갈 위치를 바꿈
    list[i+1], list[high] = list [ high ], list[i+1]
    #for문이 다 끝나면 i의 위치는 정렬이 된 리스트의 마지막 인덱스가 된다. 바로뒤 인덱스부터는 정렬이 되기 전이므로 i+1을 통해 정렬이 안된 인덱스를 가리킨다.

    return i+1 #pivot의 idx


def quick(list, low, high):
    #pivot의 위치에서 해당 함수를 실행해도 되는지 확인하는 부분
    if low < high:
       #pivot기준으로 쪼개기 위해, pivot위치를 가져옴
        pivot_position = zzongaeggi(list,low,high)
        
        #왼쪽 오른쪽 부분을 쪼갬
        quick(list,low, pivot_position-1)
        quick(list,pivot_position+1, high)


list = [30,80 ,10,90,40,50,70]
n = len(list)
quick(list,0,n-1)
print(list)
