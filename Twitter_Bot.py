from time import sleep
from twitter import *
from CryptoPrice import getPrice
import os
from HashtagsAndMore import TextBegin, Hashtag, clearGreetings
import schedule
import matplotlib.pyplot as plt
import DataVisualization as DV
import pytz
from datetime import *
import pymongo
from DataVisualization import weekVisualization

# twitter api
t= Twitter(auth=OAuth
    (token="1366841945746735105-pvY0MB64jRsuQag6mrAlN0WZbFBUMA", #.getenv("TWITTER_TOKEN"),
    token_secret="wKajDGxSV9xJjTPCRhc0IZAIpI2gFtulGDyq4GAk8IIMK", #os.getenv("TOKEN_SECRET"),
    consumer_key= "yhr4p9mN4sR1FeyJHEZvJNmVl", #os.getenv(CONSUMER_KEY),
    consumer_secret="L3YcZn30mlcQjMnOeyu65o0NbjQjXpggm1psuu4Pq2b8wen08t")) #os.getenv("CONSUMER_SECRET)


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
    #"mongodb+srv://Fynn:MSJIS0b9WfKtWqq2@cluster0.jqir5.mongodb.net/Coins?retryWrites=true&w=majority")
    "mongodb+srv://Fynn:MSJIS0b9WfKtWqq2@cluster0.jqir5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['Coins']
    ada_db = db['ada']
    eos_db = db['eos']
    miota_db = db['miota']
    nano_db = db['nano']
    xrp_db = db['xrp']
    xmr_db = db["xmr"]
    eth_db = db["eth"]

    BTC = getPrice("BTC")
    ETH = getPrice("ETH")
    XRP = getPrice("XRP")
    EOS = getPrice("EOS")
    ADA = getPrice("ADA")
    IOTA =getPrice("IOTA")
    NANO =getPrice("NANO")
    XMR = getPrice("XMR")

    ada_db.insert_one({"_id":list(ada_db.find().sort('_id',-1).limit(1))[0]["_id"]+1, "value": ADA})
    eos_db.insert_one({"_id":list(eos_db.find().sort('_id',-1).limit(1))[0]["_id"]+1, "value": EOS})
    miota_db.insert_one({"_id":list(miota_db.find().sort('_id',-1).limit(1))[0]["_id"]+1, "value": IOTA})
    nano_db.insert_one({"_id":list(nano_db.find().sort('_id',-1).limit(1))[0]["_id"]+1, "value": NANO})
    xrp_db.insert_one({"_id":list(xrp_db.find().sort('_id',-1).limit(1))[0]["_id"]+1, "value": XRP})
    xmr_db.insert_one({"_id":list(xmr_db.find().sort('_id',-1).limit(1))[0]["_id"]+1, "value": XMR})
    eth_db.insert_one({"_id":list(eth_db.find().sort('_id',-1).limit(1))[0]["_id"]+1, "value": ETH})

    text = f"""{TextBegin()}
#Bitcoin as reference
BTC: {BTC}$
ETH: {ETH}$
XRP: {XRP}$
XMR: {XMR}$
EOS: {EOS}$
ADA: {ADA}$
IOTA: {IOTA}$
NANO: {NANO}$\n
{Hashtag()}"""

    return text

def tweetCrypto():
    var = TextofTweet()
    if len(var) > 280:
        print("ClimateCoin > The Tweet to Post is over 280 characters, so don't posting that!")
    t.statuses.update(status=var)

def tweet_pictureWeek():
    weekVisualization()
    with open("grow.png", "rb") as imagefile:
        imagedata = imagefile.read()
    t_upload = Twitter(domain='upload.twitter.com',
                       auth=OAuth(token="1366841945746735105-pvY0MB64jRsuQag6mrAlN0WZbFBUMA", #.getenv("TWITTER_TOKEN")
                        token_secret="wKajDGxSV9xJjTPCRhc0IZAIpI2gFtulGDyq4GAk8IIMK", #os.getenv("TOKEN_SECRET")
                        consumer_key= "yhr4p9mN4sR1FeyJHEZvJNmVl", #os.getenv(CONSUMER_KEY)
                        consumer_secret="L3YcZn30mlcQjMnOeyu65o0NbjQjXpggm1psuu4Pq2b8wen08t")) #os.getenv("CONSUMER_SECRET))
    id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
    t.statuses.update(status=DV.textWeek(), media_ids=",".join([id_img1]))

schedule.every().day.at("12:00").do(tweetCrypto)
schedule.every().sunday.at("14:00").do(tweet_pictureWeek)
schedule.every().monday.do(clearGreetings)


if __name__ == '__main__':
    while True:
       schedule.run_pending()
       sleep(1)


