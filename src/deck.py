import random
from src.card import Card

class Deck:
    def __init__(self) -> None:
        self.cards = []
        suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))
    
    def shuffle(self) -> None:
        random.shuffle(self.cards)
        
    def deal(self, iterations = 1) -> list:
        cards_dealt = []
        
        for i in range(iterations):
            if len(self.cards) == 0:
                return cards_dealt
            cards_dealt.append(self.cards.pop())
        
        return cards_dealt
        
        