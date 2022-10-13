def merge(list):
    if len(list) >1 :
        mid = len(list) // 2
        left = list [:mid]
        right = list [mid:]

        merge(left)
        merge(right) #완전히 쪼갤때까지 실행

        # 합치기

        i=0 #left index
        j=0 #right index
        k=0 #새로 합쳐지는 list index

        #임시 정렬
        while i < len(left) and j < len(right): #left와 right리스트 둘다에서 각각 작은 값을 찾아 새로 합쳐지는 list에 할당
            if left[i] < right [j]:
                list[k] = left [i]
                i+= 1 
            else:
                list[k] = right[j]
                j+=1
            k+=1 #새로 합치는 list의 다음 index로 만들기 
       
            #반복문이 종료될 때 (left와 right리스트 길이가 둘다 3이라 가정하면) i와 j는 둘다 4로 끝남. <예시 1>

        #left와 right리스트의 길이가 다를때 둘 중 긴쪽의 원소만 남는 경우가 발생(and)조건으로 인한 반복문 조기 종료 방지용
        #하나짜리 리스트를 그대로 내리기도 함.
        while i < len(left): #left리스트가 더 길 경우 남는 원소 확인
            list [ k ] = left[i] #예시 1에서 i가 마지막 인덱스를 가리키게 됨. (i=4)
            i+=1
            k+=1
        while j < len(right):#right리스트가 더 길 경우 남는 원소 확인 
            list[k] = right[j]
            j+=1
            k+=1

            

list = [36,27,43,3,9,82,10]
merge(list)
print(list)