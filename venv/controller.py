from player import Player
from deck import Deck
from dealer import Dealer

def replay():
    return input("Do you want to continue playing ? ").lower().startswith('y')

print("Welcome to BlacJack game with Python!")
player_name = input("Player 1. Enter your name to begin:")
player1 = Player(player_name)
print(player1)

while True:
    game_on = True

    while game_on:
        # PLayer initialisation
        dealer = Dealer()

        # Player bet
        print(player1)
        pb = player1.bet()
        print(f"You still have : {player1.balance - pb}")
        # Creation and shuffle of the deck
        d = Deck()
        d.shuffle_cards()
        p1_cards_list = []
        d_cards_list = []



        # Distribution of the cards
        # Player
        p1_cards_list.append(d.deal())
        p1_cards_list.append(d.deal())
        player_score = player1.total_cards(p1_cards_list)
        print(f"\nPlayer first card is : {p1_cards_list[0]}\nPlayer second card is : {p1_cards_list[1]}")
        print(f"Your total is : {player_score}")

        # Dealer
        d_cards_list.append(d.deal())
        d_cards_list.append(d.deal())
        dealer_score = dealer.total_cards(d_cards_list)
        print(f"\nDealer first card is hidden. \nDealer second card is the following : {d_cards_list[1]}\n")
        print(f"Dealer's' total is : {dealer_score}")

        # Player's choice
        player_turn = True
        dealer_turn = True
        final_check = True

        while player_turn:
            if player1.choice() == 'hit':
                p1_cards_list.append(d.deal())
                print(f"You got a new card : {p1_cards_list[-1]}")
                player_score = player1.total_cards(p1_cards_list)
                print(f"Your total now is : {player_score}")
                if player_score > 21:
                    print(player1.lost_21(player_score))
                    player1.lose(pb)
                    dealer_turn = False
                    final_check = False
                    break
                elif player_score == 21:
                    print(player1.win_21())
                    player1.win(pb)
                    dealer_turn = False
                    final_check = False
                    break
                else:
                    print(player1.less_21(player_score))
            else:
                player_score = player_score
                break

        while dealer_turn:
            while dealer_score < 17:
                d_cards_list.append(d.deal())
                print(f"The dealer got a new card : {d_cards_list[-1]}")
                dealer_score = dealer.total_cards(d_cards_list)
                print(f"The total for the dealer now is : {dealer_score}")
                if dealer_score > 21:
                    print('La banque saute !!')
                    player1.win(pb)
                    final_check = False
                    break
            else:
                dealer_score = dealer_score
                break

        # IF score du dealer >
        while final_check:
            if dealer_score < player_score or dealer_score > 21:
                print("Player wins")
                player1.win(pb)
                break
            else:
                print("The bank wins (as ever ;-) )")
                player1.lose(pb)
                break

        # Stop the current game
        game_on = False
    if not replay():
        break
