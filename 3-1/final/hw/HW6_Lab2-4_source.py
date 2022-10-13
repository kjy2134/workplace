def average():
    n=0 #인원수
    sum=0
    score=0
    print("입력을 종료하려면 -1을 입력합니다")
    while (score >= 0):
        score = int(input("성적을 입력하시오: "))
        if score >0:
            sum = sum + score
            n = n + 1
    if n>0:
        average = sum /n
    return average
        

print("학생 성적을 입력하세요")
print("성적 평균=",average())

