class PlayerList:
    players = []
    instance = None

    def __init__(self):
        if not PlayerList.instance:
            PlayerList.instance = PlayerList.__PlayerList(self)

    def __PlayerList(self):
        return self