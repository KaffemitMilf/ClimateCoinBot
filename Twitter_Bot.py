from time import sleep
from twitter import *
from CryptoPrice import get_price
from HashtagsAndMore import text_begin, random_hashtag, clear_greetings
import schedule
import DataVisualization as DataV
import pymongo
from DataVisualization import week_visualization
from os import getenv

# twitter api
t = Twitter(auth=OAuth(
    token=getenv("twitter_token"),
    token_secret=getenv("token_secret"),
    consumer_key=getenv("twitter_consumer_key"),
    consumer_secret=getenv("twitter_consumer_secrets")))

# list of taken greetings
takenGreetings = []
takenhashtags = []


# twitter api
def text_of_tweet():
    cluster = pymongo.MongoClient(getenv("pymongoClient"))
    db = cluster['Coins']
    ada_db = db['ada']
    eos_db = db['eos']
    miota_db = db['miota']
    nano_db = db['nano']
    xrp_db = db['xrp']
    xmr_db = db["xmr"]
    eth_db = db["eth"]

    btc = get_price("BTC")
    eth = get_price("ETH")
    xrp = get_price("XRP")
    eos = get_price("EOS")
    ada = get_price("ADA")
    iota = get_price("IOTA")
    nano = get_price("NANO")
    xmr = get_price("XMR")

    ada_db.insert_one({"_id": list(ada_db.find().sort('_id', -1).limit(1))[0]["_id"] + 1, "value": ada})
    eos_db.insert_one({"_id": list(eos_db.find().sort('_id', -1).limit(1))[0]["_id"] + 1, "value": eos})
    miota_db.insert_one({"_id": list(miota_db.find().sort('_id', -1).limit(1))[0]["_id"] + 1, "value": iota})
    nano_db.insert_one({"_id": list(nano_db.find().sort('_id', -1).limit(1))[0]["_id"] + 1, "value": nano})
    xrp_db.insert_one({"_id": list(xrp_db.find().sort('_id', -1).limit(1))[0]["_id"] + 1, "value": xrp})
    xmr_db.insert_one({"_id": list(xmr_db.find().sort('_id', -1).limit(1))[0]["_id"] + 1, "value": xmr})
    eth_db.insert_one({"_id": list(eth_db.find().sort('_id', -1).limit(1))[0]["_id"] + 1, "value": eth})

    text = f"""{text_begin()}
#Bitcoin as reference
BTC: {btc}$
ETH: {eth}$
XRP: {xrp}$
XMR: {xmr}$
EOS: {eos}$
ADA: {ada}$
IOTA: {iota}$
NANO: {nano}$\n
{random_hashtag()}"""

    return text


def tweet_crypto():
    text = text_of_tweet()
    t.statuses.update(status=text)


def tweet_picture_week():
    week_visualization()
    with open("grow.png", "rb") as imagefile:
        imagedata = imagefile.read()
    t_upload = Twitter(domain='upload.twitter.com',
                       auth=OAuth(
                           token=getenv("twitter_token"),
                           token_secret=getenv("token_secret"),
                           consumer_key=getenv("twitter_consumer_key"),
                           consumer_secret=getenv("twitter_consumer_secrets")))
    id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
    t.statuses.update(status=DataV.text_week(), media_ids=",".join([id_img1]))


schedule.every().day.at("12:00").do(tweet_crypto)
schedule.every().sunday.at("14:00").do(tweet_picture_week)
schedule.every().monday.do(clear_greetings)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        sleep(1)
