import os
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time

#API key and URL
api_key = '################INSERT_API_KEY_HERE##############'
api_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

#Params and Headers
parameters = {
  'start':'1',
  'limit':'1',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}


#Function that pulls the API and then grabs the BTC price and Percent
#change and uses them as parameters with the Bash script
def poster(parameters, headers):
    session = Session()
    session.headers.update(headers)

    try:
        global api_URL
        response = session.get(api_URL, params=parameters)
        data = json.loads(response.text)
        print(data["data"][0]["quote"]["USD"]["price"])
        price_0 = data["data"][0]["quote"]["USD"]["price"]
        change_0 = data["data"][0]["quote"]["USD"]["percent_change_1h"]
        price = str(round(price_0, 2))
        change = str(round(change_0, 2))
        #print("BTC price: $" + str(price) + "\nPercent change: " + str(change) + "%")
        os.system('./slack_curl ' +  price + ' ' + change)
        return True

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return False

#Main function
def main():
    global parameters
    global headers
    while(True):
        poster(parameters, headers)
        time.sleep(3600)

main()






