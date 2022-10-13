s = input("문자열을 입력하시오")

result = {'alpha':0,'upper':0, 'lower':0, 'digit':0, 'space':0}
sentence = list(s)
result['alpha'] = len(sentence)
result['space'] = sentence.count(' ')

print(result)