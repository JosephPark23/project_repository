# Imports necessary modules: bs4 and urllib for webscraping, os and time for cleaning up interface
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
from os import name, system
import time


def clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')


# opens the url and scrapes the text from the page
def open_page():
    artist_name = input("Enter in the name of the artist: ")
    song_name = input("enter in the name of the song: ")

    artist_name = artist_name.lower()
    artist_name = artist_name.replace(" ", "")
    song_name = song_name.lower()
    song_name = song_name.replace(" ", "")

    url = f"https://www.azlyrics.com/lyrics/{artist_name}/{song_name}.html"
    # exception handling for typos and other spelling mistakes
    try:
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        print(soup.get_text())
    except urllib.request.HTTPError:
        print("We can't find what you were looking for. Check for typos and spelling errors. Try again?")
        time.sleep(3)
        clear()
        open_page()


open_page()
