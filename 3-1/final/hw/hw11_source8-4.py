class friend:
    def __init__(self,name,phone,email,adress):
        self.name = name
        self.phone = phone
        self.email = email
        self.adress = adress
    def show(self):
        print("-이름: {} \t-전화번호: {} \t-이메일: {} \t-주소: {}".format(self.name,\
            self.phone,self.email,self.adress))
            
fri = []

print("================연락처 관리=================")

while 1:
    print("================\n1.연락처 입력\n2.연락처 출력\
        \n3.연락처 조회\n4.연락처 수정\n5.연락처 삭제\n\
        6.종료")
    menu = int(input("메뉴 번호를 입력하세요 : "))
    if menu == 1:
        x=input("\n이름:")
        y=input("\n전화번호:")
        z=input("\n이메일:")
        w=input("\n주소:")
        fri.append(friend(x,y,z,w))
        

    elif menu == 2:
        for i in fri:
            i.show()
    
    elif menu == 3:
        p = input("조회할 연락처 이름 입력:")
       
        for friend in fri:
            if p == friend.name:
                friend.show() 
                break #for문 탈출
            else:
                print("검색 결과가 존재하지 않습니다")
    elif menu == 4:
        p = input("수정할 연락처 이름 입력:")
        for friend in fri:
            if friend.name == p:
                friend.show()
                print("< 1.이름 / 2.전화번호 / 3.이메일 / 4.주소 > ")
                a = int(input("수정 항목을 고르세요:"))
                
                if a == 1: 
                    b=input("새 이름:")
                    friend.name = b
                elif a == 2:
                    b = input("새 전화번호 : ")
                    friend.phone = b 
                elif a == 3:
                    b = input("새 이메일 : ")
                    friend.email = b
                elif a == 4:
                    b = input("새 주소 : ")
                    friend.adress = b
                else:
                    print("존재 x. 다시 입력하세요")
                    break
            else: 
                print("목록에 존재하지 않습니다")
    
    elif menu == 5:
        p = input("삭제할 연락처 이름 입력:") 
        for friend in fri:
            if friend.name == 'p':
                friend.remove(friend)
                break
            else:
                print("존재하지 않는 연락처입니다")
                break
    
    elif menu == 6:
        print("프로그램 종료")
        break
    else:
        print("1~6까지의 숫자 중 하나를 입력해주세요")
        


