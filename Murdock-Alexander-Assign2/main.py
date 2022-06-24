import turtle

t = turtle

# creates octagon
t.penup()
t.goto(0, 0)
t.pendown()
t.begin_fill()
t.color('red')
for i in range(8):
    t.forward(100)
    t.left(45)
t.end_fill()

# Creates 'Stop'
t.color('white')
t.penup()
t.goto(-60, 76)
t.pendown()
t.write("STOP", font=("Times", 64, "bold"))
t.hideturtle()

# Creates phill
phill = t.Turtle()
phill.shape("turtle")
phill.color('blue')
phill.penup()
phill.goto(50, -50)
phill.left(450)

t.done()