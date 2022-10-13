#구구단
def multi_table(n):
    for i in range(n,10):
        for j in range(1,10):
            print("%d x %d = %d" %(i,j,i*j))
        print("\n")

n=int(input("구구단(9단까지) 계산 \n몇단을 시작할까요?(2~9사이):"))
multi_table(n)

print("==============================")

#피타고라스
print("피타고라스의 정리에서 삼각형을 이루는 변의 길이 조합찾기")
n=int(input("변의 길이의 최댓값을 입력하세요:"))

def find(n):
    for a in range(1,n+1):
      for b in range(1,n+1):
          for c in range(1,n+1):
              if (a*a+b*b)==(c*c):
                  print(a, b, c)
find(n)

#윤년 식별기
#(연도가 4로 떨어지고, 100으로 나누어 떨어지는 년도는 제외하며, 400으로 나눠 떨어지는 년도를 윤년으로 지정)

def check(n):
    if(n%4==0)and(n%100!=0)or(n%400==0):
        return True
    else: return False

print("윤년 체크")
n=int(input("연도를 입력해주세요:"))
tf=check(n)
if(tf==True): print("%d는 윤년입니다"%n)
else: print("%d는 윤년이 아닙니다."%n)
