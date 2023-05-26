# ---------------------------------------------------------------- Scope

enemies = 1


def increase_enemies():
    enemies = 2
    print(f'enemies inside function {enemies}')


increase_enemies()
print(f'enemies outside function {enemies}')


# ---------------------------------------------------------------- local scope


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength) - not callable as the potion is in the function

# ---------------------------------------------------------------- global scope

player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()

# ---------------------------------------------------------------- modifying global scope
# Not usual to change global variables\
enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f'enemies inside function {enemies}')


increase_enemies()
print(f'enemies outside function {enemies}')

# ------------------------------------------------------------- Number guessing game
# --- my solution
import random

print('Welcome to the Number Guessing game!\nI\'m thinking of a number between 1 and 100. ')
attempts = 0
if input('Choose a difficulty. Type "easy" or "hard": ') == 'easy':
    attempts = 15
else:
    attempts = 10

hidden_number = random.randint(1, 100)
print(hidden_number)


def make_a_guess():
    guess = int(input('Make a guess: '))
    return guess


def decrease_remaining(i):
    i -= 1
    print(f'You have {i} attempts remaining to guess the number.')
    return i


is_guessed = False
print(f'You have a {attempts} attempts to remaining to guess the number.')
while not is_guessed:
    guess_number = make_a_guess()
    if guess_number == hidden_number:
        print(f'You got it! The answer was {hidden_number}')
        is_guessed = True
    elif guess_number < hidden_number:
        print('Too low.\nGuess again.')
    else:
        print('Too high.\nGuess again.')

    attempts = decrease_remaining(attempts)

    if attempts == 0:
        print('You\'ve run out of guesses. You lose.')
        break


# ---- Teacher's code
from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
