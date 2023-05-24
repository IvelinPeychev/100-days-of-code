# # ---------------------------------------------------------------- Basic
# # Simple function
# def greet():
#     print('Hello')
#     print('How do you do?')
#     print('Isn\'t the weather nice today')
#
#
# greet()
#
#
# # Function that allows one input
# def greet_with_name(name):
#     print(f'Hello {name}')
#     print(f'How do you do {name}')
#
#
# greet_with_name('Billie')
#
#
# # Function that allows more than one input
# def greet_with(name, location):
#     print(f'Hello {name}')
#     print(f'What is like in {location}')
#
#
# greet_with('Ivo', 'Sofia')
#
# # Function with keyword arguments
# greet_with(location='Sofia', name='Ivo')
#
#
# # ---------------------------------------------------------------- Area calculator
#
# # Write your code below this line 👇
#
# def paint_calc(height, width, cover):
#     import math
#     paint_needed = math.ceil((height * width) / cover)
#     print(f'You\'ll need {paint_needed} cans of paint.')
#
#
# # Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
#
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
#
#
# # ---------------------------------------------------------------- Prime checker
#
# # Write your code below this line 👇
# def prime_checker(number):
#     # result = 0
#     is_prime = True
#     for i in range(2, number - 1):
#         if number % i == 0:
#             # result += 1
#             is_prime = False
#
#     # if result == 0:
#     if is_prime:
#         print('It\'s a prime number.')
#     else:
#         print('It\'s not a prime number.')
#
#
# # Write your code above this line 👆
# # Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)
#
# # ------------------------------------------------------------------ Ceaser Cipher Part 1 - Encryption
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
#
# # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount):
#     encripted_text = ''
#     for symbol in plain_text:
#         current_index = alphabet.index(symbol)
#         new_index = current_index + shift_amount
#         if new_index >= 26:
#             new_index -= 26
#         encripted_text += alphabet[new_index]
#     print(encripted_text)
#
#     # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     # e.g.
#     # plain_text = "hello"
#     # shift = 5
#     # cipher_text = "mjqqt"
#     # print output: "The encoded text is mjqqt"
#
#     # HINT: How do you get the index of an item in a list:
#     # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#     # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
#
# # TODO-3: Call the encrypt function and pass in the user inputs.
# #  You should be able to test the code and encrypt a message.
# encrypt(plain_text=text, shift_amount=shift)
#
# # ---------------------------------------------------------------- Ceaser Cipher Part 2 - Decryption
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
#
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")
#
#
# # TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(cipher_text, shift_amount):
#     clean_word = ''
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         clean_word += alphabet[new_position]
#     print(f"The decoded text is {clean_word}")
#
# # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards*
# #  in the alphabet by the shift amount and print the decrypted text.
# # e.g.
# # cipher_text = "mjqqt"
# # shift = 5
# # plain_text = "hello"
# # print output: "The decoded text is hello"
#
#
# # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# #  Then call the correct function based on that 'drection' variable.
# #  You should be able to test the code to encrypt *AND* decrypt a message.
#
# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# else:
#     decrypt(cipher_text=text, shift_amount=shift)
#
# # ---------------------------------------------------------------- Caesar Cipher Part 3 - Refactoring the code
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
#
# # TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
# def caesar(input_text, shift_amount, direction_path):
#     output_text = ''
#     if direction_path == 'decode':
#         shift_amount *= -1
#
#     for letter in input_text:
#         position = alphabet.index(letter)
#         # if direction_path == 'encode':
#         #     new_position = position + shift_amount
#         # else:
#         #     new_position = position - shift_amount
#         # output_text += alphabet[new_position]
#
#         new_position = position + shift_amount
#         output_text += alphabet[new_position]
#
#     print(f"The {direction_path}d text is {output_text}")
#
#
# # TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(input_text=text, shift_amount=shift, direction_path=direction)

# ---------------------------------------------------------------- Caesar Cipher Part 4 - UX and final touches

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
should_continue = True
while should_continue:
    # e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    # If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    # Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    # Try running the program and entering a shift number of 45.
    # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
    # Hint: Think about how you can use the modulus (%).

    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")

    if answer == 'no':
        should_continue = False
        print('Goodbye')
