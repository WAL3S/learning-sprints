from enum import Enum
import random

class Suit(Enum):
    HEARTS='Hearts'
    SPADES='Spades'
    DIAMONDS='Diamonds'
    CLUBS='Clubs'

class Rank(Enum):
    TWO   = '2'
    THREE = '3'
    FOUR  = '4'
    FIVE  = '5'
    SIX   = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE  = '9'
    TEN   = '10'
    JACK  = 'J'
    QUEEN = 'Q'
    KING  = 'K'
    ACE   = 'A'
    
class Card():

    def __init__(self, rank:Rank, suit:Suit):
        self.rank=rank
        self.suit=suit

    def __repr__(self):
        return f'{self.rank.value} of {self.suit.value}'

def make_cards():
    return [Card(rank, suit) for suit in Suit for rank in Rank ]
    
class Deck():
    
    def __init__(self):
        self.deck=make_cards()
        self.index=0
    
    def shuffle_deck(self):
        random.shuffle(self.deck)

    def __iter__(self):
        self.index=0
        return self
    
    def __next__(self):
        if self.index>=len(self.deck):
            raise StopIteration
        card=self.deck[self.index]
        self.index+=1
        return card
    
    def draw(self):
        try:
            return next(self)
        except StopIteration:
            return None

def main():
    deck = Deck()
    deck.shuffle_deck()
    print("Drawing all 52 cards:")
    for card in deck:
        print(card)

if __name__ == "__main__":
    main()
