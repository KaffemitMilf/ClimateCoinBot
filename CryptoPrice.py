from requests import Session
import json


def get_price(coin: str):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    parameters = {
        "symbol": coin,
        "convert": "USD"
    }
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "1aaed42c-9dca-4f39-82dd-06c0e5171446"
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters).text

    # convert json to python and access the dict
    return round(json.loads(response)["data"][str(coin)]["quote"]["USD"]["price"], 2)



