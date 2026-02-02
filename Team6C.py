import turtle as t

# bg colour
t.bgcolor("WHITE")


# screen 
screen = t.Screen()
screen.setworldcoordinates(0,0,1000,1000)



t.speed(0)
#thicker lines
t.pensize(10)

def head():
    t.penup()
    t.goto(500,100)
    t.pendown()
    t.circle(220)
    
    # smile
    t.penup()
    t.goto(450,220)
    t.pendown()
    #orientation of the arrow 
    t.setheading(270)
    t.circle(50,180)
    t.setheading(0)


    #left eye
    t.penup()
    t.goto(400,400)
    t.pendown()
    t.circle(15)

    #left eye inner
    t.penup()
    t.goto(405,405)
    t.pendown()
    t.fillcolor("BLACK")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

    #right eye
    t.penup()
    t.goto(600,400)
    t.pendown()
    t.circle(15)

    #right eye inner
    t.penup()
    t.goto(605,405)
    t.pendown()
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    

    t.penup()
    t.goto(500,275)
    t.pendown()
    tilt = 90
    for i in range(0,60,10):
        t.forward(20)
        t.setheading(tilt+i)
    t.setheading(0)
        


head()


def chief_hat():
    # goto middle
    t.penup()
    t.goto(500,500)
    t.pendown()

    #middle circle
    t.pensize(5)
    t.fillcolor("BLACK")
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    

    #left circle
    t.penup()
    t.backward(150)
    t.pendown()
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    #right circle
    t.penup()
    t.forward(300)
    t.pendown()
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.penup()

    # middle circle inner
    t.goto(500,500)
    t.pensize(1)
    t.pendown()
    t.pencolor("WHITE")
    t.fillcolor("WHITE")
    t.begin_fill()
    t.circle(90)
    t.end_fill()
    

    #left circle inner
    t.penup()
    t.backward(150)
    t.pendown()
    t.begin_fill()
    t.circle(90)
    t.end_fill()

    #right circle inner
    t.penup()
    t.forward(300)
    t.pendown()
    t.begin_fill()
    t.circle(90)
    t.end_fill()

    #polygon hat
    bottom_left = (325,450)
    top_left = (375,550)
    bottom_right = (675,450)
    top_right = (625,550)
    corners = [bottom_left,top_left,top_right,bottom_right,bottom_left]
        
    t.fillcolor("BLACK")
    t.pencolor("BLACK")
    t.begin_fill()
    
    for i in corners:
        t.goto(i)
    t.end_fill()
    
    #polygon hat inner
    bottom_left = (350,475)
    top_left = (400,575)
    bottom_right = (650,475)
    top_right = (600,575)
    corners = [bottom_left,top_left,top_right,bottom_right,bottom_left]
        
    t.fillcolor("WHITE")
    t.pencolor("WHITE")
    t.begin_fill()
    t.penup()
    t.goto(bottom_left)
    t.pendown()
    
    for i in corners:
        t.goto(i)
    t.end_fill()
    

chief_hat()


def handle():
    t.fillcolor("BLACK")
    corners = [(700,150),(650,50),(700,30),(750,130)]
    t.penup()
    t.goto(700,150)
    t.pendown()
    t.begin_fill()
    for i in corners:
        t.goto(i)
    t.end_fill()

def shaft():
    corners = [
        (820,420),
        (690,120),
        (710,120),
        (840,400),
        (820,420)
    ]
    t.penup()
    t.goto(corners[0])
    t.pendown()
    for corner in corners:
        t.goto(corner)


def spatula_head():
    corners = [
    (820,400),   
    (840,400),   
    (900,470),   
    (760,470),   

    (760,570),   
    (900,570),   
    (900,470),   
    (760,470),   

    (820, 400)
    ]
    t.penup()
    t.goto(corners[0])
    t.pendown()
    t.begin_fill()
    for corner in corners:
        t.goto(corner)
    t.end_fill()


def spatula_whole():
    handle()
    t.pensize(10)
    t.penup()
    t.pencolor("BLACK")
    t.goto(700,20)


    t.pendown()

    t.circle(50)
    shaft()
    spatula_head()
spatula_whole()
t.done()

