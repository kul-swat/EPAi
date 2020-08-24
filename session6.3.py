from enum import Enum
from enum import IntEnum
from random import randint

full_deck = []
player1_cards = []
player2_cards = []

class Cards(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Suits(Enum):
    SPADES = "spades"
    CLUB = "club" 
    DIAMOND = "diamond"
    HEART = "heart"

class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

for suit in Suits:
    for card in Cards:
        full_deck.append(PlayingCard(Cards(card), Suits(suit)))

for i in range(0, len(full_deck)):
    print("card: ", full_deck[i].card)
    print("suit: ", full_deck[i].suit)

def create_deck():
    for suit in Suits:
        for card in Cards:
            full_deck.append(PlayingCard(Card(card), Suits(suit)))
    
    return(full_deck)

def draw_card(deck):
    rand_card = randint(0, len(deck) - 1)
    return deck.pop(rand_card)

def deal_war():
    while(len(partial_deck) > 0):
        player1_cards.append(draw_card(partial_deck))
        player2_cards.append(draw_card(partial_deck))

create_deck()
partial_deck = list(full_deck)
deal_war()

for i in range(0, len(player1_cards)):
    if (player1_cards[i].card > player2_cards[i].card):
        print("player1 wins the hand with: ", player1_cards[i].card)
        print("player2 loses with: ", player2_cards[i].card)
    if (player1_cards[i].card < player2_cards[i].card):
        print("player 2 wins the hand with: ", player2_cards[i].card)
        print("player 1 loses the hand with: ", player1_cards[i].card)
