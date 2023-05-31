from os import system, name
import time

deck = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K",
        "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]


def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac
    else:
        _ = system('clear')


class War:

    def __init__(self):
        self.deck = deck
        self.player_deck = []
        self.computer_deck = []

    def deck_shuffle(self, deck_):
        return deck_.shuffle()

    def deal(self):
        self.player_deck = [self.player_deck.append(self.deck[i]) for i in range(26)]
        self.computer_deck = [self.computer_deck.append(self.deck[i]) for i in range(26, 52)]

    def check(self):
        if len(self.computer_deck) < 1:
            print("You won!")
            quit()
        elif len(self.player_deck) < 1:
            print("You lost!")
            quit()
        else:
            return True

    def play(self):
        while True:
            check()
