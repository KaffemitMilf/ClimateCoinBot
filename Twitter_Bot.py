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

# twitter api
t= Twitter(auth=OAuth
    (token="xxx", #.getenv("TWITTER_TOKEN"),
    token_secret="xxx", #os.getenv("TOKEN_SECRET"),
    consumer_key= "xxx", #os.getenv(CONSUMER_KEY),
    consumer_secret="xxx")) #os.getenv("CONSUMER_SECRET)


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

# tweet current twitter-price + extra-text


def TextofTweet():
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

Here is the current Crypto value:  
#Bitcoin and #Ethereum as reference\n
BTC: {getPrice("BTC")}$
ETH: {getPrice("ETH")}$
XRP: {getPrice("XRP")}$
EOS: {getPrice("EOS")}$
ADA: {getPrice("ADA")}$
IOTA: {getPrice("MIOTA")}$
NANO: {getPrice("NANO")}$\n
{TextEnd()}\n{hashtag()}"""


        return text
    else:
        text = f"""{TextBegin()}
Here is the current Crypto value:  
#Bitcoin and #Ethereum as reference\n
BTC: {BTC}$
ETH: {ETH}$
XRP: {XRP}$
EOS: {EOS}$
ADA: {ADA}$
IOTA: {IOTA}$
NANO: {NANO}$\n
{TextEnd()}\n{hashtag()}"""


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
    if len(var) > 280:
        print("ClimateCoin > The Tweet to Post is over 280 Charackters, so don't posting that!")
        return
    t.statuses.update(status=var)


def clearGreetings():
    takenGreetings, takenGreetings, takenhashtags = []
 


def tweet_pictureWeek():
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
schedule.every().sunday.at("18:00").do(tweet_pictureWeek)
#schedule.every(4).sunday.at("18:00").do(tweet_pictureMonth)
schedule.every().monday.do(clearGreetings)


if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(30)