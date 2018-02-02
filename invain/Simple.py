from .Utils import *
import sys

class Simple():

    def __init__(self, symbol):
        try:
            if is_sequence(symbol) or not isinstance(symbol, str):
                raise ValueError('InVaIN.Simple() expects a string as the only parameter')
            else: self.ticker = symbol
        except ValueError as err:
            print(err.args,"\nQuitting")
            sys.exit(1) 

    def change_ticker(self, symbol):
        try:
            if is_sequence(symbol) or not isinstance(symbol, str):
                raise ValueError('InVaIN.Simple() expects a string as the only parameter')
            else: self.ticker = symbol
        except ValueError as err:
            print(err.args,"\nQuitting")
            sys.exit(1)

    def get_ticker(self):
        return self.ticker;
        
    def get_price(self): 
         #Pull Data 
         data = quote(self.ticker,'rmp') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['price']
         else: data = list(data.values())[0]['price']
         return data

    def get_volume(self): 
         #Pull Data 
         data = quote(self.ticker,'rmv') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['volume']
         else: data = list(data.values())[0]['volume']
         return data

    def get_ask(self): 
         #Pull Data 
         data = quote(self.ticker,'a') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['ask']
         else: data = list(data.values())[0]['ask']
         return data

    def get_askSize(self): 
         #Pull Data 
         data = quote(self.ticker,'aZ') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['askSize']
         else: data = list(data.values())[0]['askSize']
         return data

    def get_averageDailyVolume3Month(self): 
         #Pull Data 
         data = quote(self.ticker,'aDy3M') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['averageDailyVolume3Month']
         else: data = list(data.values())[0]['averageDailyVolume3Month']
         return data

    def get_averageDailyVolume10Day(self): 
         #Pull Data 
         data = quote(self.ticker,'aDy10d') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['averageDailyVolume10Day']
         else: data = list(data.values())[0]['averageDailyVolume10Day']
         return data

    def get_bid(self): 
         #Pull Data 
         data = quote(self.ticker,'b') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['bid']
         else: data = list(data.values())[0]['bid']
         return data

    def get_bidSize(self): 
         #Pull Data 
         data = quote(self.ticker,'bZ') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['bidSize']
         else: data = list(data.values())[0]['bidSize']
         return data

    def get_bookValue(self): 
         #Pull Data 
         data = quote(self.ticker,'bV') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['bookValue']
         else: data = list(data.values())[0]['bookValue']
         return data

    def get_currency(self): 
         #Pull Data 
         data = quote(self.ticker,'c') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['currency']
         else: data = list(data.values())[0]['currency']
         return data

    def get_earningsTimestamp(self): 
         #Pull Data 
         data = quote(self.ticker,'eT') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['earningsTimestamp']
         else: data = list(data.values())[0]['earningsTimestamp']
         return data

    def get_earningsTimestampEnd(self): 
         #Pull Data 
         data = quote(self.ticker,'eTE') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['earningsTimestampEnd']
         else: data = list(data.values())[0]['earningsTimestampEnd']
         return data

    def get_earningsTimestampStart(self): 
         #Pull Data 
         data = quote(self.ticker,'eTS') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['earningsTimestampStart']
         else: data = list(data.values())[0]['earningsTimestampStart']
         return data

    def get_epsForward(self): 
         #Pull Data 
         data = quote(self.ticker,'epsF') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['epsForward']
         else: data = list(data.values())[0]['epsForward']
         return data

    def get_epsTrailingTwelveMonths(self): 
         #Pull Data 
         data = quote(self.ticker,'epsT') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['epsTrailingTwelveMonths']
         else: data = list(data.values())[0]['epsTrailingTwelveMonths']
         return data

    def get_fiftyDayAverage(self): 
         #Pull Data 
         data = quote(self.ticker,'fifDyAvg') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['fiftyDayAverage']
         else: data = list(data.values())[0]['fiftyDayAverage']
         return data

    def get_fiftyDayAverageChange(self): 
         #Pull Data 
         data = quote(self.ticker,'fifDyAvgCh') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['fiftyDayAverageChange']
         else: data = list(data.values())[0]['fiftyDayAverageChange']
         return data

    def get_fiftyDayAverageChangePercent(self): 
         #Pull Data 
         data = quote(self.ticker,'fifDyAvgChP') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['fiftyDayAverageChangePercent']
         else: data = list(data.values())[0]['fiftyDayAverageChangePercent']
         return data

    def get_fiftyTwoWeekHigh(self): 
         #Pull Data 
         data = quote(self.ticker,'fif2Wh') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['fiftyTwoWeekHigh']
         else: data = list(data.values())[0]['fiftyTwoWeekHigh']
         return data

    def get_fiftyTwoWeekHighChange(self): 
         #Pull Data 
         data = quote(self.ticker,'fif2WhCh') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['fiftyTwoWeekHighChange']
         else: data = list(data.values())[0]['fiftyTwoWeekHighChange']
         return data

    def get_fiftyTwoWeekHighChangePercent(self): 
         #Pull Data 
         data = quote(self.ticker,'fif2WhChP') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['fiftyTwoWeekHighChangePercent']
         else: data = list(data.values())[0]['fiftyTwoWeekHighChangePercent']
         return data

    def get_fiftyTwoWeekLow(self): 
         #Pull Data 
         data = quote(self.ticker,'fif2Wl') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['fiftyTwoWeekLow']
         else: data = list(data.values())[0]['fiftyTwoWeekLow']
         return data

    def get_fiftyTwoWeekLowChange(self): 
         #Pull Data 
         data = quote(self.ticker,'fif2WlCh') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['fiftyTwoWeekLowChange']
         else: data = list(data.values())[0]['fiftyTwoWeekLowChange']
         return data

    def get_fiftyTwoWeekLowChangePercent(self): 
         #Pull Data 
         data = quote(self.ticker,'fif2WlChP') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['fiftyTwoWeekLowChangePercent']
         else: data = list(data.values())[0]['fiftyTwoWeekLowChangePercent']
         return data

    def get_financialCurrency(self): 
         #Pull Data 
         data = quote(self.ticker,'fC') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['financialCurrency']
         else: data = list(data.values())[0]['financialCurrency']
         return data

    def get_forwardPE(self): 
         #Pull Data 
         data = quote(self.ticker,'fPE') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['forwardPE']
         else: data = list(data.values())[0]['forwardPE']
         return data

    def get_fullExchangeName(self): 
         #Pull Data 
         data = quote(self.ticker,'fEXN') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['fullExchangeName']
         else: data = list(data.values())[0]['fullExchangeName']
         return data

    def get_gmtOffSetMilliseconds(self): 
         #Pull Data 
         data = quote(self.ticker,'gmtOff') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['gmtOffSetMilliseconds']
         else: data = list(data.values())[0]['gmtOffSetMilliseconds']
         return data

    def get_longName(self): 
         #Pull Data 
         data = quote(self.ticker,'lN') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['longName']
         else: data = list(data.values())[0]['longName']
         return data

    def get_marketCap(self): 
         #Pull Data 
         data = quote(self.ticker,'mC') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['marketCap']
         else: data = list(data.values())[0]['marketCap']
         return data

    def get_marketChange(self): 
         #Pull Data 
         data = quote(self.ticker,'regMCh') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['marketChange']
         else: data = list(data.values())[0]['marketChange']
         return data

    def get_marketChangePercent(self): 
         #Pull Data 
         data = quote(self.ticker,'regMChP') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['marketChangePercent']
         else: data = list(data.values())[0]['marketChangePercent']
         return data

    def get_marketDayHigh(self): 
         #Pull Data 
         data = quote(self.ticker,'regMDyH') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['marketDayHigh']
         else: data = list(data.values())[0]['marketDayHigh']
         return data

    def get_marketDayLow(self): 
         #Pull Data 
         data = quote(self.ticker,'regMDyL') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['marketDayLow']
         else: data = list(data.values())[0]['marketDayLow']
         return data

    def get_marketOpen(self): 
         #Pull Data 
         data = quote(self.ticker,'regMO') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['marketOpen']
         else: data = list(data.values())[0]['marketOpen']
         return data

    def get_marketPreviousClose(self): 
         #Pull Data 
         data = quote(self.ticker,'regMPvC') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['marketPreviousClose']
         else: data = list(data.values())[0]['marketPreviousClose']
         return data

    def get_marketTime(self): 
         #Pull Data 
         data = quote(self.ticker,'rmt') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['marketTime']
         else: data = list(data.values())[0]['marketTime']
         return data

    def get_postMarketChange(self): 
         #Pull Data 
         data = quote(self.ticker,'pmCh') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['postMarketChange']
         else: data = list(data.values())[0]['postMarketChange']
         return data

    def get_postMarketChangePercent(self): 
         #Pull Data 
         data = quote(self.ticker,'pmChP') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['postMarketChangePercent']
         else: data = list(data.values())[0]['postMarketChangePercent']
         return data

    def get_postMarketPrice(self): 
         #Pull Data 
         data = quote(self.ticker,'pmP') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['postMarketPrice']
         else: data = list(data.values())[0]['postMarketPrice']
         return data

    def get_postMarketTime(self): 
         #Pull Data 
         data = quote(self.ticker,'pmT') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['postMarketTime']
         else: data = list(data.values())[0]['postMarketTime']
         return data

    def get_priceHint(self): 
         #Pull Data 
         data = quote(self.ticker,'pH') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['priceHint']
         else: data = list(data.values())[0]['priceHint']
         return data

    def get_priceToBook(self): 
         #Pull Data 
         data = quote(self.ticker,'p2B') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['priceToBook']
         else: data = list(data.values())[0]['priceToBook']
         return data

    def get_sharesOutstanding(self): 
         #Pull Data 
         data = quote(self.ticker,'sho') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['sharesOutstanding']
         else: data = list(data.values())[0]['sharesOutstanding']
         return data

    def get_shortName(self): 
         #Pull Data 
         data = quote(self.ticker,'shN') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['shortName']
         else: data = list(data.values())[0]['shortName']
         return data

    def get_symbol(self): 
         #Pull Data 
         data = quote(self.ticker,'sym') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['symbol']
         else: data = list(data.values())[0]['symbol']
         return data

    def get_tradeable(self): 
         #Pull Data 
         data = quote(self.ticker,'tdbl') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['tradeable']
         else: data = list(data.values())[0]['tradeable']
         return data

    def get_trailingPE(self): 
         #Pull Data 
         data = quote(self.ticker,'tPE') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['trailingPE']
         else: data = list(data.values())[0]['trailingPE']
         return data

    def get_twoHundredDayAverage(self): 
         #Pull Data 
         data = quote(self.ticker,'tHdDyAv') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['twoHundredDayAverage']
         else: data = list(data.values())[0]['twoHundredDayAverage']
         return data

    def get_twoHundredDayAverageChange(self): 
         #Pull Data 
         data = quote(self.ticker,'tHdDyAvCh') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['twoHundredDayAverageChange']
         else: data = list(data.values())[0]['twoHundredDayAverageChange']
         return data

    def get_twoHundredDayAverageChangePercent(self): 
         #Pull Data 
         data = quote(self.ticker,'tHdDyAvChP') 

         #Isolate Stock Data
         if len(data) > 1:
             for ticker in data:
                 data[ticker] = data[ticker]['twoHundredDayAverageChangePercent']
         else: data = list(data.values())[0]['twoHundredDayAverageChangePercent']
         return data



    

