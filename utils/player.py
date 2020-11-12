"""
create a class `Player` that contains these attributes:

- `cards` which is a list of `Card`. *(you will need to import `Card` from `card.py`)*.
- `turn_count` which is an int starting a 0.
- `number_of_cards` which is an int starting at 0.
- `history` which is a list of `Card` that will contain all the cards played by the player.

And some methods:

- `play()` that will:
  - **randomly** pick a `Card` in `cards`.
  - Add the `Card` to the `Player`'s `history`.
  - Print: `{PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}`.
  - return the `Card`.
"""


from random import randint
from card import Card

class Player:
    def __init__ (self, name: str):
        self.name = name
        self.cards = []  
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def play (self):
        chosenNbr = randint (0, len(self.cards)-1) 
        chosenCard = self.cards [chosenNbr]
        self.turn_count += 1
        self.history.append (chosenCard)
        print (self.name, self.turn_count, "played: ", chosenCard.value, chosenCard.icon)

"""
test = Player("Melvin")
test.cards.append (Card("red", "♥", "3"))
test.play ()
"""

"""
Create a `Deck` class that contains:

- An attribute `cards` which is gonna contain a list of instances of `Card`.
- A `fill_deck()` method that will fill `card()` with a complete card game
  *(an instance of  'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K'
  for each possible symbol [♥, ♦, ♣, ♠])*. Your deck should contain **52 cards at the end**.
- A `shuffle()` method that will shuffle all the `Card` instances of `cards`.
- A `distribute()` that will take a list of `Player` as parameter
  and will distribute the cards evenly between all the players.
"""

class Deck:
    def __init__ (self):
        self.cards = []

    def fill_deck (self):
        

    def shuffle (self):

    def distribute (self):
"""
