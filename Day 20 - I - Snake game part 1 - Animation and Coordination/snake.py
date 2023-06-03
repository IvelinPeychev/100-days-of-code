from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            turtle = Turtle('square')
            turtle.penup()
            turtle.goto(position)
            turtle.color('white')
            self.snakes.append(turtle)

    def move_snake(self):
        for snake in range(len(self.snakes) - 1, 0, - 1):
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
