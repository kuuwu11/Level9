# Setup:
from cards import Deck
from player import Player

# Welcome
print("Welcome to Two-Deck War!")

# Create the two decks and players
deck1 = Deck()
deck2 = Deck()
player1 = Player(deck1, name="Player 1")
player2 = Player(deck2, name="Player 2")

# Main Game Loop
while player1.has_cards() and player2.has_cards():
    cards_in_play = []

    # Begin round
    input("Press Enter to play the next round.")

    # Both players draw a card
    c1 = player1.draw_card()
    c2 = player2.draw_card()
    cards_in_play.extend([c1, c2])
    print(f"{player1.name} drew {c1}.")
    print(f"{player2.name} drew {c2}.")

    # Compare and War (using .value)
    if c1.value > c2.value:
        player1.add_cards(cards_in_play)
        print(f"{player1.name} wins the round and takes {len(cards_in_play)} cards.")
    elif c2.value > c1.value:
        player2.add_cards(cards_in_play)
        print(f"{player2.name} wins the round and takes {len(cards_in_play)} cards.")
    else:
        print("War!")
        while True:
            if not player1.has_cards():
                player2.add_cards(cards_in_play)
                break
            if not player2.has_cards():
                player1.add_cards(cards_in_play)
                break

            # Players draw a card each
            c1 = player1.draw_card()
            c2 = player2.draw_card()
            cards_in_play.extend([c1, c2])
            print(f"{player1.name} drew {c1}.")
            print(f"{player2.name} drew {c2}.")

            if c1.value > c2.value:
                player1.add_cards(cards_in_play)
                print(f"{player1.name} wins the war and takes {len(cards_in_play)} cards.")
                break
            elif c2.value > c1.value:
                player2.add_cards(cards_in_play)
                print(f"{player2.name} wins the war and takes {len(cards_in_play)} cards.")
                break
            else:
                print("War!")

    # Round Summary
    print(f"{player1.name} has {player1.card_count()} cards.")
    print(f"{player2.name} has {player2.card_count()} cards.")

# Final Results
if not player1.has_cards():
    print(f"{player2.name} has collected all of the cards. {player2.name} wins the game!")
elif not player2.has_cards():
    print(f"{player1.name} has collected all of the cards. {player1.name} wins the game!")
