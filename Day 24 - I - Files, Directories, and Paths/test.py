with open('my_file.txt', 'r') as file:
    contains = file.read()
    print(contains)

with open('my_file.txt', 'a') as file:
    file.write('\nNew text.')

with open('new_file.txt', 'w') as file:
    file.write('\nNew text.')
