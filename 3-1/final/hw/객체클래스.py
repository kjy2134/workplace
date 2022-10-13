fname = "6-4.txt"

with open(fname, "r",encoding="utf-8") as file:
    b=0
    d=0
    cnt =0
    for line in file.readlines():       
        print(line)
        a = list(line)
        c = line.split(" ")
        d += len(c)
        b += len(a)
        cnt += line.count(" ")  

print("총 %d자" %b)
print("띄어쓰기 %d번" %cnt)
print("단어 %d개" %d)