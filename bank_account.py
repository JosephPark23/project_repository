import time
from os import system, name


# I'm assuming we're using a numerical keyboard, but I implemented exception handling just in case


def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac
    else:
        _ = system('clear')


class Chase:

    def __init__(self):
        self.account_name = ''
        self.balance = 0
        self.deposit_amount = 0
        self.withdraw_amount = 0
        self.pin = 0
        self.helper = ''

    def check_pin(self):
        if len(list(str(self.pin))) == 4:
            return True
        else:
            return False

    def open_account(self):
        print("Thank you for opening a Chase account!")
        self.account_name = input("Please enter your first and last name: ")
        try:
            self.balance = int(input("What is your initial balance?: "))
        except ValueError:
            print("not a valid input")
            time.sleep(3)
            clear()
        try:
            self.pin = int(input("please enter a four-digit PIN: "))
        except ValueError:
            print("Not a number!")
            time.sleep(3)
            clear()
        if not self.check_pin():
            try:
                time.sleep(2)
                clear()
                self.pin = int(input("please enter a four-digit PIN: "))
            except ValueError:
                print("Not a number!")
                time.sleep(3)
                clear()

    def check_balance(self):
        print(f"your balance: {self.balance}")

    def deposit(self):
        try:
            self.deposit_amount = int(input("How much would you like to deposit?: "))
        except ValueError:
            print("did not enter a #.")
            time.sleep(3)
            clear()
        self.balance += self.deposit_amount
        print(f"your new balance: {self.balance}")

    def withdraw(self):
        try:
            self.withdraw_amount = int(input("How much would you like to withdraw?: "))
        except ValueError:
            print("did not enter a #.")
            time.sleep(3)
            clear()
        self.balance -= self.withdraw_amount
        print(f"your new balance: {self.balance}")

    def customer_support(self):
        clear()
        self.helper = input("Choose your customer support person! (1): Joe Biden. (2): Jungkook from BTS. (3): Dom "
                            "Toretto. (4) An Apache Attack Helicopter. Enter a number to choose: ")
        if self.helper == '1':
            input("Joe: Hi, I'm Joe Biden. Currently, I'm the president of the USA. I just took this job to de-stress. "
                  "What do you want help with?\n\n")
            print('\nJoe: Well, since I have no idea how to help you, bye! ')
        elif self.helper == '2':
            # I'm just guessing that this is how he speaks...no offense
            input("Jungkook: Wassup bro, it's jungkook from bts. Hope ya havin a good day. whatcha need help with?\n\n")
            print('\nJungkook: listen bro, i have no idea. i gotta get to my concert tour. Listen to one of my songs, '
                  '#ARMYforever, and bye!')
        elif self.helper == '3':
            input("Dom: Hey, it's Dom. I've got nothing but time. What do you want?\n\n")
            print("\nDom: All I know is that Chase hired me for some promo video. I gotta go film it now. Always "
                  "remember: "
                  "nothing is stronger than family. "
                  "Except for maybe an Apache attack helicopter. Those things are death machines. If I were on the "
                  "business end of one, I'd get out of there ASAP.")
        elif self.helper == '4':
            print("\nApologies for the inconvenience, but the Apache attack helicopter is currently on a "
                  "search-and-destroy mission in the mountains of Colorado. Please try again later. ")
        else:
            print("invalid input")
        time.sleep(3)


c = Chase()
c.open_account()


def bank():
    while True:
        time.sleep(4)
        clear()
        choice = input("What would you like to do? (1): Deposit. (2): Withdraw. (3): Check balance. (4): Contact "
                       "Customer Support. Choose a number: ")
        if choice == '1':
            c.deposit()
        elif choice == '2':
            c.withdraw()
        elif choice == '3':
            c.check_balance()
        elif choice == '4':
            c.customer_support()
        else:
            print("not a valid input")


bank()
