# Card and Deck part

import random

class Card:

    RANK_NAMES = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    # Set the card's value and suit
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # Show the card's name
    def __str__(self):
        rank = self.RANK_NAMES.get(self.value, str(self.value))
        return f"the {rank} of {self.suit}"


# This class creates a deck of 52 cards
class Deck:

    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]

    # Create all 52 cards
    def __init__(self):
        self.cards = []
        for suit in self.SUITS:
            for value in range(2, 15):
                self.cards.append(Card(value, suit))

    # Shuffle the cards
    def shuffle(self):
        random.shuffle(self.cards)

    # Draw one card from the deck
    def deal_card(self):
        if not self.cards:
            return None
        return self.cards.pop()

    # Add one card to the bottom of the deck
    def add_card(self, card):
        self.cards.insert(0, card)

    # Add multiple cards to the bottom of the deck
    def add_cards(self, cards):
        self.cards[0:0] = cards

    # Count how many cards are left
    def card_count(self):
        return len(self.cards)
