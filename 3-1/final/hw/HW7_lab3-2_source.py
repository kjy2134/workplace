#성적체크
def grade(score):
    if score >= 90:
        return "A"
    elif score >=80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif score >=60 :
        return "D" 
    else:
        return "F"

print("**********성적 확인**********")
score = int(input("성적을 입력하세요:"))
print("학점:", grade(score))

print("---------------------------------")
#bmi
def bmi_c(h,w):
    bmi=w/(h/100)**2

    if (bmi >= 40):
        return bmi,"는 고도비만"
    elif (bmi >=30):
        return bmi,"는 비만"
    elif (bmi >=25):
        return bmi, "는 경도비만"
    elif(bmi >= 20):
        return bmi, "는 정상"
    else:
        return bmi,"는 저체중"

print("==========bmi 체크==========")

h=int(input("키를 cm로 입력하세요:"))
w=int(input("체중 kg을 입력하세요:"))

bmi, message = bmi_c(h,w)
print("당신의 bmi: %0.2f, %s" %(bmi, message))
