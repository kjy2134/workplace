dic = { }
fname = "animal_eng.txt"
with open(fname, "w", encoding="utf8") as file:
    file.write("강아지, dog\n")
    file.write("고양이, cat\n")
    file.write("코끼리, elepant\n")
print("**파일 전체를 출력합니다")
with open(fname, "r", encoding="utf8") as file:
    print(file.read())

with open(fname, "r", encoding="utf8") as file:
    for line in file.readlines():
        x = line.split(".")
        dic[x[0]] = x[1].replace("\n","").replace(" ","")

    print("** 동물명 영어 사전을 출력합니다 **")
    print(dic)

while 1:
    query = input("\n동물 이름(한글): ")
    key = query.lower()
    if key in dic :
        eng = dic.get(key)
        print("%s 는 영어로 %s입니다."%(query, eng))
    else:
        print("등록되지 않은 이름")