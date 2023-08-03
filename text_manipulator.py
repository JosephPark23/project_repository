import time
from os import system, name


def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac
    else:
        _ = system('clear')


def alternate_caps(text):
    result = ""
    capitalize = True

    for char in text:
        if char.isalpha():
            if capitalize:
                result += char.upper()
            else:
                result += char.lower()
            capitalize = not capitalize
        else:
            result += char

    return result


while True:
    text = input("Welcome to text manipulator. To stop using this program, enter [-q-]: "
                 "\nEnter text: ")
    if text == '-q-':
        quit()
    choice = input("\nWhat would you like to do? \n1: [C]apitalize\n2: [l]owercase\n3: strip of ["
                   "w]hitespace\n4: [s]witchcase?\nEnter option: ")
    if choice == 'c':
        print(f"\nhere's your text: {text.upper()}")
    elif choice == 'l':
        print(f"\nhere's your text: {text.lower()}")
    elif choice == 's':
        print(f"\nhere's your text: {alternate_caps(text)}")
    elif choice == 'w':
        print(f"\nhere's your text: {text.replace(' ', '')}")
    time.sleep(2)
    input("press enter to clear screen: ")
    clear()
