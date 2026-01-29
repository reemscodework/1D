import turtle # Import the turtle module

def make_e(t,radius=100):
	t.circle(radius,extent=-270)
	p=t.pos()
	t.teleport(p[0]-2*radius,p[1])
	t.right(90)
	t.forward(2*radius)

t = turtle.Turtle() 

t.teleport(-200,0)
t.color("blue")
t.pensize(3)
t.right(90)
t.forward(70)
t.circle(100,180) 
t.forward(70)

# F

t.color("purple")
t.right(180)
t.forward(170)
t.right(180)
t.forward(85)
t.right(90)
t.forward(85)
p=t.pos()
t.right(180)
t.forward(85)
t.right(90)
t.forward(100)
t.right(90)
t.forward(85)

t.teleport(p[0]+80,p[1]-35)
make_e(t,radius=50)

p=t.pos()
t.teleport(p[0]+80, p[1] - 50)
make_e(t, radius=50)

input()
