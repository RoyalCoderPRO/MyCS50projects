import requests
import sys

try:
    n = sys.argv[1]
    assert float(n)

except AssertionError:
    sys.exit('Command-line argument is not a number')
except IndexError:
    sys.exit('Missing command-line argument')

try:
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json',)
except requests.RequestException:
    sys.exit('Invalid Input')

price = float(data.json()['bpi']['USD']['rate_float'])
total = price*float(n)
print(f"${total:,.4f}")