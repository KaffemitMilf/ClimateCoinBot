from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


#eos:EOS
#Ripple:XRP
#Cardano:ADA
#Iota:MIOTA
#Nano:Nano
def getPrice(coin: str):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'convert': 'USD',
        "symbol": coin
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': "xxx",
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return round(data["data"][coin]["quote"]["USD"]["price"],2)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
