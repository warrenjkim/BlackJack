class Card:
    def __init__(self, rank: dict, suit: str) -> None:
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"