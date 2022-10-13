input = open("original.txt")
output = open("modified.txt","w")

before = "aaa"
after = "z"
for i in input.readlines():
    output.write(i.replace(before,after))
