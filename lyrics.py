# Note: Do not use this program for commercial use. Personal use only.
# Imports necessary modules: bs4 and urllib for web scraping, os and time for cleaning up interface
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
from os import name, system
import time
import string


# clears screen
def clear():
    if name == 'nt':
        _ = system('cls')
    # for Mac and linux
    else:
        _ = system('clear')


# works in conjunction with the tokenize() function to remove punctuation
def remove_punctuation(string_):
    # creates translation table
    translator = str.maketrans("", "", string.punctuation)

    # removes punctuation using translate
    clean_string = string_.translate(translator)

    return clean_string


# standardizes input for URL
def tokenize(artist, song):

    # converts all characters to lowercase and strips of whitespace
    artist_name = remove_punctuation(artist)
    artist_name = artist_name.lower().replace(" ", "")

    # converts all characters to lowercase and strips of whitespace
    song_name = remove_punctuation(song)
    song_name = song_name.lower().replace(" ", "")

    return artist_name, song_name


# initialize user input and URL
def open_page():
    print("welcome to my lyrics finder! look up your lyrics here!")
        while True:
        song_name = input("what's the name of the song?: ")
        artist_name = input("what's the artist's name? (try excluding the word 'the'): ")
        artist_name, song_name = tokenize(artist_name, song_name)
        url = f"https://www.azlyrics.com/lyrics/{artist_name}/{song_name}.html"
    
        try:
            # opens and reads the lyrics page
            page = urlopen(url)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            x = soup.find(class_="col-xs-12 col-lg-8 text-center")
            a = str(x.get_text())
            pos_one = a.find("Lyrics")
            pos_two = a.find("Submit Corrections")  # print lyrics only
            print("\n\n\nhey, it's your lyrics!:\n\n\n", a[pos_one+11:pos_two])
    
        # exception handling for typos and other spelling mistakes
        except urllib.request.HTTPError:
            print("can't find what u want, maybe cuz:\n1. ur spelling sucks\n2. ur song or artist info is just "
                  "wrong\n3. this program isn't all-encompassing")
            time.sleep(5)
            clear()
            open_page()


open_page()
