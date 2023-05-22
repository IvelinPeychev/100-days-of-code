print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print('You can ride the rollercoaster!')
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

#Write your code below this line 👇
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

#Write your code below this line 👇

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

print(f'Your final bill is: ${bill}.')

