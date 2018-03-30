import requests
import datetime
import time
import sys
from .Utils import *

class History():
    
    def __init__(self, ticker, *extras, **kwargs):
        if kwargs:
            #Check if start, end, or frequency are provided, and set accordingly
            start = kwargs['start'] if 'start' in kwargs else None
            end = kwargs['end'] if 'end' in kwargs else None
            frequency = kwargs['frequency'] if 'frequency' in kwargs else 'daily'
            num_between = kwargs['num_between'] if 'num_between' in kwargs else 1
        else:
            start = None
            end = None
            frequency = 'daily'
            num_between = 1

        now = int(time.mktime(datetime.datetime.now().timetuple()))

        #Check if start exists - if not default start time is 30 days from now, if start exists set start to strat.
        period1 = now - 30*24*60*60 if start is None else int(time.mktime(start.timetuple()))
        period2 =  now if end is None else int(time.mktime(end.timetuple()))

        if period1 > period2:
            print("Start is greater than end, cannot initialize History() object \nQuitting")
            sys.exit(1)
        
        #Check if ticker var is a list or string then set self.ticker to a list of ticker(s)
        self.ticker = [symbol.upper() for symbol in ticker] if is_sequence(ticker) else [ticker.upper()]

        #Add extra tickers if object created with parameters in the form of ('TIC','KER','XTRA')
        if extras: self.add_tickers([symbol.upper() for symbol in extras])
        
        #Set period to a list of unix timestamps, with the first item being the later time.
        self.period = [period1, period2]

        self.interval =  ""
        self.change_frequency(frequency,num_between)
        
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
            
    def get_tickers(self):
        return self.ticker

    #Returns list of datetimes instead of unix timestamps
    def get_period(self):
        return [datetime.datetime.fromtimestamp(timestamp) for timestamp in self.period]
    
    def get_startDate(self):
        return datetime.datetime.fromtimestamp(self.period[0])

    def get_endDate(self):
        return datetime.datetime.fromtimestamp(self.period[1])

    #Parameter set to *periods to allow user to provide period in an array (['period1', 'period2']) or individual parameters ('period1', 'period2')
    def change_period(self, *periods):
        #if more than two or no parameters provided there is a problem
        if len(periods) > 2 or not periods :
            print("Error History.change_period(): change_period requires either 1 list of 2 datetime objects, or 2 datetime objects as parameters. Period not changed")
            return
        
        #if not is_sequence(periods[0]):
        if len(periods) == 2:
            for period in periods:
                #If either item is not a datetime object, there is a problem
                if not isinstance(period, datetime.datetime):
                    print("Error History.change_period(): change_period requires either 1 list of 2 datetime objects, or 2 datetime objects as parameters. Period not changed")
                    return
                
            start = int(time.mktime(periods[0].timetuple()))
            end = int(time.mktime(periods[1].timetuple()))
            
            #Start time cannot be greater than end time
            if start > end:
                print("Error History.change_period(): Start time cannot be newer than end time. Please make sure you are providing the parameters in the correct order: (start, end) \n Period not changed")
                return
            
            self.period[0] = start
            self.period[1] = end
            return
        #If two lists are provided, there is a problem        
        #if is_sequence(periods[1]):
        #    print("Error History.change_period(): change_period requires either 1 list of 2 datetime objects, or 2 datetime objects as parameters. Period not changed")
         #   return
        
        #our last option is that the period is a list of datetimes    
        for period in periods[0]:
            #If either item is not a datetime object, there is a problem
            if not isinstance(period, datetime.datetime):
                print("Error History.change_period(): change_period requires either 1 list of 2 datetime objects, or 2 datetime objects as parameters. Period not changed")
                return
        start = int(time.mktime(periods[0][0].timetuple()))
        end = int(time.mktime(periods[0][1].timetuple()))
        if start > end:
            print("Error History.change_period(): Start time cannot be newer than end time. Please make sure datetimes in list are in the correct order: [start, end] \n Period not changed")
            return
        
        self.period[0] = start
        self.period[1] = end

    def change_startTime(self, start):
        if not isinstance(start, datetime.datetime):
            print("Error History.change_startTime(): change_startTime requires a single datetime object as parameters. Start not changed")
            return
        start = int(time.mktime(start.timetuple()))
        self.period[0] = start
        
    def change_endTime(self, end):
        if not isinstance(end, datetime.datetime):
            print("Error History.change_endTime(): change_endTime requires a single datetime object as parameters. End not changed")
            return
        end = int(time.mktime(end.timetuple()))
        self.period[1] = end
    
    def get_dataset(self):
        return self.hist_data

    def update_dataset(self):
        if self.period[0]>self.period[1]:
            print("Error History.update_dataset(): Start time cannot be newer than end time. Please update period \n Data not updated")
            return
        
        self.hist_data = hist(self.ticker, self.period, self.interval)
        return self.hist_data

    def change_frequency(self, frequency, num_between=1):
        compare = frequency.strip().lower()
        if isinstance(num_between, int):
            n = str(num_between)
        else:
            print("Error Changing Frequency: num_between is not of type int")
            return False
        if compare == 'daily':
            self.interval = n + "d"
        elif compare == 'weekly':
            self.interval = n + "wk"
        elif compare == 'monthly':
            self.interval = n + "mo"
        else:
            print("Error Changing Frequency: Not a Valid Frequency")
            return False
        return True

    def get_date(self, ticker=None):
        #Check if ticker is provided; if ticker is provided and is a list of tickers, return data for those tickers, otherwise return data for that ticker, or if no ticker is provided return data for all tickers 
        return {key : self.hist_data[key]['Date'] for key in self.hist_data} if ticker is None else {key : self.hist_data[key]['Date'] for key in ticker} if is_sequence(ticker) else {ticker : self.hist_data[ticker]['Date']}

    def get_open(self, ticker=None):
        #Check if ticker is provided; if ticker is provided and is a list of tickers, return data for those tickers, otherwise return data for that ticker, or if no ticker is provided return data for all tickers 
        return {key : self.hist_data[key]['Open'] for key in self.hist_data} if ticker is None else {key : self.hist_data[key]['Open'] for key in ticker} if is_sequence(ticker) else {ticker : self.hist_data[ticker]['Open']}

    def get_high(self, ticker=None):
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

























        




