from PlayerList import *
from random import randint
from itertools import cycle

def startRound(deck):
    startPosition = -1
    topNumber = -1
    for player in PlayerList().players:
        player.playing = False
        player.played = False
        card = deck[randint(0, len(deck)-1)]
        deck.remove(card)
        player.hand.append(card)
    for i in range (0, len(PlayerList().players)-1):
        if PlayerList().players[i].hand[0].number > topNumber:
            topNumber = PlayerList().players[i].hand[0].number
            startPosition = i
    PlayerList().players[startPosition].playing = True


def playerLeftToPlay():
    for player in cycle(PlayerList().players):
        if not player.played:
            return True
    return False
