def selection(list):#작은 수를 하나씩 빼서 앞에서부터 채워가는 연산
    for i in range(len(list)-1): #비교 기준값. 마지막은 하나 남게 되는데, 자연스레 가장 큰 수가 뒤에 남아있으므로 -1을 한 것
        min_index = i #가장 작은 값의 위치

        for j in range(i+1,len(list)): #기준값 뒤의 리스트 내 원소들을 훑으며 가장 작은 값 색출
            if list[min_index] > list[j]:
                min_index = j # 작은 값의 인덱스를 min에 할당해서,
        
        list[i], list[min_index] = list[min_index],list[i] #기준값의 인덱스와 찾은 작은값의 인덱스값을 서로 바꿔줌. 그리하여 작은 값을 앞으로 몰아내게 됨.


list = [64,25,12,22,11]
selection(list)
print(list)