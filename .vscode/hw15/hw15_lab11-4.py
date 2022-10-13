from tkinter import *
def add():
    result = '출력:' + str(float(entryA.get()) + float(entryB.get()))
    print(result)
    labRst.configure(text = result)
    
def sub():
    result = '출력 :' + str(float(entryA.get())-float(entryB.get()))
    print(result)
    labRst.configure(text=result)

def mul():
    result = '출력 :' + str(float(entryA.get()) * float(entryB.get()))
    print(result)
    labRst.configure(text=result)

def div() :
    result = '출력 :' + str(round(float(entryA.get())/float(entryB.get()),8))
    print(result)
    labRst.configure(text=result) #labRst의 라벨(출력:0.0)을 result에 저장된 값으로 수정

def share():
    result = '출력 :' + str(float(entryA.get())//float(entryB.get()))
    print(result)
    labRst.configure(text=result)

def rest():
    result = '출력 :' + str(float(entryA.get())%float(entryB.get()))
    labRst.configure(text=result)

def pow():
    result = '출력 :' + str(int(float(entryA.get()))**int(float(entryB.get())))
    print(result)
    labRst.configure(text=result)

tk = Tk()
tk.title('Lab.10-4')
tk.geometry('500x50')
#라벨
Label(tk,text='입력:A', width=5).pack(side=LEFT) ## 위젯 크기 축소
#입력
entryA = Entry(tk,width=5)
entryA.insert(0,'0')
entryA.pack(side=LEFT)

Label(tk,text = '입력B', width=5).pack(side=LEFT)

entryB = Entry(tk, width =5)
entryB.insert(0,'0')
entryB.pack(side=LEFT)

badd=Button(tk,text = '+', width = 3, command= add) #함수 add에 연결
badd.pack(side = LEFT)

bsub = Button(tk, text = '-', width=3, command = sub)
bsub.pack(side = LEFT)

bmul = Button(tk, text = '*',width=3,command=mul)
bmul.pack(side = LEFT)

bdiv = Button(tk, text = '/', width = 3, command = div)
bdiv.pack(side = LEFT)

bshare = Button(tk, text = '//',width=3, command=share)
bshare.pack(side=LEFT)

brest = Button(tk, text='%', width=3, command=rest)
brest.pack(side=LEFT)

bpow = Button(tk, text = '**',width=3,command=pow)
bpow.pack(side=LEFT)

labRst = Label(tk, text = '출력 : 0.0', width = 20, anchor= 'w')
labRst.pack(side = LEFT)

tk.mainloop()

