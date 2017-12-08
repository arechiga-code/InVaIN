import requests

def is_sequence(arg):
    #If arg has strip function it is a String so not sequence. If it has __getitem__ or __iter__ attribute it is iterable
    return not hasattr(arg, "strip") and (hasattr(arg, "__getitem__") or hasattr(arg, "__iter__"))

def fetch(tickers, fields):
        BASE_URL = 'http://aws.inva.in/quotes'
        
        #Stringify if list
        if is_sequence(tickers):
            tickers = ','.join(tickers)
            
        if is_sequence(fields):
            fields = ','.join(fields)
            
        #Prepare the Parameters
        temp = {'t':tickers, 'f': fields}        

        #Pull Stock Data
        response = requests.get(BASE_URL, params = temp)

        #Parse into Dict Object
        data = response.json()

        #return data
        return data
