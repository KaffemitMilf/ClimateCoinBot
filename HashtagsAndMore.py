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
            'Climate', 'Climatechange', 'CO2', 'Energy', 'Earth', 'ClimateCrisis', 'Mining', 'Cryptomining', 'Technology', 'Cryptonews',"XMR","Monero"]

list_hello = ["Good evening, Mr. Graham Wu!",
                 "Did you -Syu today?",
                 "Nice that you found your way into our little dark room together!",
                 "How did you spend your day?",
                 "Hope you had a great experience, mate!","The future will be green!","Now it's time for sleep, hope just tommorow crypto will be cheap!",
                 "So have good dreams about wallet full of crypto-things!","Good day :)","Dream about crypto!","Moin! Moin!",
                 "Wakey, wakey, staking is waiting!",
                 "Be active and make your day productive!",
                 "Good morning! Rise just like bitcoin price!",
                 "Good morning!","Hello there! buy some crypto",
                 "Good morning, investor!", "Make this day better!",
                 "Rise and shine!",
                 "Hoping your day will be bright!",
                 "Today will be the best!", "Now it's your turn cryptocurrency to earn!",
                 "Tweet goes yeet!",
                 "Crypto!, Crypto!, Crypto!",
                 "Grab a Weisswurst and sit you next to me!",
                 "Nice to meet you here :)",
                 "Make your earnings be increased!"
                 ]


def randomTextBegin() -> str:  # 8,14,18,22
        return random.choice(list_hello)

def listhashtag() -> str:
    return "#" + random.choice(hashtags)

