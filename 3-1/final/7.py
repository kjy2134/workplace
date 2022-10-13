김민수={'이름':'김민수','숙제':[10,9,10,8,10],'시험':[65,75],'출석':[29]}
이민아={'이름':'이민아','숙제':[10,9,10,10,10],'시험':[75,85],'출석':[29]}
배철수={'이름':'배철수','숙제':[10,9,10,9,10],'시험':[80,88],'출석':[30]}

weight = [25,30,40,5]
student = [김민수, 이민아, 배철수]

def hw_sum(dic):
    sum=0
    for i in dic['숙제']:
        sum += i
    return sum

def score(dic):
    return (hw_sum(dic)/50*weight[0]+(dic['시험'][0]/100)*weight[1]+(dic['시험'][1]/100)*weight[2]\
    +(dic['출석'][0]/30)*weight[3])

def ave(score):
    if score >=90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'F'

print("김민수 총점,성적:", score(김민수),',',ave(score(김민수)))
print("\n이민아 총점,성적:", score(이민아),',',ave(score(이민아)))
print("\n배철수 총점,성적:", score(배철수),',',ave(score(배철수)))
