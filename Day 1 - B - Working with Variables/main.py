# ---------------------------------------------------------------- Simple printing
print('Day 1 - B - Working with Variables - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

print('Hello\nHello\nHello')

print("Day 1 - B - Working with Variables - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

print('Hello ' + input('What is your name? '))


print(len(input('What is your name? ')))

# ---------------------------------------------------------------- Number switching

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# --------------------------------------------------------------- Band name Generator

print('Welcome to the Brand Name Generator.')
city = input("What's name of the city you grew up in?\n ")
pet = input("What's your pet's name?\n ")
print(f"Your band name could be {city} {pet}")