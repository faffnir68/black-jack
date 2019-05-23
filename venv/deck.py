import random
from random import shuffle

class Deck():

    def __init__(self):
        cards_color = ['Heart', 'Diamond', 'Spade', 'Club']
        cards_nb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        combo_cards = []
        for c_col in cards_color:
            for c_nb in cards_nb:
                result = c_nb, c_col
                combo_cards.append(result)
        print(combo_cards)

    def shuffle_cards(self):
        print(shuffle(combo_cards))


d = Deck()
d.shuffle_cards()


"""
========= BASES =========

CREER UN DECK, UN JOUEUR ET UN DEALER

1) le DECK de cartes
    ====== ATTRIBUTS =====
    - le deck de cartes doit être composé de 4 couleurs de 10 chiffres et de 3 figures allant de 1 à 10 inclus
    (- la carte de l'as vaut 1 OU 11)
    ====== ACTIONS ======
    - mélange du deck

4) le JOUEUR :
    ==== ATTRIBUTS ====
    Le joueur a un compte bancaire
        - le compte bancaire du joueur peut etre débité
        - le compte bancaire du joueur peut être crédité
        - le compte bancaire du joueur doit être vérifié à chaque mouvement d'argent
        - le joueur commence avec 2 cartes au hasard ET visibles
    ==== ACTIONS ====
        - le joueur doit utiliser BET en début de partie
        - le joueur peut utiliser STAY ---> arrête de recevoir des cartes
        - le joueur peut utiliser HIT ----> demande une nouvelle carte au deck
5) le DEALER :
    ==== ATTRIBUTS ====
        - le dealer commence avec 2 cartes au hasard
        - l'une des 2 cartes est caché
        - l'autre carte est révélé
    ==== ACTIONS ====
        - le dealer peut utiliser HIT
        

======= ETAPES DE JEU =======

"""