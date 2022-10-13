def count_f(path):
    with open(path) as file:
        mou=['a','e','i','o','u']
        number= ['1','2','3','4','5','6','7','8','9','0']
        cn=0
        cm=0
        for line in file.readlines():
            cn+=line.count(mou)
        
            cm+=line.count(number)
    print("영어모음 수 : %d" %cn)
    print("\n숫자 수: %d" %cm )
count_f("animal_eng.txt")
            

