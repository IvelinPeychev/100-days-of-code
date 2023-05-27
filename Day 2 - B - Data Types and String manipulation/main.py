# ---------------------------------------------------------------- Number input

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]))


# ----------------------------------------------------------------  BMI index of fatness

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# print(int(float(weight) / (float(height) * (float(height)))))
print(int(float(weight) / (float(height) ** 2)))


# ---------------------------------------------------------------- Life calculator

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

ages_left = 90 - int(age)
days = round(ages_left * 365)
weeks = round(ages_left * 52)
months = round(ages_left * 12)


print(f'You have {days} days, {weeks} weeks, and {months} months left.')


# ---------------------------------------------------------------- Bill calculator

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12 or 15? '))
people = int(input('How many people to split the bill? '))

per_person = round(((total_bill + ((total_bill*tip) / 100)) / people), 2)
final_amount = '{:.2f}'.format(per_person)

print(f'Each person should pay: ${final_amount}')
