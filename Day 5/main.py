fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(fruit)

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
even_total = 0
for i in range(101):
    if i % 2 == 0:
        even_total += i
print(even_total)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)