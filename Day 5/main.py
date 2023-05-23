# ---------------------------------------------------------------- first tests
fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(fruit)

# ---------------------------------------------------------------- Max height
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total = 0
count = 0
for student in student_heights:
    total += int(student)
    count += 1

average = round(total / count)
print(average)


# ---------------------------------------------------------------- Max student score
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_number = 0

for number in student_scores:
    if number > max_number:
        max_number = number

print(f'The highest score in the class is: {max_number}')

# ---------------------------------------------------------------- Total even numbers
even_total = 0
for i in range(101):
    if i % 2 == 0:
        even_total += i
print(even_total)

# ---------------------------------------------------------------- Fizz Buzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# -------------------------------------------------------------- Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
number_of_letters = int(input('How many letters would you like in your password?\n'))
number_of_symbols = int(input('How many symbols would you like?\n'))
number_of_digits = int(input('How many numbers would you like?\n'))

total_char = number_of_letters + number_of_symbols + number_of_digits

letters_part = ''
for i in range(number_of_letters):
    letter = random.choice(letters)
    letters_part += letter

number_part = ''
for i in range(number_of_digits):
    number = random.choice(numbers)
    number_part += number

symbols_part = ''
for i in range(number_of_symbols):
    symbol = random.choice(symbols)
    symbols_part += symbol

password_list = [letters_part, number_part, symbols_part]
random.shuffle(password_list)
password = password_list[0] + password_list[1] + password_list[2]
print(password)