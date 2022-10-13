def string_k(k,str):

    string = []

    text = str.split(" ")

    for x in text:
        if len(x) > k:
            string.append(x)

    return string

str = input("input a string:")
k = int(input("input length k:"))

print(string_k(k,str))