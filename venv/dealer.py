from deck import Deck
from player import Player

class Dealer(Player):
    def __init__(self, name = "Dealer"):
        Deck.__init__(self)
        Player.__init__(self)
        self.name = name

    # METHODS
    def win(self, win_amt):
        print(f"The dealer won {win_amt}")

    def lose(self, lose_amt):
        print(f"The dealer lose {lose_amt}")

    def total_cards(self, *args):
        total = 0
        i = 0
        for card_number in args[i]:
            total = total + card_number[0]
            i = i + 1
        return total

"""
dealer = Dealer()
dealer.getCard()
"""