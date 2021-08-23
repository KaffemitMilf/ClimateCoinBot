from bs4 import BeautifulSoup
import requests

def getPrice(coin) -> str:
    coin = coin.lower()
    names = {
        "eth" : "ethereum",
        "btc" : "bitcoin",
        "ada" : "cardano",
        "xmr" : "monero",
        "miota" : "iota"
    }
    if coin in names:
        coin = names[coin]
    price = "0"
    while price == "0":
        #getting whole website as text
        source = requests.get(f"https://coinmarketcap.com/currencies/{coin}/")
        source = source.text
        soup = BeautifulSoup(source, "lxml")
        #find div with class x
        information = soup.find("div", class_="priceValue___11gHJ")
        #seperate text from html, remove $ sign
        price =information.text[1:].replace(",","")
    return price



