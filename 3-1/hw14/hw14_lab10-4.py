import turtle

win =turtle.Screen()
t1=turtle.Turtle()

def move(x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()

def rec(x,y,wid,hei):
    move(x,y)
    t1.setheading(0)
    t1.goto(x+wid,y)
    t1.goto(x+wid,y-hei)
    t1.goto(x,y-hei)
    t1.goto(x,y)

def tri(x,y,size):
    move(x,y)
    t1.setheading(0)
    t1.right(60)
    t1.forward(size)
    t1.right(120)
    t1.forward(size)
    t1.right(120)
    t1.forward(size)

def sta(x,y,size):
    move(x,y)
    t1.setheading(0)
    i=0
    while i <5:
        t1.forward(size)
        t1.right(144)
        i += 1
    
width = turtle.window_width()
height = turtle.window_height()

divide = width / 3
leftside=-(width/2)
x1 = leftside+divide*0.1
y1 = height*0.1

x2 = leftside+divide+divide*0.5
y2 = y1

x3 = leftside+divide*2 + divide*0.1
y3 = y1 

wid1= divide*0.5
hei1= wid1
size_tri= wid1
size_sta= wid1
rec(x1,y1,wid1,hei1)
tri(x2,y2,size_tri)
sta(x3,y3,size_sta)
turtle.mainloop()


    

