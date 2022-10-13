def create_num(num):#num은 정수형
    created_num_list=[]
    for i in range(0,num):
        each_sum=0
        for j in range(0,len(str(i))):
            each_sum += int(str(i)[j])
        created_num = i + each_sum
        if num == created_num:
            created_num_list.append(i)
    return created_num_list
    if len(created_num_list) <1:
        return []
num=int(input())
if len(create_num(num)) < 1:
    print(0)
else:
    print(create_num(num)[0])



