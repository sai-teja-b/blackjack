from casino.hand import Hand 

class Player():
    def __init__(self):
        self.money = 50
        self.hand = Hand()

    def add_winnings(self,winnings):
        self.money += winnings

    def can_place_bet(self, amount):
        return self.money >= amount

    def recieve_card(self, card):
        self.hand.add_card(card) 

    def empty_hand(self):
        self.hand.cards = []       

    @property
    def score(self):
        return self.hand.get_value()

    @property 
    def is_over(self):
        return self.hand.get_score()

    @property
    def has_blackjack(self):
        return self.hand.get_value()

    @property
    def cards(self):
        return self.hand.cards

def Dealer(Player):
    pass
    
