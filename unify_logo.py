import turtle
import random

# ---------------- Screen ----------------
screen = turtle.Screen()
screen.setup(1000, 600)
screen.bgcolor("white")
screen.title("UNIFY Logo")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# ---------------- Helpers ----------------
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def sketch_line(x1, y1, x2, y2, color, width=7):
    t.color(color)
    t.width(width)
    move(x1, y1)
    for i in range(25):
        nx = x1 + (x2 - x1) * i / 25 + random.randint(-2, 2)
        ny = y1 + (y2 - y1) * i / 25 + random.randint(-2, 2)
        t.goto(nx, ny)

def filled_rect_rotated(cx, cy, w, h, angle, color):
    t.color(color)
    t.fillcolor(color)
    t.penup()
    t.goto(cx, cy)
    t.setheading(angle)
    t.forward(-w/2)
    t.left(90)
    t.forward(h/2)
    t.right(90)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()
    t.setheading(0)

# =========================================================
# 1) GAVEL — TRUE CENTER
# =========================================================

ANGLE = 35

# Handle (perfectly centred)
filled_rect_rotated(0, 65, 320, 18, ANGLE, "#6B3E1E")

# Gavel head (wide, clear)
filled_rect_rotated(90, 120, 120, 40, ANGLE, "#7A4A28")
filled_rect_rotated(90, 120, 72, 24, ANGLE, "gold")

# Back cap
filled_rect_rotated(140, 135, 34, 36, ANGLE, "#5A2E1A")

# Bottom protrusion
filled_rect_rotated(-90, 30, 80, 28, ANGLE, "#5A2E1A")

# =========================================================
# 2) UNIFY TEXT — CENTERED
# =========================================================

base_y = 40
x = -170   # <-- THIS is the centering fix

# U
sketch_line(x, base_y+60, x, base_y-20, "purple")
sketch_line(x+40, base_y+60, x+40, base_y-20, "purple")
sketch_line(x, base_y-20, x+40, base_y-20, "purple")

# N
x += 70
sketch_line(x, base_y-20, x, base_y+60, "purple")
sketch_line(x, base_y+60, x+40, base_y-20, "purple")
sketch_line(x+40, base_y-20, x+40, base_y+60, "purple")

# I
x += 70
sketch_line(x+20, base_y-20, x+20, base_y+60, "purple")

# F
x += 50
sketch_line(x, base_y-20, x, base_y+60, "#00A2E8")
sketch_line(x, base_y+60, x+40, base_y+60, "#00A2E8")
sketch_line(x, base_y+20, x+30, base_y+20, "#00A2E8")

# Y
x += 70
sketch_line(x, base_y+60, x+20, base_y+30, "#00A2E8")
sketch_line(x+40, base_y+60, x+20, base_y+30, "#00A2E8")
sketch_line(x+20, base_y+30, x+20, base_y-20, "#00A2E8")

# =========================================================
# 3) WOODEN BASE — WAY CLOSER
# =========================================================

t.color("#4A2414")
t.fillcolor("#4A2414")
move(-260, -35)   # <-- pulled UP hard
t.begin_fill()
t.forward(520)
t.right(90)
t.forward(18)
t.right(90)
t.forward(520)
t.right(90)
t.forward(18)
t.end_fill()

# Stars
t.color("gold")
t.width(3)
for sx in [-25, 0, 25]:
    move(sx, -42)
    for _ in range(5):
        t.forward(10)
        t.right(144)

# ---------------- Finish ----------------
turtle.done()
