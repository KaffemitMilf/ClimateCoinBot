import time
from twitter import *
import random
from CryptoPrice import getPrice
import os
import smtplib
import datetime
from datetime import datetime
import pytz
import os
from HashtagsAndMore import randomTextBegin, listEnd, listhashtag
import schedule
tz_DE = pytz.timezone('Europe/Berlin')
datetime_DE = datetime.now(tz_DE)
#time = datetime_DE.strftime("%H:%M:%S")
 #define later needed variables
rnumber = random.randint(1,100)
def timeMin():
    datetime_DE = datetime.now(tz_DE)
    return int(datetime_DE.strftime("%M"))
def timeH():
    datetime_DE = datetime.now(tz_DE)
    return int(datetime_DE.strftime("%H"))

#list of taken greetings
takenGreetings = []
takenGreetingsEnd = []
takenhashtags = []
#twitter api
t = Twitter(auth=OAuth(
token = os.getenv("TWITTER_TOKEN"),
token_secret = os.getenv("TOKEN_SECRET"),
consumer_key = os.getenv("CONSUMER_KEY"),
consumer_secret= os.getenv("CONSUMER_SECRET")))

#tweet current twitter-price + extra-text
def TextofTweet():

    text = TextBegin()+f"""
Here is the current Crypto value:  
#Bitcoin and #Ethereum as reference\n
BITCOIN: {getPrice("BTC")}$
ETHEREUM {getPrice("ETH")}$
RIPPLE: {getPrice("XRP")}$
EOS: {getPrice("EOS")}$
CARDANO: {getPrice("ADA")}$
IOTA: {getPrice("MIOTA")}$
NANO: {getPrice("NANO")}$\n
""" +TextEnd() + "\n" +hashtag()

    return text

#random twitter-text
def TextBegin():

        randomnum = random.choice(randomTextBegin())
        while randomnum in takenGreetings:
            randomnum = random.choice(randomTextBegin())

        takenGreetings.append(randomnum)
        return randomnum


def TextEnd():
        randomnum = random.choice(listEnd())
        while randomnum in takenGreetingsEnd:
            randomnum = random.choice(listEnd())
        takenGreetingsEnd.append(randomnum)
        return randomnum

def hashtag():
    randomnum = random.choice(listhashtag())
    while randomnum in takenGreetings:
        randomnum = random.choice(listhashtag())

    takenhashtags.append(randomnum)
    return randomnum

def tweetCrypto():
    var = TextofTweet()
    while len(var) > 280:
        time.sleep(60)
        var = TextofTweet()
    t.statuses.update(status= var)
def usedGreetings():
    takenGreetings, takenGreetings, takenhashtags = []

schedule.every().day.at("08:00").do(tweetCrypto) #8
schedule.every().day.at("14:00").do(tweetCrypto) #14
schedule.every().day.at("18:00").do(tweetCrypto) #18
schedule.every().day.at("22:00").do(tweetCrypto) #22
schedule.every().monday.do(usedGreetings)


while True:
    schedule.run_pending()
    time.sleep(10)





