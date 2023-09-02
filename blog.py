from datetime import datetime as dt
from os import system, name
from time import sleep


# for cleaning up the screen
def clear():
    # windows
    if name == 'nt':
        _ = system('cls')
    # mac
    else:
        _ = system('clear')


# creates the blog file or handles the exception if blog file already exists
def create_blog():
    try:
        f = open("blog.txt", "x")
        f.write("My Personal Python Blog: ")
        f.close()

    # after first use
    except FileExistsError:
        print("Accessing blog")
        sleep(2)
        for i in range(3):
            sleep(1)
            print('...')
        clear()


# creates a new entry
def new_entry():
    # records the date, time, title and entry
    now = dt.now()
    dt_string = now.strftime("Date: %B %d, %Y \nTime: %I:%M %p")
    title_text = input("Enter the entry title: ")
    entry_text = input("Enter your text: ")

    # saves the data in the blog.txt file
    for i in range(3):
        sleep(0.5)
        print('\n...')
    clear()
    f = open('blog.txt', 'a')
    f.write(f"{format_entry(entry_text, title_text, dt_string)}")
    f.close()


# formats the entry
def format_entry(entry_text, title_text, dt_string):
    # variables for formatting
    x = '#' * 90
    return_text = []
    current_line = []
    words = entry_text.split()

    # creates "margins" to make the text appear more organized
    if len(words) <= 16:
        entry_text = f"\n\n====[ {title_text} ]====\n\n{entry_text}\n\n{dt_string}\n\n{x}"
        return entry_text
    
    for word in words:
        if len(current_line) < 16:
            current_line.append(word)
        else:
            line = ' '.join(current_line)
            return_text.append(f'{line}')
            current_line = []

    # adds finishing touches and returns the formatted text
    return_text = '\n'.join(return_text)
    entry_text = f"\n\n====[ {title_text} ]====\n\n{return_text}\n\n{dt_string}\n\n{x}"
    return entry_text


# opens and prints the contents of the blog
def open_blog():
    f = open("blog.txt")
    print(f.read())
    input("\n======================\npress enter to proceed\n======================\n")
    clear()


# finds specific post by title
def access_post_():
    title = input('enter title: ')
    clear()

    # finds and prints the post
    f = open("blog.txt")
    blog_object = str(f.read())
    index_one = blog_object.find(f'====[ {title} ]====')
    if index_one == - 1:
        print("post not found")
        sleep(3)
        clear()
        return
    index_two = blog_object.find('###', index_one+6+len(title))
    print(f"post that you wanted is here:\n{blog_object[index_one:index_two]}")
    input("\n======================\npress enter to proceed\n======================\n")
    clear()


def main():
    create_blog()
    while True:
        choice = int(input("what you wanna do?\n(1) write a new entry\n(2) read the blog\n(3) access a blog post by "
                           "title\nenter your choice: "))
        if choice == 1:
            clear()
            new_entry()
        elif choice == 2:
            clear()
            open_blog()
        elif choice == 3:
            clear()
            access_post_()


main()
