from turtle import Turtle, Screen
import random

# tim = Turtle('turtle')
screen = Screen()
screen.setup(width=500, height=400)

# # ---------------------------------------------------------------- Drawing project
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def move_cclockwize():
#     tim.left(10)
#
# def move_clockwize():
#     tim.right(10)
#
# def move_clear():
#     tim.reset()
#
#
# screen.listen()
# # Passing the function in another function without the ()
# screen.onkey(key='w', fun=move_forward)
# screen.onkey(key='s', fun=move_backward)
# screen.onkey(key='a', fun=move_cclockwize)
# screen.onkey(key='d', fun=move_clockwize)
# screen.onkey(key='c', fun=move_clear)


# ---------------------------------------------------------------- Race

colors = ['red', 'green', 'blue', 'black', 'orange', 'purple']
is_race_on = False
all_turtles = []

screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Choose color: ')


# user_1 = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Choose color: ')
# user_2 = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Choose color: ')

# tim.penup()
# tim.goto(x=-230, y=-100)


def set_start():
    y = -90
    for color in colors:
        name = Turtle('turtle')
        name.penup()
        name.color(color)
        name.goto(-230, y)
        y += 30
        all_turtles.append(name)


if user_bet:
# if user_1:
    is_race_on = True
    set_start()

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f'You won! The {winner} turtle is the winner!')
            # if winner == user_1:
            #     print(f'{user_1} won! The {winner} turtle is the winner!')
            # elif winner == user_2:
            #     print(f'{user_2} won! The {winner} turtle is the winner!')
            else:
                print(f'You lose! The {winner} turtle is the winner!')

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
