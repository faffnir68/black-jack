
class Player():
    def __init__(self, name, balance = 0):
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

    