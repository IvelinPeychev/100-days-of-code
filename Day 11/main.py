# ---------------------------------------------------------------- Black Jack project

############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    import art
    import random

    def calculate_score(all_cards):
        total_score = 0
        for card in all_cards:
            total_score += card
        return total_score

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        print(art.logo)
        player_cards = [random.choice(cards) for card in range(2)]
        dealer_cards = [random.choice(cards)]
        print(f'Your cards: {player_cards}')
        print(f'Computer\'s first card: {dealer_cards}')
        if calculate_score(player_cards) == 21:
            print(f'You have {calculate_score(player_cards)} - Blackjack, you win.')
            blackjack()
        while input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            new_card = random.choice(cards)
            player_cards.append(new_card)
            if calculate_score(player_cards) > 21:
                print(f'You got {calculate_score(player_cards)}. You lose.')
                blackjack()
            else:
                print(f'You have {calculate_score(player_cards)}')

        if len(player_cards) > len(dealer_cards):
            new_computer_card = random.choice(cards)
            dealer_cards.append(new_computer_card)

        print(f'Your final hand: {player_cards}')
        print(f'Computer final hand {dealer_cards}')

        if calculate_score(player_cards) > calculate_score(dealer_cards):
            print('You Win.')
        elif calculate_score(player_cards) == calculate_score(dealer_cards):
            print('Draw')
        else:
            print('You lose')

        blackjack()

    else:
        print('It is good thing that you don\'t like to gamble.')


blackjack()

