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


# ---------------------------------------------------------------- Prime checker

# Write your code below this line 👇
def prime_checker(number):
    # result = 0
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
            # result += 1
            is_prime = False

    # if result == 0:
    if is_prime:
        print('It\'s a prime number.')
    else:
        print('It\'s not a prime number.')


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# ------------------------------------------------------------------ Ceaser Cipher Part 1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    encripted_text = ''
    for symbol in plain_text:
        current_index = alphabet.index(symbol)
        new_index = current_index + shift_amount
        if new_index >= 26:
            new_index -= 26
        symbol = alphabet[new_index]
        encripted_text += symbol
    print(encripted_text)

    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    # e.g.
    # plain_text = "hello"
    # shift = 5
    # cipher_text = "mjqqt"
    # print output: "The encoded text is mjqqt"

    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


encrypt(text,shift)
