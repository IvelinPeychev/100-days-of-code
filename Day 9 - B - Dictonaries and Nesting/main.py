# ---------------------------------------------------------------- Starting

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}


# Retrieving items from dictionary.
print(programming_dictionary['Bug'])

# Adding new items to dictionary
programming_dictionary['Loop'] = 'The action of doing something over and over again.'
print(programming_dictionary['Loop'])
print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
print(programming_dictionary)

# Edit an item in the dictionary
programming_dictionary['Bug'] = 'A moth in your computer.'

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# ---------------------------------------------------------------- Grading program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
# for key, value in student_scores.items():
for key in student_scores:
    value = student_scores[key]
    if value > 90:
        student_grades[key] = 'Outstanding'
    elif value > 80:
        student_grades[key] = 'Exceeds Expectations'
    elif value > 70:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Fail'

# 🚨 Don't change the code below 👇
print(student_grades)


# -------------------------------------------------------------- Nesting Dictionary

# Nesting
captials = {
        'France': 'Paris',
        'Germany': 'Berlin'
    }

# Nesting list in dict
travel_log = {
    'France': ['Paris', 'Lion', 'Lille'],
    'Germany': ['Berlin', 'Hamburg', 'Stuttgart']
}


# Nesting dict in dict
travel_log2 = {
    'France': {
        'cities_visited': ['Paris', 'Lion', 'Lille'],
        'total_visited': 12},
    'Germany': {
        'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visited': 15
        }
    }

# Nesting list in dict
travel_log3 = [
    {
        'country': 'France',
        'cities_visited': ['Paris', 'Lion', 'Lille'],
        'total_visited': 12
    },
    {
        'country': 'Germany',
        'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visited': 15
        }
]

# ---------------------------------------------------------------- Dictionary in list
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country, times_visited, cities):
    new_dict = {
        'country': country,
        'visits': times_visited,
        'cities': cities
    }
    travel_log.append(new_dict)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


# ---------------------------------------------------------------- Final Project - blind auction program

from art import logo

print(logo)
print('Welcome to the secret auction program.')

other_bidders = True
bidders = {}

while other_bidders:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))

    bidders = {
        name: bid,
    }

    others = input('Are there any other bidders? Type "yes" or "no". ')
    if others == 'no':
        other_bidders = False


# winner_bid = 0
# winner = ''
# for name in bidders:
#     bid = bidders[name]
#     if bid > winner_bid:
#         winner = name
#         winner_bid = bid
#
# print(f'The winner is {winner} with a bid of ${winner_bid}')

# Same as the above but wrapped in a function
def find_highest_bidder(bidding_record):
    winner_bid = 0
    winner = ''
    for winner_name in bidding_record:
        name_bid = bidding_record[winner_name]
        if name_bid > winner_bid:
            winner = winner_name
            winner_bid = name_bid

    print(f'The winner is {winner} with a bid of ${winner_bid}')


find_highest_bidder(bidders)
