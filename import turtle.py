import turtle

def mid_top(divider):
    t.penup()
    t.home()
    t.left(90)
    t.forward(200//divider)
    t.pendown()

def left_shield(divider):
    top_divider = divider/1.1
    bottom_angle = divider/1.15
    
    if divider == 0:
        divider = 1
        top_divider = 1
        bottom_angle = 1
        
    mid_top(divider)
    t.left(215)
    print(top_divider)
    t.circle(150//top_divider, 90)
    
    t.right(105) 
    t.circle(-350//divider, 90*bottom_angle)
    
    

def right_shield(divider):
    top_divider = divider/1.1
    bottom_angle = divider/1.15
    
    if divider == 0:
        divider = 1
        top_divider = 1
        bottom_angle = 1
        
    mid_top(divider)
    t.right(215)
    print(top_divider)
    t.circle(-150//top_divider, 90)
    
    t.left(105) 
    t.circle(350//divider, 90*bottom_angle)

#to test where middle line is
def test_middle():
    mid_top(1)
    t.right(180)
    t.forward(600)


def sheild():
    #test_middle()
    left_shield(0)
    left_shield(1.2)
    right_shield(0)
    right_shield(1.2)
    mid_top(1)



screan = turtle.Screen()
t = turtle.Turtle()

sheild()
turtle.done()
