import requests
import sys

n = sys.argv[1]
try:
    assert float(sys.argv[1])
except:
    sys.exit('Invalid Input')
try:
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json',)
    print(data.json())
except requests.RequestException:
    sys.exit('Invalid Input')