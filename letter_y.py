#Created File
import turtle

t = turtle.Turtle()
height = 100
x = 50
y = 50
#creating the letter Y
t.pensize(5)

def draw_y_coordinates(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    #first diagonal line going NW
    x = x-height/2
    y = y+height/2
    t.goto(x, y)

    #second diagonal going W of new X,Y
    x -= 30
    t.goto(x,y)

    #diagonal line SE near center
    x +=height/2 + 15
    y -= height/2 + 15
    t.goto(x,y)

    y -= height - 15
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

def draw_y(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.left(135)
    t.forward(50)

    t.left(45)
    t.forward(30)

    t.left(135)
    t.forward(60)

    t.right(45)
    t.forward(50)

    t.left(90)
    t.forward(20)

    t.left(90)
    t.forward(50)

    t.right(45)
    t.forward(60)

    t.left(135)
    t.forward(30)

    t.left(45)
    t.forward(50)


#draw_y_coordinates(x,y)
draw_y(x,y)


turtle.done()

