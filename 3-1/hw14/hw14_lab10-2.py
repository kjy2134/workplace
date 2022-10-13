import turtle,random

line_t= turtle.Turtle()
line_t.penup()
line_t.setposition(200,50)
line_t.pendown()
line_t.setposition(200,-50)
line_t.hideturtle()

tom = turtle.Turtle()
tom.shape('turtle')
tom.penup()
tom.setposition(-100,20)

sam = turtle.Turtle()
sam.shape('turtle')
sam.penup()
sam.setposition(-100,-20)

tom_sum=0
sam_sum=0

while ((tom_sum < 300)) and (sam_sum <300):
    tom_dis=random.randint(1,10)
    tom.forward(tom_dis)
    tom_sum += tom_dis

    sam_dis = random.randint(1,10)
    sam.forward(sam_dis)
    sam_sum += sam_dis

if tom_sum > sam_sum :
    tom.color('blue')
    sam.color('red')

else:
    tom.color('red')
    sam.color('blue')
turtle.mainloop()