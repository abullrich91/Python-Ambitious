from Player import *
from PlayerList import *


def addPlayer(name, startingMoney):
    PlayerList().players.append(Player(name, startingMoney))


def reachedTopScore(topScore):
    for player in PlayerList().players:
        if player.acumulatedScore > topScore:
            return True
    return False
