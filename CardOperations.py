from Suit import *
from Card import *


def __isLosingCard(card):
    return card.number in range(11, 13)


def __isBlackThree(card):
    return card.number == 3 and card.suit in [Suit.CLUBS, Suit.SPADES]


def __isRedThree(card):
    return card.number == 3 and card.suit in [Suit.DIAMONDS, Suit.HEARTS]


def createDeck():
    deck = []
    for i in range(0, len(Suit)):
        for j in range(0, 13):
            deck.append(Card(i, j))
    return deck


def checkCardAndManage(card, player):
    if __isLosingCard(card):
        player.currentScore = 0
        player.playing = False
        player.played = True
    elif __isBlackThree(card):
        player.playing = False
        player.played = True
    elif __isRedThree(card):
        player.currentScore = player.currentScore * 2
