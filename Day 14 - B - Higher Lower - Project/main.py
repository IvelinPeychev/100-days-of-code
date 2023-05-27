import art
import game_data
import random


def game():
    right_answers = 0
    while True:

        print(art.logo)
        option_a = random.choice(game_data.data)
        option_b = random.choice(game_data.data)

        print(f'Compare A: {option_a["name"]}, {option_a["description"]}, {option_a["country"]}')
        print(art.vs)
        print(f'Against B: {option_b["name"]}, {option_b["description"]}, {option_b["country"]}')

        correct_answer = max(option_a['follower_count'], option_b['follower_count'])

        user_answer = input('Who has more followers? Type "A" or "B": ').lower()
        if user_answer == 'a':
            user_answer = option_a['follower_count']
        elif user_answer == 'b':
            user_answer = option_b['follower_count']
        else:
            print('Invalid answer, Game Over.')

        if user_answer == correct_answer:
            right_answers += 1
            print(f'You\'re right! Current score: {right_answers}')
        else:
            print(f'Sorry, that\'s wrong. Final score: {right_answers}')
            break


game()
