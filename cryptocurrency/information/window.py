import cryptocurrency.information.coingecko_api as ca

coin_info = ca.list_coins()

[print(info) for info in coin_info]
