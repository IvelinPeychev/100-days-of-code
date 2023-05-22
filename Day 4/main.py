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

