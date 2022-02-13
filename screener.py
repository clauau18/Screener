from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#fullRequest = requests.get("https://api.coingecko.com/api/v3/coins/list").json()
#fullRequest = requests.get("https://api.coingecko.com/api/v3/simple/supported_vs_currencies").json()
url_coinGecko = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
url_cmc = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'


headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '27b892a8-87f3-475a-8d4a-ec3e39344b02',
}

parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url_cmc, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)