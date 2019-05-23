from deck import Deck

class Player(Deck):
    def __init__(self, name, balance = 0):
        Deck.__init__(self)
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account owner : {self.name}\nBalance : {self.balance}"

    def win(self, win_amt):
        self.balance = self.balance + win_amt
        print(f"You won {win_amt}")

    def lose(self, lose_amt):
        self.balance = self.balance - lose_amt
        print(f"You lose {lose_amt}")

d = Deck()
d.shuffle_cards()
player1 = Player("Anthony", 100)
player1.shuffle_cards()
player_fc = (player1.deal())
player_sc = (player1.deal())

if player_fc[0] > player_sc[0]:
    print(player_fc[0], player_fc[1])
else:
    print(player_sc[0], player_sc[1])


