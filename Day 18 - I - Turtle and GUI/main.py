import turtle
from turtle import Turtle
import random

tim = Turtle()
turtle.colormode(255)
tim.shape('turtle')
tim.color('medium slate blue')

for _ in range(4):
    tim.forward(100)
    tim.right(90)

for _ in range(10):
    tim.forward(10)
    tim.up()
    tim.forward(10)
    tim.down()

# ---------------------------------------------------------------- Color drawing
colors = ['red', 'green', 'blue', 'dark magenta', 'orange', 'purple', 'medium blue']


angles = 3
while angles < 11:
    color = random.choice(colors)
    for _ in range(angles):
        degrees = 360 / angles
        tim.color(color)
        tim.forward(100)
        tim.right(degrees)
    angles += 1

# ----- Teacher solution


def draw_shape(num_sides):
    degrees2 = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(degrees2)


for shape_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

# -------------------------------------------------------------------- Random walk

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t = (r, g, b)
    return t


def random_drawing(number):
    width = 5
    for num in range(number):
        # color2 = random.choice(colors)
        tim.width(width)
        tim.color(random_color())
        direction = random.choice(['r', 'l'])
        if direction == 'r':
            tim.rt(90)
        else:
            tim.lt(90)

        tim.fd(50)
        width += 0.09

        tim.speed(10)


random_drawing(100)


# -------------- Teacher solution

directions = [0, 90, 180, 90]
tim.pensize(15)
tim.speed('fastest')
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


# ---------------------------------------------------------------- Spirograph


direction = 360
tim.speed('fastest')
for _ in range(36):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(direction)
    direction -= 10

# -------- Teacher solution

def draw_spirograph(size_of_gap):
    tim.speed('fastest')
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)



screen = turtle.Screen()
screen.exitonclick()
