import time
from twitter import *
from CryptoPrice import getPrice
import os
from HashtagsAndMore import randomTextBegin, listEnd, listhashtag
import schedule
import matplotlib.pyplot as plt


# twitter api
t = Twitter(auth=OAuth(
    token=os.getenv("TWITTER_TOKEN"),
    token_secret=os.getenv("TOKEN_SECRET"),
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET")))

# tweet current twitter-price + extra-text


def TextofTweet():

    text =f"""{TextBegin()}
Here is the current Crypto value:  
#Bitcoin and #Ethereum as reference\n
BITCOIN: {getPrice("BTC")}$
ETHEREUM {getPrice("ETH")}$
RIPPLE: {getPrice("XRP")}$
EOS: {getPrice("EOS")}$
CARDANO: {getPrice("ADA")}$
IOTA: {getPrice("MIOTA")}$
NANO: {getPrice("NANO")}$\n
{TextEnd()}}\n{hashtag()}"""

    return text


# random twitter-text
takenGreetings = []
takenGreetingsEnd = []
takenhashtags = []


def TextBegin():

    randomnum = randomTextBegin()
    while randomnum in takenGreetings:
        randomnum = randomTextBegin()

    takenGreetings.append(randomnum)
    return randomnum


def TextEnd():
    randomnum = listEnd()
    while randomnum in takenGreetingsEnd:
        randomnum = listEnd()

    takenGreetingsEnd.append(randomnum)
    return randomnum


def hashtag():
    randomnum = listhashtag()
    while randomnum in takenGreetings:
        randomnum = listhashtag()

    takenhashtags.append(randomnum)
    return randomnum


def tweetCrypto():
    var = TextofTweet()
    if len(var) < 280:
        print("ClimateCoin > The Tweet to Post is over 280 Charackters, so don't posting that!")
        return
    t.statuses.update(status=var)


def clearGreetings():
    takenGreetings, takenGreetings, takenhashtags = []


schedule.every().day.at("08:00").do(tweetCrypto)  # 8
schedule.every().day.at("14:00").do(tweetCrypto)  # 14
schedule.every().day.at("18:00").do(tweetCrypto)  # 18
schedule.every().day.at("22:00").do(tweetCrypto)  # 22
schedule.every().monday.do(clearGreetings)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(30)
