import random as ran

# Create a deck of cards
cards_symbol = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [f'{rank} of {suit}' for suit in cards_symbol for rank in ranks]

# Shuffle the deck
ran.shuffle(deck)

# Print the shuffled deck
for card in deck:
    print(card)
