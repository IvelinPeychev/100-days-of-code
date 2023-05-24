# ---------------------------------------------------------------- Basic
# Simple function
def greet():
    print('Hello')
    print('How do you do?')
    print('Isn\'t the weather nice today')


greet()


# Function that allows one input
def greet_with_name(name):
    print(f'Hello {name}')
    print(f'How do you do {name}')


greet_with_name('Billie')


# Function that allows more than one input
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is like in {location}')


greet_with('Ivo', 'Sofia')

# Function with keyword arguments
greet_with(location='Sofia', name='Ivo')


# ---------------------------------------------------------------- Area calculator

#Write your code below this line 👇

def paint_calc(height, width, cover):
    import math
    paint_needed = math.ceil((height * width) / cover)
    print(f'You\'ll need {paint_needed} cans of paint.')

# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


