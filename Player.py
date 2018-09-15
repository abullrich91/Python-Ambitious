class Player:
    name = ""
    currentScore = 0
    acumulatedScore = 0
    hand = []
    playing = False
    played = False
    money = 0

    def __init__(self, name, money):
        self.name = name
        self.money = money
