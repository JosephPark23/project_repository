# Note: Do not use this program for commercial use, personal use only
# Imports necessary modules: bs4 and urllib for webscraping, os and time for cleaning up interface, string and colorama
# and utilities for aesthetics
# Run inside terminal
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
from os import name, system
import time
import string
import colorama as cr
from utilities import Util as util

cr.init(autoreset=True)


# clears screen
def clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')


# works in conjunction with the tokenize() function to remove punctuation
def remove_punctuation(string_):
    # creates translation table
    translator = str.maketrans("", "", string.punctuation)

    # removes punctuation using translate
    clean_string = string_.translate(translator)

    return clean_string


# standardizes input for url
def tokenize(artist, song):
    # converts all characters to lowercase and strips of whitespace
    artist_name = remove_punctuation(artist)
    artist_name = artist_name.lower().replace(" ", "")

    # converts all characters to lowercase and strips of whitespace
    song_name = remove_punctuation(song)
    song_name = song_name.lower().replace(" ", "")

    return artist_name, song_name


# intitializes the url
def get_url():
    song_name = input("what's the name of the song?: ")
    artist_name = input("what's the primary artist's name? (if it doesn't work, try excluding the word 'the'): ")
    artist_name, song_name = tokenize(artist_name, song_name)
    url = f"https://www.azlyrics.com/lyrics/{artist_name}/{song_name}.html"
    return url


# opens and reads the lyrics page
def get_object(url):
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    x = soup.find(class_="col-xs-12 col-lg-8 text-center")
    a = str(x.get_text())
    return a


# prints lyrics in specific format
def format_lyrics(lyrics):
    # isolates the lyrics from the rest of the text
    pos_one = lyrics.find("Lyrics")
    pos_two = lyrics.find("Submit Corrections")  # print lyrics only
    x = lyrics[pos_one + 11:pos_two - 18]
    print(util.bold + "\n==========================\n||hey, it's your lyrics!||\n==========================\n\n")

    # prints the lyrics line-by-line
    lines = x.splitlines()
    for line in lines:
        print(f"{cr.Fore.CYAN}{line}")
        time.sleep(0.1)

    # checks if user wishes to look up another song
    y = input(util.bold + "\n=============(scroll up for your lyrics!)=============\nif u wanna find another "
                          "song, just hit that enter key!\nif u don't, that's okay! press 'q', "
                          "then enter!\n======================================================\n")
    return y


# checks if user wants to leave or not
def decision(x):
    if x == 'q':
        clear()
        print(util.bold + "hey hey hey goodbye~")
        time.sleep(2)
        quit()
    else:
        clear()


# handles the urllib HTTP error
def handle_exception():
    print("\n\ncan't find what u want, maybe cuz:\n1. ur spelling sucks\n2. sometimes the artist of the song "
          "is not who u\n"
          "think it is, or the song name is wrong\n3. this program isn't all-encompassing")
    time.sleep(8)
    clear()
    open_page()


# runs the program
def open_page():
    print(util.bold + "welcome to my lyrics finder! look up your lyrics here!\n")
    while True:
        try:
            url = get_url()
            lyrics = get_object(url)
            decision(format_lyrics(lyrics))

        # exception handling for typos and other spelling mistakes, and to keep the loop running smoothly
        except urllib.request.HTTPError:
            handle_exception()


open_page()
