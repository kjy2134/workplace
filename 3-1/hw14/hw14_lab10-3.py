import turtle

win = turtle.Screen()
t1 = turtle.Turtle()

distance = 15

trap = [89,-200,158,-248]

def getmin(v1,v2):
    if v1 < v2:
        return v1
    return v2

def getmax(v1,v2):
    if v1<v2:
        return v1
    return v2

def moveto(x,y):
    t1.penup()
    t1.goth(x,y)
    t1.pendown()

def isintrap(x,y,trap):
    minx = getmin(trap[0], trap[2])
    maxx = getmax(trap[0], trap[2])
    miny = getmin(trap[1], trap[3])
    maxy = getmax(trap[1], trap[3])
    if x >= minx and x <= maxx and y>=miny and y <=maxy:
        return True
    else:
        return False
    
def showtrap(trap):
    t1.fillcolor("red")
    t1.begin_fill()
    moveto(trap[0],trap[1])
    t1.goto(trap[2],trap[1])
    t1.goto(trap[2],trap[3])
    t1.goto(trap[0],trap[3])
    t1.goto(trap[0],trap[1])
    t1.end_fill()
    moveto(trap[2] +distance, trap[3] + distance)

def keyeast():
    position = t1.pos()
    t1. goto(position[0]+distance, position[1])
    if isintrap(position[0]+distance, position[1],trap):
        showtrap(trap)

def keywest():
    position=t1.pos()
    t1.goto(position[0]-distance, position[1] )
    if isintrap(position[0]-distance,position[1],trap):
        showtrap(trap)

def keysouth():
    position = t1.pos()
    t1.goto(position[0], position[1]-distance)
    if isintrap(position[0], position[1]-distance,trap):
        showtrap(trap)

def keynorth():
    position = t1.pos()
    t1.goto(position[0],position[1]+distance)
    if isintrap(position[0], position[1]+distance,trap):
        showtrap(trap)

def keyend():
    t1.penup()
    t1.home()
    t1.write("End")

win.setup(560,550)
win.bgpic("maze.gif")
t1.shape('turtle')
t1.color("blue")

t1.penup()
t1.goto(-100,-260)
t1.pendown()

win.onkey(keyeast,'Right')
win.onkey(keywest,'Left')
win.onkey(keysouth,'Down')
win.onkey(keynorth,'Up')
win.onkey(keyend,'e')
win.onkey(keyeast, 'E')

win.listen()
turtle.mainloop()