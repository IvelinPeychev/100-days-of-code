# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
print(int(float(weight) / (float(height) * (float(height)))))
print(int(float(weight) / (float(height) ** 2)))

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

ages_left = 90 - int(age)
days = round(ages_left * 365)
weeks = round(ages_left * 52)
months = round(ages_left * 12)


print(f'You have {days} days, {weeks} weeks, and {months} months left.')
