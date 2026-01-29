import turtle

t = turtle.Turtle()
t.speed(5)
t.pensize(5)

t.penup()
t.goto(-50, -50)
t.pendown()


t.setheading(90)
t.forward(75)


t.right(90)
t.forward(10)
t.circle(-15, 180)

t.left(120)
t.forward(50)

t.right(90)
t.forward(10)
t.right(90)
t.forward(50)
t.penup()

t.goto(-50, -50)
t.setheading(180)
t.pendown()
t.forward(10)


t.right(90)
t.forward(85)
t.right(90)
t.forward(20)
t.circle(-25, 165)

t.hideturtle()
turtle.done()
