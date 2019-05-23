from deck import Deck

class Dealer(Deck):
    def __init__(self, name = "Dealer"):
        Deck.__init__(self)
        self.name = name

    # METHODS
    def win(self, win_amt):
        print(f"The dealer won {win_amt}")

    def lose(self, lose_amt):
        print(f"the dealer lose {lose_amt}")

    def getCard(self):
        return self.deal()

dealer = Dealer()
dealer.getCard()