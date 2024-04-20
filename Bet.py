from BetSuit import BetSuit
class Bet:
    
    def __init__(self, suit, level):
        self.suit = suit
        self.level = level
        self.id = self.suit.value  + (self.level - 7) * 6

    def __str__(self) -> str:
        return self.suit.__str__() + str(self.level)
    
    def getID(self) -> str:
        return str(self.id)

    def __lt__(self, otherBet):
        return self.id - otherBet.id
    
class BetFactory:
    def __init__(self):
        self.Bets = []
        for level in range(7, 14):
            for suit in BetSuit:
                self.Bets.append(Bet(suit, level))
    
    def __str__(self):
        result = ""
        for bet in self.Bets:
            result += bet.__str__() + "|"
        return result
    
    def asIDs(self):
        result = ""
        for bet in self.Bets:
            result += bet.getID() + "|"
        return result




