# if running this in an IDE, please turn terminal emulation on for this to work
from os import system, name
import time
import random

deck = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K",
        "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2, "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
face_cards = {"A": 14, "K": 13, "Q": 12, "J": 11}

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

    def deck_shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        for i in range(26):
            self.player_deck.append(self.deck[i])
            self.computer_deck.append(self.deck[i + 26])

    def convert_facecard(self, card):
        if card in face_cards:
            return face_cards[card]
        else:
            return card

    def compare_cards(self, player_card, computer_card):
        return player_card > computer_card

    def war(self, turn):
        player_war = self.player_deck[turn:turn + 4]
        computer_war = self.computer_deck[turn:turn + 4]
        war_length = min(len(player_war), len(computer_war))
        if war_length >= 4:
            player_war_values = [self.convert_facecard(card) for card in player_war]
            computer_war_values = [self.convert_facecard(card) for card in computer_war]
            if player_war_values[war_length - 1] > computer_war_values[war_length - 1]:
                self.player_deck.extend(computer_war[:war_length])
                del self.computer_deck[turn:turn + war_length]
            elif player_war_values[war_length - 1] < computer_war_values[war_length - 1]:
                self.computer_deck.extend(player_war[:war_length])
                del self.player_deck[turn:turn + war_length]
        else:
            if len(player_war) < 4:
                del self.player_deck[turn:]
            if len(computer_war) < 4:
                del self.computer_deck[turn:]

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
        self.deck_shuffle()
        self.deal()
        turn = 0
        print(f"Your deck: {self.player_deck}\nComputer: {self.computer_deck}")
        while True:
            self.check()
            player_card = self.convert_facecard(self.player_deck[turn])
            comp_card = self.convert_facecard(self.computer_deck[turn])
            print(player_card, comp_card)
            if player_card != comp_card:
                if self.compare_cards(player_card, comp_card):
                    self.player_deck.append(comp_card)
                elif not self.compare_cards(player_card, comp_card):
                    self.computer_deck.append(player_card)
            elif player_card == comp_card:
                self.war(turn)
            turn += 1


w = War()
w.play()
