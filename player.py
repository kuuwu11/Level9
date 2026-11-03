#Player Classes

import random
from collections import deque
class Player:
    player_count = 0
    def __init__ (self, deck, name=None):
        Player.player_count += 1
        self.number = Player.player_count
        self.name = name if name else f"Player {self.number}"

        deck.shuffle()
        self.hand = deque(deck.cards)

    # Take top cards
    def draw_card(self):
        if not self.has_cards():
            return None
        return self.hand.popleft()

    #Add won cards to bottom
    def add_cards(self, cards):
        won_cards = list(cards)
        random.shuffle(won_cards)
        self.hand.extend(won_cards)

    #Card count for players
    def card_count(self):
        return len(self.hand)

    #Check to make sure the player still has cards
    def has_cards(self):
        return len(self.hand) > 0

    #Print the results
    def __str__(self):
        return f"{self.name} has {self.card_count()} cards."
