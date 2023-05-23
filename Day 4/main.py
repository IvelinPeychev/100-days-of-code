import random

random_integer = random.randint(1, 5)
print(random_integer)

random_float = random.random()
print(random_float)

random_number = random_integer + random_float
print(random_number)

# Import the random module here
#
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# number = random.randint(0, len(names)-1)
# name = names[number]

name = random.choice(names)

print(f'{name} is going to buy the meal today!')



# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

column = int(position[0]) - 1
row = int(position[1]) - 1
map[row][column] = 'X'

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

map_choice = [rock, paper, scissors]
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. '))
if user_choice > 2:
    print('Invalid number, you lose')
else:
    user_hand = map_choice[user_choice]
    computer_choice = random.randint(0, 2)
    computer_hand = map_choice[computer_choice]

    print(f'{user_hand}\n Computer chose:\n {computer_hand}')

    if user_hand == map_choice[0]:
        if computer_hand == map_choice[2]:
            print('You win')
        elif computer_hand == map_choice[0]:
            print('Draw')
        else:
            print('You lose.')
    elif user_hand == map_choice[1]:
        if computer_hand == map_choice[0]:
            print('You win')
        elif computer_hand == map_choice[1]:
            print('Draw')
        else:
            print('You lose.')
    elif user_hand == map_choice[2]:
        if computer_hand == map_choice[1]:
            print('You win.')
        elif computer_hand == map_choice[2]:
            print('Draw')
        else:
            print('You lose.')
