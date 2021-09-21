import matplotlib.pyplot as plt
import pymongo
from HashtagsAndMore import text_begin, random_hashtag
from os import getenv


def get_growth(coin, days):
    cluster = pymongo.MongoClient(getenv("pymongoClient"))
    db = cluster['Coins']
    coin_db = db[coin]
    coin_list = []
    coin_list_vs = []

    coin_data = coin_db.find().sort('_id', -1).limit(int(days) + 1)
    for i in coin_data:
        coin_list.append(float(i['value'].replace(',', "")))
    coin_list.reverse()
    x = 0
    y = 1
    # calculate growth
    for i in range(0, len(coin_list) - 1):
        k = coin_list[x] - coin_list[y]
        k = (k / coin_list[y]) * 100
        coin_list_vs.append(k)
        x += 1
        y += 1

    return coin_list_vs


def week_visualization():
    # get lists with growth in %
    axe_1 = get_growth("ada", 7)
    axe_2 = get_growth("eos", 7)
    axe_3 = get_growth("miota", 7)
    axe_4 = get_growth("nano", 7)
    axe_5 = get_growth("xrp", 7)
    axe_7 = get_growth("xmr", 7)
    axe_6 = get_growth("eth", 7)

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
    l = plt.legend(loc='upper left', facecolor="#14171A", frameon=False)
    for text in l.get_texts():
        text.set_color("#F5F8FA")
    plt.savefig("grow.png", bbox_inches="tight", dpi=300)


def get_growth_overall(coin, days):
    cluster = pymongo.MongoClient(getenv("pymongoClient"))
    db = cluster['Coins']

    coin_db = db[coin]
    coin_list = []

    coin_data = coin_db.find().sort('_id', -1).limit(int(days) + 1)
    for i in coin_data:
        coin_list.append(float(i['value']))
    coin_list.reverse()
    k = coin_list[0] - coin_list[len(coin_list) - 1]
    k = round((k / coin_list[len(coin_list) - 1]) * 100, 2)
    if k > 0:
        return "+" + str(k)
    else:
        return str(k)


def text_week():
    text = f"""{text_begin()}
ETH: {get_growth_overall("eth", 7)}%
XRP: {get_growth_overall("xrp", 7)}%
XMR: {get_growth_overall("xmr", 7)}%
EOS: {get_growth_overall("eos", 7)}%
ADA: {get_growth_overall("ada", 7)}%
IOTA: {get_growth_overall("miota", 7)}%
NANO: {get_growth_overall("nano", 7)}% \n
{random_hashtag()}
"""
    return text
