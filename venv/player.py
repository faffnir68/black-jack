from deck import Deck

class Player(Deck):
    def __init__(self, name, balance = 0):
        Deck.__init__(self)
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account owner : {self.name}\nBalance : {self.balance}"

    def bet(self):
        while True:
            try:
                amt = int(input("How much do you want to bet ?"))
            except:
                print("Input an number please")
                continue
            else:
                break
        return amt

    def choice(self):
        while True:
                choice = input(f"{self.name}, what do want to do. One more card or not ? (Hit/Stay)").lower()
                if choice == 'hit' or choice == 'stay':
                    break
                else:
                    print(f"{self.name}, please enter the words 'Hit' or 'Stay'")
                    continue
        return choice

    def win(self, win_amt):
        self.balance = self.balance + win_amt
        print(f"You won {win_amt}")

    def lose(self, lose_amt):
        self.balance = self.balance - lose_amt
        print(f"You lose {lose_amt}")

d = Deck()
player1 = Player("Anthony", 100)
d.shuffle_cards()
print(d)
player_fc = (d.deal())
player_sc = (d.deal())
dealer_fc = (d.deal())
dealer_sc = (d.deal())
print(player_fc, player_sc)
print(dealer_fc, dealer_sc)
pb = player1.bet()


if player_fc[0] > player_sc[0]:
    print(player_fc[0], player_fc[1])
else:
    print(player_sc[0], player_sc[1])


