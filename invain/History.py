import requests
import datetime
import time
import sys
from .Utils import *

class History():

    #Start and End are datetime objects with start being the older of the two dates.
    #Frequency has three options for interval of returned dates with daily = d, weekly = wk, and monthly = mo; All options accept any number n in the form of nd, nwk, or nmo with n being the number of days, weeks, or months
    def __init__(self, ticker, start=None, end=None, frequency='1d'):
        now = int(time.mktime(datetime.datetime.now().timetuple()))
        
        #Check if ticker var is a list or string then set self.ticker to a list of ticker(s)
        self.ticker = [symbol.upper() for symbol in ticker] if is_sequence(ticker) else [ticker.upper()]

        #Check if start exists - if not default start time is 30 days from now, if start exists set start to strat.
        period1 = now - 30*24*60*60 if start is None else int(time.mktime(start.timetuple()))
        period2 =  now if end is None else int(time.mktime(end.timetuple()))

        self.period = [period1, period2]
        
        self.interval = frequency
        
        #Grab Historical Data
        self.hist_data = hist(self.ticker, self.period, self.interval)

    #Add Tickers to End of List, Extend Allows for ticker to be a List                
    def add_ticker(self, ticker):
        self.ticker.extend([symbol.upper() for symbol in ticker]) if is_sequence(ticker) else self.ticker.extend([ticker.upper()])   
                
    #If Someone is Sketch About Singular Form
    def add_tickers(self, tickers, *extras):
        self.add_ticker(tickers)
        self.add_ticker(extras)

    def remove_ticker(self, ticker):
        try:
            if ticker in self.ticker: self.ticker.remove(ticker.upper())
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

    def get_date(self, ticker=None):
        #Check if ticker is provided; if ticker is provided and is a list of tickers, return data for those tickers, otherwise return data for that ticker, or if no ticker is provided return data for all tickers 
        return {key : self.hist_data[key]['Date'] for key in self.hist_data} if ticker is None else {key : self.hist_data[key]['Date'] for key in ticker} if is_sequence(ticker) else {ticker : self.hist_data[ticker]['Date']}

    def get_open(self, ticker=None):
        #Check if ticker is provided; if ticker is provided and is a list of tickers, return data for those tickers, otherwise return data for that ticker, or if no ticker is provided return data for all tickers 
        return {key : self.hist_data[key]['Open'] for key in self.hist_data} if ticker is None else {key : self.hist_data[key]['Open'] for key in ticker} if is_sequence(ticker) else {ticker : self.hist_data[ticker]['Open']}

    def get_highs(self, ticker=None):
        #Check if ticker is provided; if ticker is provided and is a list of tickers, return data for those tickers, otherwise return data for that ticker, or if no ticker is provided return data for all tickers 
        return {key : self.hist_data[key]['High'] for key in self.hist_data} if ticker is None else {key : self.hist_data[key]['High'] for key in ticker} if is_sequence(ticker) else {ticker : self.hist_data[ticker]['High']}

    def get_low(self, ticker=None):
        #Check if ticker is provided; if ticker is provided and is a list of tickers, return data for those tickers, otherwise return data for that ticker, or if no ticker is provided return data for all tickers 
        return {key : self.hist_data[key]['Low'] for key in self.hist_data} if ticker is None else {key : self.hist_data[key]['Low'] for key in ticker} if is_sequence(ticker) else {ticker : self.hist_data[ticker]['Low']}

    def get_close(self, ticker=None):
        #Check if ticker is provided; if ticker is provided and is a list of tickers, return data for those tickers, otherwise return data for that ticker, or if no ticker is provided return data for all tickers 
        return {key : self.hist_data[key]['Close'] for key in self.hist_data} if ticker is None else {key : self.hist_data[key]['Close'] for key in ticker} if is_sequence(ticker) else {ticker : self.hist_data[ticker]['Close']}

    def get_adj_close(self, ticker=None):
        #Check if ticker is provided; if ticker is provided and is a list of tickers, return data for those tickers, otherwise return data for that ticker, or if no ticker is provided return data for all tickers 
        return {key : self.hist_data[key]['Adj Close'] for key in self.hist_data} if ticker is None else {key : self.hist_data[key]['Adj Close'] for key in ticker} if is_sequence(ticker) else {ticker : self.hist_data[ticker]['Adj Close']}

    def get_volume(self, ticker=None):
        #Check if ticker is provided; if ticker is provided and is a list of tickers, return data for those tickers, otherwise return data for that ticker, or if no ticker is provided return data for all tickers 
        return {key : self.hist_data[key]['Volume'] for key in self.hist_data} if ticker is None else {key : self.hist_data[key]['Volume'] for key in ticker} if is_sequence(ticker) else {ticker : self.hist_data[ticker]['Volume']}

    def get_combo(self,**kwargs):
        #If user does not provide either ticker or field, then we return an error
        if not kwargs : return "Error History.get_combo(): No ticker or data field provided. Cannot combine"

        ticker = kwargs['tickers'] if 'tickers' in kwargs else None
        field = kwargs['fields'] if 'fields' in kwargs else None
        #Check if ticker is provided; if ticker is provided and is a list of tickers, return data for those tickers, otherwise return data for that ticker, or if no ticker is provided return data for all tickers 
        tickers = [key for key in self.hist_data] if ticker is None else [key.upper() for key in ticker] if is_sequence(ticker) else [ticker.upper()]
        #Check if field is provided; if field is provided and is a list of field, return data for those field, otherwise return data for that field, or if no field is provided return data for all fields 
        fields = [header for header in self.hist_data[self.ticker[0]]] if field is None else [header.title() for header in field] if is_sequence(field) else [field.title()]

        data = {key : {header : self.hist_data[key][header] for header in fields} for key in tickers}
        return data

























        




