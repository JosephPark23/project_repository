from cryptography.fernet import Fernet # for obvious purposes
import base64 # converting bytes and strings
from os import system, name # clearing the terminal
from extract_gmail_from_user import get_body
from send_email import send_message
from time import sleep


# clears the screen
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

# retry for terminal
def retry(seconds):
    sleep(seconds)
    clear()


# generates the key string and gives it to the user
def generate_key_string():
    # uses Fernet to generate key
    key = Fernet.generate_key()
    f = Fernet(key)

    # provides user with key string
    key_string = base64.urlsafe_b64encode(key).decode()
    print("Here's your key - store it somewhere safe: " + key_string)
    input("\nPress enter to proceed: ")
    clear()
    # returns the fernet object
    return f

# for when the user already has an existing key
def get_key_string():
    # get key string from user and converts the string to bytes
    key_string = input("Enter your keystring: ")
    key = base64.urlsafe_b64decode(key_string.encode())

    # store it in Fernet object and return
    try:
        f = Fernet(key)
    except ValueError:
        print("Invalid key.")
        retry(1)
        get_key_string()

    return f


# gets the message and returns it in bytes
def get_new_message():
    # obtains message from the user
    message = input("What's your message?: ")

    # returns the message into bytes
    return message.encode()


# encrypts plaintext bytes
def encrypt_plaintext(bytes, f):
    encrypted_bytes = f.encrypt(bytes)
    return encrypted_bytes.decode()

# decrypts an encrypted string
def decode_encrypted_string(encrypted_string, f):
    # converts message to bytes
    decrypted_bytes = f.decrypt(encrypted_string)

    # converts to string and return
    return decrypted_bytes.decode()


# getting the key
def get_key():
    choice = input("If you have a key, please press enter. "
                   "\nOtherwise, please press the 'a' key "
                   "\nand press 'enter' to generate a new key string: ")
    clear()
    if choice == '':
        f = get_key_string()
    elif choice == 'a':
        f = generate_key_string()
    else:
        print("Please enter a valid option.")
        retry(1)
        get_key()

    return f


# sends an encrypted email
def send_encrypted_email():
    # gets the key and the user's message
    f = get_key()
    message = get_new_message()

    # encrypts and returns as string
    encrypted_string = encrypt_plaintext(message, f)

    # gets the identifiers needed to send: message id is to help the recipient locate the email with the decrypter program
    message_id = int(input("What's the message ID?: "))
    recipient_email = input("What's the recipient email?: ")
    clear()

    # sends the email
    send_message(message_id, encrypted_string, recipient_email)


# decrypts an email with specific email ID
def decrypt_email():
    # gets the key from the user
    f = get_key_string()

    # gets the identifiers and the text
    message_id = int(input("What's the message ID?: "))
    encrypted_text = get_body(message_id)
    clear()

    # print decrypted text
    print(f"Your decrypted text:\n{decode_encrypted_string(encrypted_text, f)}")

# run the program
def main():
    try:
        choice = int(input("Welcome to the Secure Message Service. Would you like to"
          "\n(1) Send an encrypted message"
          "\n(2) Decrypt a message"
          "\nEnter your choice (1/2): "))
        if choice == 1:
            clear()
            send_encrypted_email()
        elif choice == 2:
            clear()
            decrypt_email()
        else:
            print("Not a valid input.")
            retry(1)
            main()
    except ValueError:
        print("Not a valid input.")
        retry(1)
        main()


main()
