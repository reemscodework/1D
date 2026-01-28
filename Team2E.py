import turtle 

t = turtle.Turtle()
t.color("red")
t.speed(0)
for a in range(4) : 
    for i in range(20) : 
        for j in range(5) : 
            t.fd(30)
            t.circle(20,180)
        t.right(5)
    t.penup() 
    t.fd(50)
    t.pendown()


turtle.done()
