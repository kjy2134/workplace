print("=============(1)==============")

def check(s):
    low = 0
    high = len(s) -1

    while True :
        if low > high :
            return True;

        
        a= s[low]
        b = s[high]

        if a!=b:
            return False
        low +=1
        high -=1

s= input("input a string:")
print("회문입니까?")
s=s.replace(" ","") #제거함

if(check(s)==True):
    print("YES")
else:
    print("No")

#############################For문 활용##############3#######

print("============(2)===========")

def check_f(s):
    for i in range(0, len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
        return True
s = input("input a string:")
print( "회문입니까?")

s= s.replace(" ", "")
if(check_f(s) == True):
    print("yes")
else :
    print("no.")


#########################역문자열 활용######################
def reverse(S):
    return s[::-1]

def check_r(s):
    rev = reverse(s)

    if (s == rev):
        return True 
    return False

s = input("input a string:")
print("회문입니까?:")
s = s.replace(" ", "")

if (check_r(s)==True):
    print("yes.")
else:
    print("no")
