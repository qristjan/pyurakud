import requests


class Coin:
    def __init__(self, coin_id, symbol, name):
        self.coin_id = coin_id
        self.symbol = symbol
        self.name = name

    @classmethod
    def from_json(cls, json):
        return cls(json['id'], json['symbol'], json['name'])

    def __str__(self):
        return self.name


def list_coins():
    r = requests.get('https://api.coingecko.com/api/v3/coins/list')
    return [Coin.from_json(coin_info) for coin_info in r.json()]
