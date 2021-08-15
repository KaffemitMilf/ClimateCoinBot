import matplotlib.pyplot as plt
from CryptoPrice import getPrice
import pymongo
from HashtagsAndMore import TextBegin, Hashtag

def getGrowth(coin, days):
    cluster = pymongo.MongoClient(
       "mongodb+srv://Fynn:MSJIS0b9WfKtWqq2@cluster0.jqir5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster['Coins']

    coin_db = db[coin]
    coin_list = []
    coin_list_vs = []

    coin_data = coin_db.find().sort('_id', -1).limit(int(days) + 1)
    for i in coin_data:
        coin_list.append(float(i['value'].replace(',',"")))
    coin_list.reverse()
    x = 0
    y = 1
    # calculate growth
    for i in range(0, len(coin_list) - 1):
        k = coin_list[x] - coin_list[y]
        k = (k/coin_list[y])*100
        coin_list_vs.append(k)
        x += 1
        y += 1

    return coin_list_vs

def weekVisualization():

    #get lists with growth in %
    axe_1 = getGrowth("ada", 7)
    axe_2 = getGrowth("eos",7)
    axe_3 = getGrowth("miota",7)
    axe_4 = getGrowth("nano",7)
    axe_5 = getGrowth("xrp",7)
    axe_7 = getGrowth("xmr",7)
    axe_6 = getGrowth("eth",7)

    # Days
    x = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]

    # add color
    plt.figure(facecolor="#14171A")
    ax = plt.axes()
    ax.set_facecolor("#14171A")
    # outer lines
    ax.spines["bottom"].set_color("#F5F8FA")
    ax.spines["left"].set_color("#F5F8FA")
    ax.spines["top"].set_color("#F5F8FA")
    ax.spines["right"].set_color("#F5F8FA")
    # axes
    ax.tick_params(axis='x', colors="#F5F8FA")
    ax.tick_params(axis='y', colors="#F5F8FA")

    # adding graphs to the digram
    # ,marker = 'o', markerfacecolor = 'r'
    plt.plot(x, axe_5, label="XRP", color="lightblue")
    plt.plot(x, axe_2, label="EOS", color="grey")
    plt.plot(x, axe_1, label="ADA", color="darkgreen")
    plt.plot(x, axe_3, label="MIOTA", color="purple")
    plt.plot(x, axe_4, label="NANO", color="blue")
    plt.plot(x, axe_6, label="ETHEREUM", color="lightgreen")
    plt.plot(x, axe_7, label="MONERO", color="orange")
    # naming axis
    plt.xlabel("Days", fontweight="bold", color="#F5F8FA")
    plt.ylabel("", fontweight="bold", color="#F5F8FA")

    # giving title, save as png
    plt.title("growth of the last 7 days in percent", color="#F5F8FA")

    # change color of fond in legend
    l = plt.legend(loc='upper left',facecolor="#14171A", frameon=False)
    for text in l.get_texts():
        text.set_color("#F5F8FA")
    plt.savefig("grow.png", bbox_inches="tight", dpi=300)

def getGrowthOverall(coin,days):
    cluster = pymongo.MongoClient(
        'mongodb+srv://Fynn:MSJIS0b9WfKtWqq2@cluster0.jqir5.mongodb.net/Coins?retryWrites=true&w=majority')
    db = cluster['Coins']

    coin_db = db[coin]
    coin_list = []
    coin_list_vs = []

    coin_data = coin_db.find().sort('_id', -1).limit(int(days) + 1)
    for i in coin_data:
        coin_list.append(float(i['value']))
    coin_list.reverse()
    k = coin_list[0] - coin_list[len(coin_list)-1]
    k = round((k / coin_list[len(coin_list)-1]) * 100, 2)
    if k > 0:
        return "+" + str(k)
    else:
        return str(k)

def textWeek():
    text = f"""{TextBegin()}
ETH: {getGrowthOverall("eth", 7)}%
XRP: {getGrowthOverall("xrp", 7)}%
XMR: {getGrowthOverall("xmr", 7)}%
EOS: {getGrowthOverall("eos", 7)}%
ADA: {getGrowthOverall("ada", 7)}%
IOTA: {getGrowthOverall("miota", 7)}%
NANO: {getGrowthOverall("nano", 7)}% \n
{Hashtag()}
"""
    return text

