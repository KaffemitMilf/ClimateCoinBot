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
<<<<<<< Updated upstream

    text = TextBegin()+f"""
=======
    if int(datetime_DE.strftime("%H")) == 12:
        cluster = MongoClient(
        '')
        db = cluster['Coins']
        ada_db = db['ada']
        eos_db = db['eos']
        miota_db = db['miota']
        nano_db = db['nano']
        xrp_db = db['xrp']

        BTC = getPrice("BTC")
        ETH = getPrice("ETH")
        XRP = getPrice("XRP")
        EOS = getPrice("EOS")
        ADA = getPrice("ADA")
        IOTA = getPrice("MIOTA")
        NANO = getPrice("NANO")

        ada_db.insertOne({'_id': (ada_db.find({}).sort({_id:-1}).limit(1) + 1), 'value': ADA})
        eos_db.insertOne({'_id': (eos_db.find({}).sort({_id:-1}).limit(1) + 1), 'value': EOS})
        miota_db.insertOne({'_id': (miota_db.find({}).sort({_id:-1}).limit(1) + 1), 'value': IOTA})
        nano_db.insertOne({'_id': (nano_db.find({}).sort({_id:-1}).limit(1) + 1), 'value': NANO})
        xrp_db.insertOne({'_id': (xrp_db.find({}).sort({_id:-1}).limit(1) + 1), 'value': XRP})



        text = f"""{TextBegin()}
>>>>>>> Stashed changes
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





<<<<<<< Updated upstream
=======
def clearGreetings():
    takenGreetings, takenGreetings, takenhashtags = []
 

def tweet_pictureWeeK():
    DV.weekVisualization()
    with open("grow.png", "rb") as imagefile:
        imagedata = imagefile.read()
    t_upload = Twitter(domain='upload.twitter.com',
                       auth=OAuth(token=os.getenv("TWITTER_TOKEN"),
                                  token_secret=os.getenv("TOKEN_SECRET"),
                                  consumer_key=os.getenv("CONSUMER_KEY"),
                                  consumer_secret=os.getenv("CONSUMER_SECRET")))
    id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
    t.statuses.update(status="PTT ★", media_ids=",".join([id_img1]))

def tweet_pictureMonth():
    DV.monthVisualization()
    with open("grow.png", "rb") as imagefile:
        imagedata = imagefile.read()
    t_upload = Twitter(domain='upload.twitter.com',
                       auth=OAuth(token=os.getenv("TWITTER_TOKEN"),
                                  token_secret=os.getenv("TOKEN_SECRET"),
                                  consumer_key=os.getenv("CONSUMER_KEY"),
                                  consumer_secret=os.getenv("CONSUMER_SECRET")))
    id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
    t.statuses.update(status="PTT ★", media_ids=",".join([id_img1]))

schedule.every().monday.at("12:00").do(tweetCrypto)
schedule.every().tuesday.at("12:00").do(tweetCrypto)
schedule.every().wednesday.at("12:00").do(tweetCrypto)
schedule.every().thursday.at("12:00").do(tweetCrypto)
schedule.every().friday.at("12:00").do(tweetCrypto)
schedule.every().saturday.at("12:00").do(tweetCrypto)
schedule.every().sunday.at("12:00").do(tweet_picture)
schedule.every(4).sunday.at("18:00").do(tweet_pictureMonth)
schedule.every().monday.do(clearGreetings)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(30)
>>>>>>> Stashed changes
