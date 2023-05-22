print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print('You can ride the roller coaster!')
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print('Child tickets are pay $5.')
    elif age <= 18:
        bill = 7
        # Even though both are less it will execute the first block if it is less than 12
        print('Youth tickets are pay $7.')
    elif 45 <= age <= 55:
        print('Everything is going to be ok. Have a free ride on us.')
    else:
        bill = 12
        print('Adult tickets are pay $12.')

    answer = input("Do you want to a photo taken? Y or N. ")
    if answer == 'Y':
        bill += 3

    print(f'Your final bill is ${bill}')
else:
    print('Sorry, you have to grow taller before you can ride.')


# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
result = round(weight/height**2)

if result < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif result <= 25:
    print(f"Your BMI is {result}, you have a normal weight.")
elif result <=30:
    print(f"Your BMI is {result}, you are slightly overweight.")
elif result <=35:
    print(f"Your BMI is {result}, you are obese.")
else:
    print(f"Your BMI is {result}, you are clinically obese.")


# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Leap year.')
else:
    print('Not leap year.')

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bill = 0
if size == 'S':
       bill = 15
elif size == 'M':
    bill = 20
else:
    bill = 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
         bill +=3

if extra_cheese == 'Y':
    bill +=1

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

t = name1.lower().count('t') + name2.lower().count('t')
r = name1.lower().count('r') + name2.lower().count('r')
u = name1.lower().count('u') + name2.lower().count('u')
e = name1.lower().count('e') + name2.lower().count('e')

total1 = t+r+u+e

l = name1.lower().count('l') + name2.lower().count('l')
o = name1.lower().count('o') + name2.lower().count('o')
v = name1.lower().count('v') + name2.lower().count('v')
e = name1.lower().count('e') + name2.lower().count('e')

total2 = l+o+v+e

LoveScore = int(str(total1)+str(total2))

if 10 >= LoveScore or LoveScore >= 90:
    print(f'Your score is {LoveScore}, you go together like coke and mentos.')
elif 40 <= LoveScore <= 50:
    print(f'Your score is {LoveScore}, you are alright together.')
else:
    print(f'Your score is {LoveScore}.')

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input('You are on a crossroad. Choose a direction "left" or "right"?\n').lower()

if direction == 'left':
    direction = input('You found a dock. Will you "swim" or "wait"?\n').lower()
    if direction == 'wait':
        direction = input('A boat arrived and take you to the house with 3 doors - "green", "yellow", "red". Choose a door.\n').lower()
        if direction == 'yellow':
            print('You found the treasure. Congratulations.')
        elif direction == 'green':
            print('A poisonous snake was hidden behind the door and bit you. Game Over.')
        elif direction == 'red':
            print('You wake up a slipping dragon behind the Red door. Game Over.')
    else:
        print('A crocodile attacked you. Game Over.')
else:
    print('You fell into a hole. Game Over.')