from tkinter import *

def click(key):
    if key == '=':
        result = eval(e.get())
        s=str(result)
        e.insert(END,'='+s)

    elif key == 'C':
        e.delete(0,END)
    else:
        e.insert(END,key)


tk = Tk()
tk.title("간단한 계산기")

e = Entry(tk,width=35,bg='white')
e.grid(row=0, column =0, columnspan =6)

buttonList = [
    '1','2','3','+','C',
    '4','5','6','-','//',
    '7','8','9','*','%',
    '0','.','=','/','**'
]
rowindex=1
colindex=0
for buttonText in buttonList:
    Button(tk,text=buttonText, width=10, \
        command=lambda t =buttonText:click(t)).grid(row=rowindex, column=colindex)
    colindex+=1
    if colindex >4 :
        rowindex +=1
        colindex = 0
tk.mainloop()
    
