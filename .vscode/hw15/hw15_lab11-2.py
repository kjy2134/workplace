from tkinter import *

def click(key):
    if key == '=':
        result = eval(entry.get())
        s = str(result)
        entry.insert(END, '=' + s)
    
    elif key == '@':
        entry.delete(0,END)
    else:
        entry.insert(END,key)

    
tk = Tk()
entry = Entry(tk, width = 25, bg = 'white')
entry.grid(row=0, column = 0, columnspan=4) #columnspan이 내장된거엿다.

button_list = ['1', '2', '3', '+', '4', '5', '6', '-',\
     '7', '8', '9', '*', '0', '.', '=', '@']

row_index=1
col_index=0
for button_text in button_list:

    Button(tk, text=button_text, width=5,\
         command = lambda t = button_text : click(t)).grid(row = row_index, column=col_index)
    col_index +=1
    if col_index > 3:
        row_index +=1
        col_index =0

tk.mainloop()

