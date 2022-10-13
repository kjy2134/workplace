


class friend:
    def __init__(s, name, phone):
        s.name = name
        s.phone = phone
    
    def getname(s):
        return s.name
    
    def getphone(s):
        return s.phone
    
    def setphone(s,phone):
        s.phone = phone
    
    def show(s):
        print("이름:", s.name,"\n전화번호:", s.phone)


print("==============(1)================")
f = friend("윤성우", "010-111-1222") #객체 선언
f. getname()
f.getphone()
f.setphone("010-3333-4444")
f.show()

print("================(2)==============")
fr = []
fr.append(friend("윤지민", "010-5555-6666" ))
fr.append(friend("이선준", "010-9464-6446"))
fr.append(friend("장지우", "010-6666-7777"))
fr.append(friend("윤지율", "010-7777-9999"))
for i in fr:
    i.show()

print("==============(3)================")
for i in fr:
    if i.getname().startswith("윤"):
        i.show()

print("============(4)=================")
for i in fr:
    if i.getname() == "장지우":
        i.setphone("010-9999-9999")
    
for i in fr:
    if i.getname() == "장지우":
        i.show()



        