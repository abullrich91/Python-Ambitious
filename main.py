from CardOperations import *
from PlayerOperations import *
from GameOperations import *
import copy


def Ambicioso(topScore, startingMoney):
    players = ["Ale", "Lore", "Mati", "Santi"]
    deck = createDeck()
    backupDeck = copy.copy(deck)
    for card in deck:
        print("Number: " + str(card.number) + " Suit: " + str(card.suit))
    for player in players:
        addPlayer(player, startingMoney)
    while not reachedTopScore(topScore):
        deck = copy.copy(backupDeck)
        startRound(deck)
        while playerLeftToPlay() or len(deck) == 0:
            drawCard()
            checkCardAndManage()





Ambicioso(100, 20)
