class Hand:
    def __init__(self, dealer = False) -> None:
        self.cards = []
        self.value = 0
        self.dealer = dealer
        
    def add_card(self, card_list) -> None:
        self.cards.extend(card_list)
    
    def calculate_value(self) -> None:
        self.value = 0
        
        for card in self.cards:
            has_ace = False
            if card.rank["rank"] == "A":
                has_ace = True
                
            self.value += int(card.rank["value"])
            
        if has_ace and self.value > 21:
            self.value -= 10
                
    def get_value(self) -> int:
        self.calculate_value()
        return self.value
    
    def is_blackjack(self) -> bool:
        return self.get_value() == 21
    
    def display(self, show_dealer_cards = False) -> None:
        print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
        
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_dealer_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)
            
        if not self.dealer:
            print("Value: ", self.get_value())
        print()
            
            