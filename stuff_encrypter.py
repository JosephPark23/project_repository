# encrypt the contents of your files!
from cryptography.fernet import Fernet
import base64 # converting bytes and strings
from os import system, name # clearing the terminal
import time # error handling messages

# clears the screen
def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


# making a key
def create_key():
    # use Fernet to make a key
    key = Fernet.generate_key()

    # provides user with key string
    key_string = base64.urlsafe_b64encode(key).decode()
    print("Here's your key - store it somewhere safe: " + key_string)

    # returns the key object
    f = Fernet(key)
    return f


# creates an encrypted file
def create_file():
    # obtains file name and content
    file_name = input("Enter the name of the file: ")
    content = input("Enter the content of your file: ")

    # adding content to file - if file exists, an exception is thrown
    try:
        file_content = open(file_name, "x")
        file_content.write(content)
        file_content.close()

    except FileExistsError:
        print("File already exists...")
        time.sleep(2)
        clear()
        create_file()

    # returns info
    return file_name


# encrypting the file
def encrypt_file(file_name, f):
    # opens the file
    with open(file_name, 'rb') as file:
        plaintext = file.read()

    # now they can't read it
    encrypted = f.encrypt(plaintext)

    # adds encrypted content to the file
    with open(file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


# makes an encrypted file
def create_encrypted_file():
    file_name = create_file()
    f = create_key()
    encrypt_file(file_name, f)


# but i need to read it now!!
def decrypt_file():
    # decrypting
    file_name = input("Enter the name of the file you want to decrypt: ")
    clear()
    # get the encrypted content
    try:
        with open(file_name, 'rb') as encrypted_file:
            encrypted_content = encrypted_file.read()

    except FileNotFoundError:
        print("File doesn't exsist...")
        time.sleep(2)
        clear()
        decrypt_file()

    key = input("Enter the key: ")

    # converts the string into readable bytes
    key_bytes = base64.urlsafe_b64decode(key.encode())
    f = Fernet(key_bytes)

    # decrypts the content
    decrypted_bytes = f.decrypt(encrypted_content)
    clear()

    # returns decoded bytes in the form of a string
    return decrypted_bytes.decode("utf-8")


# self explanatory
def main():
    choice = input("Do you want to:\n"
        "(1) Create an encrypted file,\n"
        "(2) Decrypt an encrypted file\n"
        "Enter a number (1/2): ")
    if choice == '1':
        clear()
        create_encrypted_file()
    elif choice == '2':
        clear()
        print("File Contents:\n" + decrypt_file())
    else:
        print("Invalid option. Try again: ")
        time.sleep(2)
        clear()
        main()


main()
