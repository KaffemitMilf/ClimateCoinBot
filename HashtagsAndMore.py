from datetime import datetime
import pytz

tz_DE = pytz.timezone('Europe/Berlin')
datetime_DE = datetime.now(tz_DE)
time = datetime_DE.strftime("%H:%M:%S")

def timeH():
    datetime_DE = datetime.now(tz_DE)
    return int(datetime_DE.strftime("%H"))

def randomTextBegin(): #8,14,18,22
    #gm
    if timeH() <= 8:
        readME = open("ListHellogm.txt", "r").read()
        output = readME.split(";")
        for i in range(0, len(output)):
            output[i] = output[i].replace("\n","")
    #gn
    elif timeH() >= 20:
        readME = open("Listgn.txt", "r").read()
        output = readME.split(";")
        for i in range(0, len(output)):
            output[i] = output[i].replace("\n","")
    #normalDay
    else:
        readME = open("ListHelloNormal.txt", "r").read()
        output = readME.split(";")
        for i in range(0, len(output)):
            output[i] = output[i].replace("\n","")

    return output

def listEnd():
    #gm
    if timeH() <= 8:
        readME = open("ListEndGm.txt", "r").read()
        list = readME.split(";")
        for i in range(0, len(list)):
            list[i] = list[i].replace("\n", "")
    #gn
    if timeH() >= 22:
        readME = open("listEndGn.txt", "r").read()
        list = readME.split(";")
        for i in range(0, len(list)):
            list[i] = list[i].replace("\n", "")

    #normal
    else:
            readME = open("listEndNormal.txt", "r").read()
            list = readME.split(";")
            for i in range(0,len(list)):
                list[i] = list[i].replace("\n","")
    return list

def listhashtag():
    readME = open("Hashtags.txt", "r").read()
    list = readME.split(",")
    for i in range(0,len(list)):
        list[i] = "#"+list[i]
    return list
