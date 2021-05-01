import matplotlib.pyplot as plt
from CryptoPrice import getPrice
import pymongo

def weekVisualization():
    cluster = pymongo.MongoClient(
        'mongodb+srv://Fynn:MSJIS0b9WfKtWqq2@cluster0.jqir5.mongodb.net/Coins?retryWrites=true&w=majority')
    db = cluster['Coins']
    ada_db = db['ada']
    eos_db = db['eos']
    miota_db = db['miota']
    nano_db = db['nano']
    xrp_db = db['xrp']

    ada_list = []
    eos_list = []
    miota_list = []
    nano_list = []
    xrp_list = []

    ada_datas = ada_db.find().sort('_id', -1).limit(7)
    for i in ada_datas:
        ada_list.append(i['value'])
    ada_list.reverse()

    eos_datas = eos_db.find().sort('_id', -1).limit(7)
    for i in eos_datas:
        eos_list.append(i['value'])
    eos_list.reverse()

    miota_datas = miota_db.find().sort('_id', -1).limit(7)
    for i in miota_datas:
        miota_list.append(i['value'])
    miota_list.reverse()

    nano_datas = nano_db.find().sort('_id', -1).limit(7)
    for i in nano_datas:
        nano_list.append(i['value'])
    nano_list.reverse()

    xrp_datas = xrp_db.find().sort('_id', -1).limit(7)
    for i in xrp_datas:
        xrp_list.append(i['value'])
    xrp_list.reverse()

    # Days
    x = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]

    # Data
    axe_1 = ada_list  # [5, 1, 2, 3, 4, -5, 6]
    axe_2 = eos_list  # [2, 4, -1, 7, 8, 9, 10]
    axe_3 = miota_list  # [1, 3, 4, 5, 6, 8, 2]
    axe_4 = nano_list  # [1, 9, 6, 4, 8, 2, 7]
    axe_5 = xrp_list  # [8, 2, 9, 4, 6, 2, 8]

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

    # naming axis
    plt.xlabel("Days", fontweight="bold", color="#F5F8FA")
    plt.ylabel("", fontweight="bold", color="#F5F8FA")

    # giving title, save as png
    plt.title("The prices in the last 7 days", color="#F5F8FA")

    # change color of fond in legend
    l = plt.legend(facecolor="#14171A", frameon=False)
    for text in l.get_texts():
        text.set_color("#F5F8FA")
    plt.savefig("grow.png", bbox_inches="tight", dpi=300)

def monthVisualization():
    cluster = pymongo.MongoClient(
        'mongodb+srv://Fynn:MSJIS0b9WfKtWqq2@cluster0.jqir5.mongodb.net/Coins?retryWrites=true&w=majority')
    db = cluster['Coins']
    ada_db = db['ada']
    eos_db = db['eos']
    miota_db = db['miota']
    nano_db = db['nano']
    xrp_db = db['xrp']

    ada_list = []
    eos_list = []
    miota_list = []
    nano_list = []
    xrp_list = []

    ada_datas = ada_db.find().sort('_id', -1).limit(30)
    for i in ada_datas:
        ada_list.append(i['value'])
    ada_list.reverse()

    eos_datas = eos_db.find().sort('_id', -1).limit(30)
    for i in eos_datas:
        eos_list.append(i['value'])
    eos_list.reverse()

    miota_datas = miota_db.find().sort('_id', -1).limit(30)
    for i in miota_datas:
        miota_list.append(i['value'])
    miota_list.reverse()

    nano_datas = nano_db.find().sort('_id', -1).limit(30)
    for i in nano_datas:
        nano_list.append(i['value'])
    nano_list.reverse()

    xrp_datas = xrp_db.find().sort('_id', -1).limit(30)
    for i in xrp_datas:
        xrp_list.append(i['value'])
    xrp_list.reverse()

    # Days
    x = []
    for i in range(0,30):
        x.append(i)


    # Data
    axe_1 = ada_list  # [5, 1, 2, 3, 4, -5, 6]
    axe_2 = eos_list  # [2, 4, -1, 7, 8, 9, 10]
    axe_3 = miota_list  # [1, 3, 4, 5, 6, 8, 2]
    axe_4 = nano_list  # [1, 9, 6, 4, 8, 2, 7]
    axe_5 = xrp_list  # [8, 2, 9, 4, 6, 2, 8]

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

    # naming axis
    plt.xlabel("Days", fontweight="bold", color="#F5F8FA")
    plt.ylabel("Price", fontweight="bold", color="#F5F8FA")

    # giving title, save as png
    plt.title("The prices in the last 30 Days", color="#F5F8FA")

    # change color of fond in legend
    l = plt.legend(facecolor="#14171A", frameon=False)
    for text in l.get_texts():
        text.set_color("#F5F8FA")
    plt.savefig("grow.png", bbox_inches="tight", dpi=300)


