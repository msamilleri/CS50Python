import json
import sys
import requests

try:
    buy_count = input()

    if buy_count.isnumeric():
        number_of_coin = int(buy_count)
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json" )
        bitcoin = response.json()
        price_check = bitcoin["bpi"]['USD']['rate_float']
        bitcoin2usd = number_of_coin * price_check
        print(f"${bitcoin2usd:,.4f}")

    if buy_count.isalpha() :
        sys.exit('Command-line argument is not a number')


except requests.RequestException:
    sys.exit('SYSTEM NOT RESPONSE !!! ')