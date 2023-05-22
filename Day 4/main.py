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