import smtplib
from bs4 import BeautifulSoup
import requests
from datetime import datetime as dt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import capwords
import re


# returns the date and time in a string format
def get_date():
    now = dt.now()

    # formats the date and time into a string
    dt_date = now.strftime("%B %d, %Y")
    dt_time = now.strftime("%I:%M %p")

    return dt_date, dt_time


# checks the day (A or B)
def get_day():
    url = "https://www.ardsleyschools.org/hs"

    # sends GET request to url
    response = requests.get(url)

    # parses the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # isolates text from within class
    element = soup.find(class_="ui-article-description")
    header = str(element.get_text())
    index = header.find(" day)")
    day = header[index - 1]

    # returns the day
    if day == 'A':
        return "a B day"
    else:
        return "an A day"


# gets the weather
def get_weather_data():
    url = 'https://forecast.weather.gov/MapClick.php?lat=41.0236&lon=-73.7949'

    # sends GET request to url
    response = requests.get(url)

    # parses the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # isolates the highs, lows, and conditions as text
    data = soup.find(id='seven-day-forecast-list')
    conditions = str((data.find(class_='short-desc')).get_text())
    high = str((data.find(class_='temp temp-high')).get_text())
    high = re.findall(r'\d+', high)
    high = f"with a high of {high[0]}°F"
    low = str((data.find(class_='temp temp-low')).get_text())
    low = re.findall(r'\d+', low)
    low = f"a low of {low[0]}°F"

    # returns aforementioned variables
    return conditions.lower(), high, low


# acquires PL position data
def get_record():
    url = "https://www.foxsports.com/soccer/liverpool-team"

    # sends GET request to url
    response = requests.get(url)

    # parses the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # formats and returns table position and game record in a [W-D-L] format
    element = soup.find(class_="mg-xl-t-7 mg-md-sm-t-5 ff-n fs-11 uc cl-wht")
    record = str(element.get_text())
    index = record.find('PREMIER LEAGUE') + 14
    formatted_text = f"Current Win Record and Table Position for Liverpool FC [W-D-L]: \n{capwords(record[:index])}"
    return formatted_text


# sends the actual email
def send_email(subject, body, to_email, from_email, password):
    # initializes email
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    msg.attach(MIMEText(body, "plain"))

    # exception handling in case of error
    try:
        # establishes connection with outlook SMTP server
        server = smtplib.SMTP("smtp-mail.outlook.com", 587)
        server.starttls()

        # logs in to sender email via app password
        server.login(from_email, password)

        # sends email
        server.sendmail(from_email, to_email, msg.as_string())
        print("Email sent successfully!")
        server.quit()
    except Exception as e:
        print(f"Failed to send email. Error: {e}")  # exception handling


# formats email
def format_email():
    date, time = get_date()
    bool_day = get_day()
    conditions, high, low = get_weather_data()
    table_data = get_record()
    greeting = "Good morning! Here's your daily briefing!"
    text = (f"Today is {date}. It is {bool_day}.\n"
            f"\nWeather: There will be {conditions}, {high} and {low}.\n"
            f"\nSports information: \n{table_data}\n"
            f"\nHave a great day!\n\n"
            f"jospar-bot")
    email = (f"{greeting}\n\n"
             f"{text}")
    return email


def compose_email():
    subject = "Daily Briefing from jospar-bot"  # subject of email
    text = format_email()  # text of email
    recipient = "joseph0701p@gmail.com"  # recipient email
    sender = "code_burner_01@outlook.com"  # sender email
    app_password = "wgnwooooexufvgfi"  # one-time app password
    send_email(subject, text, recipient, sender, app_password)


compose_email()
