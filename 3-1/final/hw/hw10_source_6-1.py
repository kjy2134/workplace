print("(1)====================")
fname = input("파일이름:")
print("--파일 전체 출력--")

with open(fname, "r                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ") as file:
    print(file.read())

with open(fname, "r") as file:
    table = dict()
    for line in file.readlines():
        words = line.split()
        for word in words:
            if word not in table:
                table[word] = 1
            else :
                table[word] += 1

    print("==단어 빈도수 출력==")
    print(table)

print("(2)=================")
def parse_file(path):
    with open(path) as infile:
        spaces =0
        tabs =0
        for line in infile.readlines():
            spaces += line.count('')
            tabs += line.count('\t')
            return spaces, tabs

spaces, tabs = parse_file(fname)
print("스페이스 수 = %d, 탭 수= %d" %(spaces, tabs))
