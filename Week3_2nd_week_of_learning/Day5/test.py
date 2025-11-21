
from DailyChallenge import Card

suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

all_cards = []

for i in suit:
    for j in value:
        all_cards.append(Card(i,j))

print(all_cards)