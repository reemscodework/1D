import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

move(0, -80)
t.color("#4A7DFF")  # blue tone
t.begin_fill()
t.circle(100)
t.end_fill()

move(0, -10)
t.color("white")
t.write("U P", align="center", font=("Arial", 40, "bold"))

move(0, -200)
t.color("black")
t.write("UNI PAL", align="center", font=("Arial", 24, "bold"))

screen.mainloop()
