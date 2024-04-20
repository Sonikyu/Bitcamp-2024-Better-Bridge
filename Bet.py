class Bet:
    def __init__(self, suit, level):
        self.suit = suit
        self.level = level
        self.id = self.suit * 6 + self.level - 7
    def __lt__(self, otherBet):
        return self.id - otherBet.id