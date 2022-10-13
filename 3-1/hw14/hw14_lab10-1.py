import turtle

win = turtle.Screen()
t1 = turtle.Turtle()

def moveto(x,y):
    t1.penup()
    t1.goto(x,y)
    t1.pendown()

def drawrec(x,y,wid,hei):
    moveto(x,y)
    t1.goto(x+wid,y)
    t1.goto(x+wid,y-hei)
    t1.goto(x,y-hei)
    t1.goto(x,y)

def drawtri(x,y,size):
    t1.setheading(0)
    moveto(x,y)
    t1.right(60)
    t1.forward(size)
    t1.right(120)
    t1.forward(size)
    t1.right(120)
    t1.forward(size)

width = turtle.window_width()
height = turtle.window_height()
dividewidth = width /2
left = -(width/2)
right = width /2
left1 = left
right1=left + dividewidth
left2=right1
right2=right

shapewidth = dividewidth * 0.8

x1=left + dividewidth * 0.1
y1 = height * 0.1

x2=left2 + dividewidth * 0.5
y2=height * 0.1

drawrec(x1,y1,shapewidth, shapewidth)

t1.setheading(0)
drawtri(x2,y2,shapewidth)
turtle.mainloop()
