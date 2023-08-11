from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime as dt
from pyfirmata import Arduino, util
from time import sleep
import pyfirmata as pyf

# initialize board
board = pyf.Arduino('COM5')
it = pyf.util.Iterator(board)
it.start()

# initialize output
board.digital[13].mode = pyf.OUTPUT

f = open("arduino_log.txt", "x")


# scrape sunrise and sunset times
def get_object():
    # opens and reads the page
    url = "https://www.sunrisesunsettime.org/north-america/united-states/ardsley.htm"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    # finds the specific elements and returns the sunrise and sunset times
    element = soup.find(class_="sunrise-time")
    sunrise_time_ = str(element.get_text()).strip()
    element_one = soup.find(class_="sunset-time")
    sunset_time_ = str(element_one.get_text()).strip()
    return sunrise_time_, sunset_time_


while True:
    # formats the returned times
    sunrise_time_str, sunset_time_str = get_object()
    unformatted_time = dt.strptime(sunrise_time_str, "%I:%M")
    sunrise_time = unformatted_time.strftime("%H:%M")
    unformatted_time_ = dt.strptime(sunset_time_str, "%H:%M")
    sunset_time = unformatted_time_.strftime("%H:%M")

    # checks if time matches sunset time
    now = dt.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    print(sunset_time)
    if current_time == sunset_time:
        # activates the board
        board.digital[13].write(1)
        sleep(4)
        board.digital[13].write(0)
        print("System activated at: ", dt.now())
