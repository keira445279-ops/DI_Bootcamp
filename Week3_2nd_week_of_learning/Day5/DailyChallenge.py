# ****************************Exercise 2: Create a deck of cards class*****************************************
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

import random

class Deck:
    def __init__(self):
        
        suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        self.all_cards = []
        for i in suit:
            for j in value:
                self.all_cards.append(Card(i,j))

    def shuffle_cards(self):
        random.shuffle(self.all_cards)
         
    def deal_card(self):
        return self.all_cards.pop()

deck = Deck()
result = deck.deal_card()
print (result)