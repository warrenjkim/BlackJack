from src.deck import Deck
from src.hand import Hand

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0
        
        
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
                
            except:
                print("Enter a number")
            
        while game_number < games_to_play:
            game_number += 1
            
            deck = Deck()
            deck.shuffle()
            
            player_hand = Hand()
            dealer_hand = Hand(dealer = True)
            
            for i in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())
                
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()
            
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Hit or Stand? ").lower()
                print()
                
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal())
                    player_hand.display()
                    
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()
            
            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal())
                dealer_hand_value = dealer_hand.get_value()
                
            dealer_hand.display(show_dealer_cards = True)
            
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            print("Final Results:")
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)
            
            self.check_winner(player_hand, dealer_hand, game_over = True)
            
            
        
    def check_winner(self, player_hand: Hand, dealer_hand: Hand, game_over = False) -> bool:
        if not game_over:
            if player_hand.get_value() > 21 or dealer_hand.is_blackjack():
                print("Dealer wins")
                return True
                
            elif dealer_hand.get_value() > 21 or player_hand.is_blackjack():
                print("You win")
                return True
                
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Tie")
                return True
                
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win")
            
            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie")
            
            if player_hand.get_value() < dealer_hand.get_value():
                print("Dealer wins")
                
            return True
        
        return False