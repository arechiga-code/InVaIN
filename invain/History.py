import requests
import datetime
import time
import sys
from .Utils import *

class History():

    #Start and End are datetime objects with start being the older of the two dates.
    #Frequency has three options for interval of returned dates with daily = d, weekly = wk, and monthly = mo; All options accept any number n in the form of nd, nwk, or nmo with n being the number of days, weeks, or months
    def __init__(self, ticker, start=None, end=None, frequency='1d', *extras):
        now = int(time.mktime(datetime.datetime.now().timetuple()))
        
        #Check if ticker var is a list or string then set self.ticker to a list of ticker(s)
        self.ticker = ticker if is_sequence(ticker) else [ticker]

        #Check if start exists - if not default start time is 30 days from now, if start exists set start to strat.
        period1 = now - 30*24*60*60 if start is None else int(time.mktime(start.timetuple()))
        period2 =  now if end is None else int(time.mktime(end.timetuple()))

        self.period = [period1, period2]
        
        self.interval = frequency
        self.add_tickers(extras)
        
        #Grab Historical Data
        self.hist_data = hist(self.ticker, self.period, self.interval)

    #Add Tickers to End of List, Extend Allows for ticker to be a List                
    def add_ticker(self, ticker):
        self.ticker.extend(ticker) if is_sequence(ticker) else self.ticker.extend([ticker])   
                
    #If Someone is Sketch About Singular Form
    def add_tickers(self, tickers, *extras):
        self.add_ticker(tickers)
        self.add_ticker(extras)

    def remove_ticker(self, ticker):
        try:
            if ticker in self.ticker: self.ticker.remove(ticker)
            else: raise ValueError('InVaIN.Advanced() Failed to remove ticker. Ticker not found in list')
        except ValueError as err:
            print(err.args,"\n Non-Fatal Error")
                            
    def get_ticker(self):
        return self.ticker
    
    def get_dataset(self):
        return self.hist_data

    def update_dataset(self):
        self.hist_data = hist(self.ticker, self.period, self.interval)
        return self.hist_data

    def change_frequency(self, frequency, num_between=1):
        compare = frequency.strip().lower()
        if isinstance(num_between, int):
            n = str(num_between)
        else:
            print("Error Changing Frequency: num_between is not of type int")
            return
        
        self.interval = n +'d' if compare == 'daily' else n + 'wk' if compare == 'weekly' else n + 'mo' if compare == 'monthly' else print("Error Changing Frequency: Not a Valid Frequency")
