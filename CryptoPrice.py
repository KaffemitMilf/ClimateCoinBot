from requests import Session
import json
from os import getenv

def get_price(coin: str):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        "symbol": coin,
        "convert": "USD"
    }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": getenv("api-key")
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters).text

    # convert json to python and access the dict
    return round(json.loads(response)["data"][str(coin)]["quote"]["USD"]["price"], 2)



