#Created File
import turtle

t = turtle.Turtle()
height = 100
x = 50
y = 50
#creating the letter Y
t.pensize(5)

t.penup()
t.goto(x, y)
t.pendown()

#t.left(135)
x = x-height/2
y = y+height/2
t.goto(x, y)

x -= 30
t.goto(x,y)

x +=height/2 + 15
y -= height/2 + 15
t.goto(x,y)

y -= height - 30
t.goto(x,y)

x += 30
t.goto(x,y)

y =+ height/2 - 15
t.goto(x,y)

x += height/2 + 15
y += height/2 + 15
t.goto(x,y)

x -= 30
t.goto(x,y)

x -= height/2
y -= height/2 
t.goto(x,y)

t.penup()
t.goto(0,0)    



turtle.done()

