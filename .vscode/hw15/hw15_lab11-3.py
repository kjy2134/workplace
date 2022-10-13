
from tkinter import *

x_cur, y_cur = None, None
color_cur = "black"

def draw_canvas():
    canvas.delete('all')
    width_cur = entry.get()

    canvas.create_text(100,100,fill = 'green', font = 'Arial 30 italic bold', text = "TexT")
    canvas.create_line(50,150,50,200,capstyle=ROUND, width=width_cur,fill='red')
    canvas.create_rectangle(100,150,150,200,width=width_cur,outline='red')
    canvas.create_polygon(200,150,250,150,250,200,fill='blue')
    Var.set(entry.get())

def reset_canvas():
    canvas.delete('all')

def draw(event):
    global x_cur, y_cur
    if x_cur and y_cur:
        width_cur = entry.get()
        Var.set(entry.get())
        canvas.create_line(x_cur,y_cur, event.x, event.y, capstyle = ROUND, width=width_cur\
        ,fill = color_cur)
    x_cur = event.x
    y_cur = event.y

def reset(event):
    global x_cur, y_cur
    x_cur, y_cur = None, None

def toggle(event):
    global color_cur
    if color_cur == 'white':
        color_cur = 'black'
    else: 
        color_cur = 'white'

tk = Tk()
tk.title('Lab. 10-3')

#텍스트 등록
label = Label(tk, text="선굵기")
label.grid(row=0, column=0)
#버튼 등록
entry = Entry(tk)
entry.grid(row=0, column= 1)
entry.insert(0,'5')

image = PhotoImage(file='apple.png')
img = Label(tk, image= image)
img.grid(row=1, columnspan= 2, sticky= W+E)

bdraw= Button(tk, text='그리기', command=draw_canvas)
bdraw.grid(row=2, columnspan=2, sticky = W+E)
erase= Button(tk, text='지우기', command=reset_canvas)
erase.grid(row=3,columnspan=2,sticky=W+E)

canvas = Canvas(tk, bg='white', bd='2', width=300, height=300)
canvas.grid(row=4, columnspan=2)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>',reset)
canvas.bind('<Button-3>', toggle)

Var = DoubleVar()
slider = Scale(tk,variable=Var, orient=HORIZONTAL)
slider.grid(row=5, columnspan=2, sticky=W+E)

tk.mainloop()



