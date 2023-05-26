from os import system, name
import time


def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac
    else:
        _ = system('clear')


class Hangman:

    # initializes variables
    def __init__(self):
        self.word = word
        self.wrong_guesses = 0
        self.guessed_so_far = ['_']*len(self.word)
        self.positions = []

    # checks if letter user enters is actually a letter
    def validate(self, user_guess):
        if user_guess.isalpha() and len(user_guess) == 1:
            return True
        else:
            print("u did not enter a letter")
            return False

    # checks if the letter user guessed is in the word
    def check(self, user_guess):
        self.positions = []
        for i, char in enumerate(self.word):
            if char == user_guess:
                self.positions.append(i)
        return bool(self.positions)

    # ends the game to see if person won
    def end_game(self, guessed_so_far, wrong_guesses):
        # there's probably a more efficient way to do this, but I'm not that good
        if "_" not in guessed_so_far:
            print(f"yay u won the word was {self.word}")
            quit()
        elif wrong_guesses == 8:
            print('hangman ded')
            quit()

    # play part
    def play_hangman(self):
        while self.wrong_guesses < 7:
            time.sleep(3)
            clear()
            print(self.guessed_so_far, f"\nnumber of wrong guesses left: {7-self.wrong_guesses}\n")
            self.end_game(self.guessed_so_far, self.wrong_guesses)
            user_guess = input('Enter your guess!: ')
            if not self.validate(user_guess):
                continue
            if not self.check(user_guess):
                print('The letter that you entered is not in the word')
                self.wrong_guesses += 1
                continue
            print('check works', self.check(user_guess))
            for pos in self.positions:
                self.guessed_so_far[pos] = user_guess
        print("hangman dead")


print("Welcome to Hangman! For instructions, go to www.wikihow.com/Play-Hangman.")
time.sleep(5)
while True:
    clear()
    word = input("Enter a word: ")
    if word.isalpha():
        break
    else:
        print('u did not enter a word, try again')
h = Hangman()
h.play_hangman()
