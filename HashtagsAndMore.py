from datetime import datetime
import pytz
import random

tz_DE = pytz.timezone('Europe/Berlin')
datetime_DE = datetime.now(tz_DE)
time = datetime_DE.strftime("%H:%M:%S")


def timeH() -> int:
    datetime_DE = datetime.now(tz_DE)
    return int(datetime_DE.strftime("%H"))


hashtags = ['Crypto', 'Cryptocurrency', 'Etherum', 'Blockchain', 'Token', 'BTC', 'ETH', 'ETC', 'BNB', 'ZEC', 'EOS', 'ADA', 'XRP', 'MIOTA', 'DASH', 'DODGE', 'NANO', 'CARDANO', 'LTC', 'IOTA', 'Priceupdate', 'Altcoins', 'Innovation',
            'Climate', 'Climatechange', 'CO2', 'Energy', 'Earth', 'ClimateCrisis', 'Mining', 'Cryptomining', 'Technology', 'Cryptonews', 'Cryptocurrencies']

list_end_gm = ['Warning! Try to have a busy morning!',
               "Now it's your turn cryptocurrency to earn!",
               "Make everything you can till 12 pm!"]

list_end_gn = ["Now it's time for sleep, hope just tommorow crypto will be cheap!",
               "So have good dreams about wallet full of crypto-things!;Good night :)",
               "Dream about crypto!"]

list_end_normal = ["Hope you will be doing great!;Don't forget about mining today!",
                   "Take an advice: not to forget to check crypto price!",
                   "Just work and don't think that your crypto will drop!",
                   "Plant some trees! (link in bio);The future will be green!"]

list_hello_gm = ["Moin! Moin!",
                 "Wakey, wakey, mining is waiting!",
                 "Be active and make your day productive!",
                 "Good morning! Rise just like bitcoin price!",
                 "Good morning!;Hello there! Wake and take some crypto payments!",
                 "Good morning, investor! Make this day better!",
                 "Rise and shine! Don't forget to mine!",
                 "Rise and shine!"]

list_hello_gn = ["Good evening, Mr. Graham Wu!",
                 "Did you -Syu today?",
                 "Nice that you found your way into our little dark room together!",
                 "Day comes to an end, don't forget your extra divident!",
                 "How did you spend your day?",
                 "Hope you had a great experience, mate!"]

list_hello_normal = ["Tweet goes yeet!",
                     "Crypto!, Crypto!, Crypto!",
                     "Grab a Weisswurst and sit you next to me!",
                     "Nice to meet you here :)",
                     "I hope your day is nice!",
                     "Hey, beast! Make your earnings be increased!",
                     "Today will be the best! Your crypto wallet will worry about the rest!",
                     "Hoping your day will be bright like Bitcoin price till 2009"]


def randomTextBegin() -> str:  # 8,14,18,22
    # gm
    if timeH() <= 8:
        return random.choice(list_hello_gm)
    # gn
    elif timeH() >= 20:
        return random.choice(list_hello_gn)
    # normalDay
    else:
        return random.choice(list_hello_normal)


def listEnd() -> str:
    # gm
    if timeH() <= 8:
        return random.choice(list_end_gm)
    # gn
    if timeH() >= 22:
        return random.choice(list_end_gn)
    # normal
    else:
        return random.choice(list_end_normal)


def listhashtag() -> str:
    return random.choice(hashtags)
