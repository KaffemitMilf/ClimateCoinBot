from time import sleep
from twitter import *
from CryptoPrice import getPrice
import os
from HashtagsAndMore import randomTextBegin, listhashtag
import schedule
import matplotlib.pyplot as plt
import DataVisualization as DV
import pytz
from datetime import *
import pymongo

# twitter api
t= Twitter(auth=OAuth
    (token="1366841945746735105-CxidSpZWVEs6teNkvQ2LRnUyrdoE8R", #.getenv("TWITTER_TOKEN"),
    token_secret="qbbSne1uGG5urOQxWUSUpLCW8J7JEnIYj68RX4PCGqHXS", #os.getenv("TOKEN_SECRET"),
    consumer_key= "Q68p95z93b8ZtYbcC0nQMHold", #os.getenv(CONSUMER_KEY),
    consumer_secret="uZJx4SA4919PKgj2IAC1pMHhsNkxTJWhs7NCFGj1gJFNL8sj4A")) #os.getenv("CONSUMER_SECRET)


tz_DE = pytz.timezone('Europe/Berlin')
datetime_DE = datetime.now(tz_DE)

time = datetime_DE.strftime("%H:%M:%S")
 #define later needed variables


#list of taken greetings
takenGreetings = []
takenGreetingsEnd = []
takenhashtags = []
#twitter api

def TextofTweet():

    cluster = pymongo.MongoClient(
    "mongodb+srv://Fynn:MSJIS0b9WfKtWqq2@cluster0.jqir5.mongodb.net/Coins?retryWrites=true&w=majority")
    db = cluster['Coins']
    ada_db = db['ada']
    eos_db = db['eos']
    miota_db = db['miota']
    nano_db = db['nano']
    xrp_db = db['xrp']
    xmr_db = db["xmr"]

    BTC = getPrice("BTC")
    ETH = getPrice("ETH")
    XRP = getPrice("XRP")
    EOS = getPrice("EOS")
    ADA = getPrice("ADA")
    IOTA =getPrice("IOTA")
    NANO =getPrice("NANO")
    XMR = getPrice("XMR")

    ada_db.insertOne({'_id': (ada_db.find().sort("_id", -1).limit(1) + 1), 'value': ADA})
    eos_db.insertOne({'_id': (eos_db.find().sort("_id",-1).limit(1) + 1), 'value': EOS})
    miota_db.insertOne({'_id': (miota_db.find().sort("_id",-1).limit(1) + 1), 'value': IOTA})
    nano_db.insertOne({'_id': (nano_db.find().sort("_id",-1).limit(1) + 1), 'value': NANO})
    xrp_db.insertOne({'_id': (xrp_db.find().sort("_id",-1).limit(1) + 1), 'value': XRP})
    xmr_db.insertOne({'_id': (xmr_db.find().sort("_id", -1).limit(1) + 1), 'value': XMR})


    text = f"""{TextBegin()}

  
#Bitcoin as reference\n
BTC: {getPrice("BTC")}$
ETH: {getPrice("ETH")}$
XRP: {getPrice("XRP")}$
XMR: {getPrice("XMR")}
EOS: {getPrice("EOS")}$
ADA: {getPrice("ADA")}$
IOTA: {getPrice("MIOTA")}$
NANO: {getPrice("NANO")}$\n
{hashtag()}"""


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

def hashtag():
    randomnum = listhashtag()
    while randomnum in takenGreetings:
        randomnum = listhashtag()

    takenhashtags.append(randomnum)
    return randomnum


def tweetCrypto():
    var = TextofTweet()
    if len(var) > 280:
        print("ClimateCoin > The Tweet to Post is over 280 Characters, so don't posting that!")
        return
    t.statuses.update(status=var)


def clearGreetings():
    takenGreetings, takenhashtags = []

def tweet_pictureWeek():
    DV.weekVisualization()
    with open("grow.png", "rb") as imagefile:
        imagedata = imagefile.read()
    t_upload = Twitter(domain='upload.twitter.com',
                       auth=OAuth(token="1366841945746735105-CxidSpZWVEs6teNkvQ2LRnUyrdoE8R", #.getenv("TWITTER_TOKEN")
                        token_secret="qbbSne1uGG5urOQxWUSUpLCW8J7JEnIYj68RX4PCGqHXS", #os.getenv("TOKEN_SECRET")
                        consumer_key= "Q68p95z93b8ZtYbcC0nQMHold", #os.getenv(CONSUMER_KEY)
                        consumer_secret="uZJx4SA4919PKgj2IAC1pMHhsNkxTJWhs7NCFGj1gJFNL8sj4A")) #os.getenv("CONSUMER_SECRET))
    id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
    t.statuses.update(status="PTT ★", media_ids=",".join([id_img1]))

def tweet_pictureMonth():
    DV.monthVisualization()
    with open("grow.png", "rb") as imagefile:
        imagedata = imagefile.read()
    t_upload = Twitter(domain='upload.twitter.com',
                       auth=OAuth(token="1366841945746735105-CxidSpZWVEs6teNkvQ2LRnUyrdoE8R", #.getenv("TWITTER_TOKEN")
                        token_secret="qbbSne1uGG5urOQxWUSUpLCW8J7JEnIYj68RX4PCGqHXS", #os.getenv("TOKEN_SECRET")
                        consumer_key= "Q68p95z93b8ZtYbcC0nQMHold", #os.getenv(CONSUMER_KEY)
                        consumer_secret="uZJx4SA4919PKgj2IAC1pMHhsNkxTJWhs7NCFGj1gJFNL8sj4A")) #os.getenv("CONSUMER_SECRET))
    id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
    t.statuses.update(status="PTT ★", media_ids=",".join([id_img1]))

schedule.every().monday.at("12:00").do(tweetCrypto)
schedule.every().tuesday.at("12:00").do(tweetCrypto)
schedule.every().wednesday.at("12:00").do(tweetCrypto)
schedule.every().thursday.at("12:00").do(tweetCrypto)
schedule.every().friday.at("11:35").do(tweetCrypto)
schedule.every().saturday.at("12:00").do(tweetCrypto)
schedule.every().sunday.at("12:00").do(tweet_pictureWeek)
schedule.every().monday.do(clearGreetings)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        sleep(30)

