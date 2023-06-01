import colorgram
import turtle
from turtle import Turtle
import random


# # To extract the colors from image.jpg , commented after that
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle.colormode(255)
jonny = turtle.Turtle()
jonny.hideturtle()

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def hirst(x, y, rows, number_per_row):
    for _ in range(rows):
        jonny.penup()
        jonny.setpos(x, y)
        jonny.pendown()
        for _ in range(number_per_row):
            jonny.color(random.choice(color_list))
            jonny.dot(20)
            jonny.penup()
            jonny.forward(50)
            jonny.pendown()

        y += 50


hirst(-300, -300, 10, 10)

screen = turtle.Screen()
screen.exitonclick()
