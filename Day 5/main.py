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
