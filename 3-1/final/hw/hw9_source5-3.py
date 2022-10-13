jumin = input("주민번호를 입력하시오(xxxxxx-xxxxxxx):")

partition= jumin.split('-') #-기준 분할 저장: ["앞자리--","뒷자리--"]
print("생년월일정보 =", partition[0])

month=int(jumin[2:4])
day=int(jumin[4:6])
gender=int(jumin[7:8])

if(gender == 1 or gender == 2):
    year = "19"+ jumin[0:2]
else:
    year = "20"+jumin[0:2]

age = 2022-int(year)+1

print("당신은 %s에 태어났습니다" %year)
print("당신의 생일은 %d월 %d 일 입니다"  %(month,day))
print("당신은 올해 %d살 입니다" %(age))
if(gender==1 or gender ==3):
    print("당신은 남성")

else :
    print("당신은 여성")


print("==============(2)==============")

a, b = input("먹고싶은 과일 2개를 중간에 공란을 주고 입력하세요: ").split()
print("과일 1:", a)
print("과일 2:", b)

