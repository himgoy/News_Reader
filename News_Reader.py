import requests
import json
import time
from win32com.client import Dispatch
import inflect
# Get your API Key from this Website
# https://newsapi.ai/

NewsApiKey = input("Enter your API Key Here : ")

def speak(string):
    if string == None:
        string = "No Data"
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(string)


def print_country_dictionary():
    i = 1
    for key in country_dictonary:
        if i <= 9:
            print(f"{i}.  {key}")
        else:
            print(f"{i}. {key}")
        i += 1


def input_using_name():
    country_name = input("Name of the country Whose news you would like to Read : ")
    while True:
        short_form = country_dictonary.get(country_name)
        if short_form is None:
            print("Write a valid Country Name")
            country_name = input("Name the country Whose news you would like to Read : ")
            continue

        else:
            speak(f"You have chosen {country_name}")
            return short_form


def input_using_number():
    while True:
        try:
            country_number = int(input("Number of the country Whose news you would like to Read : "))
            if len(country_list) >= country_number >= 1:
                country_name = country_list[country_number - 1]
                speak(f"You have chosen {country_name}")
                break
            else:
                print(f"Give a Valid Country Number between 1 and {len(country_list)}")

        except ValueError:
            print("ERROR!, Give a Valid Country Number")
            continue
    short_form = country_dictonary.get(country_name)
    return short_form


def news_bot():
    p = inflect.engine()  # For First, Second, Third ...
    url = "http://newsapi.org/v2/top-headlines?country=" + short_form + "&apiKey=" + NewsApiKey
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(f"URL = {url}")
    articles_from_site = news_dict["articles"]
    i = 1
    # speak("This is Himanshu's News Agency, which is ready to serve you.\n"
    #       "I am himgoy the bot, who will be reading for you. You can also follow me by reading the console.")
    speak("The Headlines for today are as Follows")
    for article in articles_from_site:
        speak(p.ordinal(i))
        print(f"\n{article['url']}\nTitle : {article['title']}")
        speak(article['title'])
        time.sleep(0.2)
        print(f"Description : {article['description']}")
        speak(article['description'])
        i += 1
    speak("Thanks for using himgoy bot to fulfil your news needs")


if __name__ == '__main__':
    country_dictonary = {
        "Argentina": "ar",
        "Australia": "au",
        "Austria": "at",
        "Belgium": "be",
        "Brazil": "br",
        "Bulgaria": "bg",
        "Canada": "ca",
        "China": "cn",
        "Colombia": "co",
        "Cuba": "cu",
        "Czech Republic": "",
        "Egypt": "eg",
        "France": "fr",
        "Germany": "de",
        "Greece": "gr",
        "Hong Kong": "hk",
        "Hungary": "hn",
        "India": "in",
        "Indonesia": "id",
        "Ireland": "ie",
        "Israel": "il",
        "Italy": "it",
        "Japan": "jp",
        "Latvia": "lv",
        "Lithuania": "lt",
        "Malaysia": "my",
        "Mexico": "mx",
        "Morocco": "ma",
        "Netherlands": "nl",
        "New Zealand": "nz",
        "Nigeria": "ng",
        "Norway": "no",
        "Philippines": "ph",
        "Poland": "pl",
        "Portugal": "pt",
        "Romania": "ro",
        "Russia": "ru",
        "Saudi Arabia": "sa",
        "Serbia": "rs",
        "Singapore": "sg",
        "Slovakia": "sk",
        "Slovenia": "si",
        "South Africa": "za",
        "South Korea": "kr",
        "Sweden": "se",
        "Switzerland": "ch",
        "Taiwan": "tw",
        "Thailand": "th",
        "Turkey": "tr",
        "UAE": "ae",
        "Ukraine": "ua",
        "United Kingdom": "gb",
        "United States": "us",
        "Venezuela": "ve",
    }
    country_list = ['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Bulgaria', 'Canada', 'China', 'Colombia',
                    'Cuba', 'Czech Republic', 'Egypt', 'France', 'Germany', 'Greece', 'Hong Kong', 'Hungary', 'India',
                    'Indonesia', 'Ireland', 'Israel', 'Italy', 'Japan', 'Latvia', 'Lithuania', 'Malaysia', 'Mexico',
                    'Morocco', 'Netherlands', 'New Zealand', 'Nigeria', 'Norway', 'Philippines', 'Poland', 'Portugal',
                    'Romania', 'Russia', 'Saudi Arabia', 'Serbia', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa',
                    'South Korea', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Turkey', 'UAE', 'Ukraine',
                    'United Kingdom', 'United States', 'Venezuela']

    print_country_dictionary()

    # ********* Choose any one of the following Function *********
    # short_form = input_using_name()
    short_form = input_using_number()

    news_bot()
    time.sleep(2)
