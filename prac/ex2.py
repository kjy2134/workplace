def selfnum1():
    list=[] 
    selfnum=[]
    for i in range(1,10001):
        if i<10 :
        
            list[0]=str(i)[0]
            selfnum.append(i+list[0])
        
        elif i<100:
            
            list[0]=str(i)[0]
            list[1]=str(i)[1]
            selfnum.append(i+list[0]+list[1])
        
        elif i<1000:
            
            list[0]=str(i)[0]
            list[1]=str(i)[1]
            list[2]=str(i)[2]
            selfnum.append(i + int(list[0])+int(list[1])+int(list[2]))
        
        else :
            
            list[0]=str(i)[0]
            list[1]=str(i)[1]
            list[2]=str(i)[2]
            list[3]=str(1)[3]
            selfnum.append(i + int(list[0])+int(list[1])+int(list[2]) + int(list[3]))
    return selfnum

for i in range(1,10001):
    if i in selfnum1():
        continue
    print(i)
    
        

