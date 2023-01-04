import turtle
screen = turtle.Screen()
screen.screensize(250,250,'black')
pen = turtle.Pen()
pen.color('green')
pen.hideturtle()
pen.speed(55555)
pen.up()
pen.goto(0,200)
pen.down()
qw = 0
while qw<200:
    pen.right(qw)
    pen.forward(qw*3)
    qw += 1



turtle.done()
