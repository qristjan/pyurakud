import requests


class CoinListItem:
    def __init__(self, coin_id, symbol, name):
        self.coin_id = coin_id
        self.symbol = symbol
        self.name = name

    @classmethod
    def from_json(cls, json):
        return cls(json['id'], json['symbol'], json['name'])

    def __str__(self):
        return self.name


class Coin:
    def __init__(self, coin_id, name, price):
        self.coin_id = coin_id
        self.name = name
        self.price = price

    @classmethod
    def from_json(cls, json):
        return cls(json['id'], json['name'], json['market_data']['current_price']['eur'])

    def __str__(self):
        return "{}:\n{} (EUR)".format(self.name, self.price)


def list_coins():
    r = requests.get('https://api.coingecko.com/api/v3/coins/list')
    return [CoinListItem.from_json(coin_info) for coin_info in r.json()]


def get_coin_info(coin):
    r = requests.get('https://api.coingecko.com/api/v3/coins/{}'.format(coin.coin_id))
    return Coin.from_json(r.json())
