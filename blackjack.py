import random
import art

############### Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

blackjack_definitions = {"blackjack": 21,
                         "ace_hard": 1,
                         "ace_soft": 11,
                         "dealer_stop": 17}


def draw_card():
    return random.choice(cards)


def calculate_score(card1, card2):
    return card1 + card2


def game():
    play_again = 'y'
    while play_again == 'y':
        print(art.logo)
        win = False
        lose = False
        player_cards = [draw_card(), draw_card()]
        dealer_cards = [draw_card(), draw_card()]
        player_card_value = calculate_score(player_cards[0], player_cards[1])
        dealer_card_value = calculate_score(dealer_cards[0], dealer_cards[1])
        print(f"Your cards: {player_cards}, current score: {player_card_value}")
        print(f"The dealers first card is {dealer_cards[0]}")

        if dealer_card_value == blackjack_definitions["blackjack"]:
            print("Dealer got a blackjack! You lost.")
        elif player_card_value == blackjack_definitions["blackjack"]:
            print("You got a blackjack! You win!")
        else:
            while input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                player_cards.append(draw_card())
                if player_cards[2] == blackjack_definitions["ace_soft"] and\
                        player_card_value > blackjack_definitions["ace_soft"]:
                    player_cards[2] = blackjack_definitions["ace_hard"]
                player_card_value = calculate_score(player_card_value, player_cards[2])
                print(f"Your cards: {player_cards}, current score: {player_card_value}")
                if player_card_value > blackjack_definitions["blackjack"]:
                    print(f"Score is {player_card_value}, you lose.")
                    lose = True
                    break
                elif player_card_value == blackjack_definitions["blackjack"]:
                    print("You got a blackjack! You win!")
                    win = True
                    break
                print(f"The dealers first card is {dealer_cards[0]}")

            if not win and not lose:
                while dealer_card_value < blackjack_definitions["dealer_stop"]:
                    dealer_cards.append(draw_card())
                    if dealer_cards[2] == blackjack_definitions["ace_soft"] and\
                            dealer_card_value > blackjack_definitions["ace_soft"]:
                        dealer_cards[2] = blackjack_definitions["ace_hard"]
                    dealer_card_value = calculate_score(dealer_card_value, dealer_cards[2])
                    if dealer_card_value > blackjack_definitions["blackjack"]:
                        print(f"Dealer score is {dealer_card_value}, you win!")
                        lose = True
                        break
                    elif dealer_card_value == blackjack_definitions["blackjack"]:
                        print("The dealer got a blackjack! You lose.")
                        win = True
                        break

            if not win and not lose:
                print(f"Your final hand: {player_cards}, final score: {player_card_value}")
                print(f"Dealers final hand: {dealer_cards}, final score: {dealer_card_value}")
                if player_card_value == dealer_card_value:
                    print("Your score is the same as the dealers, you draw!")
                elif player_card_value > dealer_card_value and not player_card_value > 21:
                    print("Your score is higher than the dealers, you win!")
                else:
                    print("Your score is lower than the dealers, you lose!")

        play_again = input("Type 'y' to play again, type 'n' to quit: ")


def main():
    game()


if __name__ == '__main__':
    main()