import requests
import datetime
import time
from .__version__ import __version__

def is_sequence(arg):
    #If arg has strip function it is a String so not sequence. If it has __getitem__ or __iter__ attribute it is iterable
    return not hasattr(arg, "strip") and (hasattr(arg, "__getitem__") or hasattr(arg, "__iter__"))

def fetch(rtype, parameters):
        BASE_URL = 'http://aws.inva.in/'
        headers = {'User-Agent': 'InVaIN/'+__version__}        

        url = BASE_URL+rtype
        
        
        #Pull Stock Data
        response = requests.get(url, params = parameters, headers=headers)

        #Parse into Dict Object
        data = response.json()

        #return data
        return data
    
def quote(tickers, fields):     

        #Stringify if list
        if is_sequence(tickers):
            tickers = ','.join(tickers)
            
        if is_sequence(fields):
            fields = ','.join(fields)
            
        #Prepare the Parameters
        temp = {'t':tickers, 'f': fields}

        #Parse into Dict Object
        data = fetch('quotes', temp)

        #return data
        return data

def hist(tickers, period, interval):     
        period1 = "";
        period2 = "";

        if is_sequence(tickers):
            tickers = ','.join(tickers)
        period1 = period[0]
        period2 = period[1]
            
        times = str(period1)+','+str(period2)
        #Prepare the Parameters - Period 1 is oldest date - Period 2 is newest date
        temp = {'t': tickers, 'times': times , 'inter' : interval}

        #Parse into Dict Object
        data = fetch('hist', temp)

        for key in data:
            data[key] = csv_format(data[key])
            
        #return data
        return data


def csv_format(data):
    #Returns each row of the CSV
    data = data.rstrip().split('\n')

    #Creat Dict object with headers as keys and lists to be filled with data
    csv_data = {header : list() for header in data[0].split(',')}

    #Remove Header row since we no longer need it 
    data.remove(data[0])
    
    #Loop to fill each header list with data from the csv
    for datum in data:
        temp = datum.split(',')
        #Reverse order of list so we can pop elements off and won't need to track index in for loop
        temp.reverse()

        #Loop to fill add data from row to appropriate header
        for key in csv_data.keys():
            csv_data[key].append(temp.pop())
            
    return csv_data
    
