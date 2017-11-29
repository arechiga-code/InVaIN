import requests
import json
__version___ = ".01";

BASE_URL = 'https://inva.in/quotes'

class InVaIN():
        
        def __init__(self, *symbols):
                self.tickers = list(symbols)

        #Add Tickers to End of List, Extend Allows for ticker to be a List                
        def add_ticker(self, ticker):
                self.tickers.extend(ticker)
        #If Someone is Sketch About Singular Form
        def add_tickers(self, tickers):
                self.add_ticker(tickers)

        def remove_ticker(self, ticker):
                self.tickers.remove(ticker)
                
        #Returns Ticker List
        def get_tickers(self):
                return self.tickers;

        def get_price_string(self):
                #Prepare the Parameters
                temp = {'t':','.join(self.tickers)}
                
                #Pull Stock Price Data
                response = requests.get(BASE_URL, params = temp)

                #Parse into CSV string
                data = ','.join(str(s) for s in response.json().values())
                return data
        
        def get_prices(self):
                #Prepare the Parameters
                temp = {'t':','.join(self.tickers)}
                
                #Pull Stock Price Data
                response = requests.get(BASE_URL, params = temp)

                #Parse into Dict Object
                data = response.json()
                return data
