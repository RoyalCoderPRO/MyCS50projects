import requests
import sys

n = sys.argv[1]
try:
    assert float(n)
except:
    sys.exit('Invalid Input')
try:
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json',)
except requests.RequestException:
    sys.exit('Invalid Input')
price = float(data.json()['bpi']['USD']['rate_float'])
total = price*float(n)
print(f'${total}')