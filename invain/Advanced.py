import requests
import sys
from .Simple import Simple
from .Utils import *

class Advanced(Simple):
    def __init__(self, ticker, *extras):
        #Check if ticker var is a list or string then set self.ticker to a list of ticker(s)
        self.ticker = [symbol.upper() for symbol in ticker] if is_sequence(ticker) else [ticker.upper()]

        self.add_tickers([symbol.upper() for symbol in extras])

        self.field = []
        
        
    #Nullify method for removal
    def change_ticker(self):
        return
        
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
        return self.ticker;
            
#              Add Fields to Custom Field List
#################################################################
    def add_price(self): 
         self.field.extend(['rmp']) 

    def remove_price(self): 
         if 'rmp' in self.field: self.field.remove('rmp') 

    def add_volume(self): 
         self.field.extend(['rmv']) 

    def remove_volume(self): 
         if 'rmv' in self.field: self.field.remove('rmv') 

    def add_ask(self): 
         self.field.extend(['a']) 

    def remove_ask(self): 
         if 'a' in self.field: self.field.remove('a') 

    def add_askSize(self): 
         self.field.extend(['aZ']) 

    def remove_askSize(self): 
         if 'aZ' in self.field: self.field.remove('aZ') 

    def add_averageDailyVolume3Month(self): 
         self.field.extend(['aDy3M']) 

    def remove_averageDailyVolume3Month(self): 
         if 'aDy3M' in self.field: self.field.remove('aDy3M') 

    def add_averageDailyVolume10Day(self): 
         self.field.extend(['aDy10d']) 

    def remove_averageDailyVolume10Day(self): 
         if 'aDy10d' in self.field: self.field.remove('aDy10d') 

    def add_bid(self): 
         self.field.extend(['b']) 

    def remove_bid(self): 
         if 'b' in self.field: self.field.remove('b') 

    def add_bidSize(self): 
         self.field.extend(['bZ']) 

    def remove_bidSize(self): 
         if 'bZ' in self.field: self.field.remove('bZ') 

    def add_bookValue(self): 
         self.field.extend(['bV']) 

    def remove_bookValue(self): 
         if 'bV' in self.field: self.field.remove('bV') 

    def add_currency(self): 
         self.field.extend(['c']) 

    def remove_currency(self): 
         if 'c' in self.field: self.field.remove('c') 

    def add_earningsTimestamp(self): 
         self.field.extend(['eT']) 

    def remove_earningsTimestamp(self): 
         if 'eT' in self.field: self.field.remove('eT') 

    def add_earningsTimestampEnd(self): 
         self.field.extend(['eTE']) 

    def remove_earningsTimestampEnd(self): 
         if 'eTE' in self.field: self.field.remove('eTE') 

    def add_earningsTimestampStart(self): 
         self.field.extend(['eTS']) 

    def remove_earningsTimestampStart(self): 
         if 'eTS' in self.field: self.field.remove('eTS') 

    def add_epsForward(self): 
         self.field.extend(['epsF']) 

    def remove_epsForward(self): 
         if 'epsF' in self.field: self.field.remove('epsF') 

    def add_epsTrailingTwelveMonths(self): 
         self.field.extend(['epsT']) 

    def remove_epsTrailingTwelveMonths(self): 
         if 'epsT' in self.field: self.field.remove('epsT') 

    def add_fiftyDayAverage(self): 
         self.field.extend(['fifDyAvg']) 

    def remove_fiftyDayAverage(self): 
         if 'fifDyAvg' in self.field: self.field.remove('fifDyAvg') 

    def add_fiftyDayAverageChange(self): 
         self.field.extend(['fifDyAvgCh']) 

    def remove_fiftyDayAverageChange(self): 
         if 'fifDyAvgCh' in self.field: self.field.remove('fifDyAvgCh') 

    def add_fiftyDayAverageChangePercent(self): 
         self.field.extend(['fifDyAvgChP']) 

    def remove_fiftyDayAverageChangePercent(self): 
         if 'fifDyAvgChP' in self.field: self.field.remove('fifDyAvgChP') 

    def add_fiftyTwoWeekHigh(self): 
         self.field.extend(['fif2Wh']) 

    def remove_fiftyTwoWeekHigh(self): 
         if 'fif2Wh' in self.field: self.field.remove('fif2Wh') 

    def add_fiftyTwoWeekHighChange(self): 
         self.field.extend(['fif2WhCh']) 

    def remove_fiftyTwoWeekHighChange(self): 
         if 'fif2WhCh' in self.field: self.field.remove('fif2WhCh') 

    def add_fiftyTwoWeekHighChangePercent(self): 
         self.field.extend(['fif2WhChP']) 

    def remove_fiftyTwoWeekHighChangePercent(self): 
         if 'fif2WhChP' in self.field: self.field.remove('fif2WhChP') 

    def add_fiftyTwoWeekLow(self): 
         self.field.extend(['fif2Wl']) 

    def remove_fiftyTwoWeekLow(self): 
         if 'fif2Wl' in self.field: self.field.remove('fif2Wl') 

    def add_fiftyTwoWeekLowChange(self): 
         self.field.extend(['fif2WlCh']) 

    def remove_fiftyTwoWeekLowChange(self): 
         if 'fif2WlCh' in self.field: self.field.remove('fif2WlCh') 

    def add_fiftyTwoWeekLowChangePercent(self): 
         self.field.extend(['fif2WlChP']) 

    def remove_fiftyTwoWeekLowChangePercent(self): 
         if 'fif2WlChP' in self.field: self.field.remove('fif2WlChP') 

    def add_financialCurrency(self): 
         self.field.extend(['fC']) 

    def remove_financialCurrency(self): 
         if 'fC' in self.field: self.field.remove('fC') 

    def add_forwardPE(self): 
         self.field.extend(['fPE']) 

    def remove_forwardPE(self): 
         if 'fPE' in self.field: self.field.remove('fPE') 

    def add_fullExchangeName(self): 
         self.field.extend(['fEXN']) 

    def remove_fullExchangeName(self): 
         if 'fEXN' in self.field: self.field.remove('fEXN') 

    def add_gmtOffSetMilliseconds(self): 
         self.field.extend(['gmtOff']) 

    def remove_gmtOffSetMilliseconds(self): 
         if 'gmtOff' in self.field: self.field.remove('gmtOff') 

    def add_longName(self): 
         self.field.extend(['lN']) 

    def remove_longName(self): 
         if 'lN' in self.field: self.field.remove('lN') 

    def add_marketCap(self): 
         self.field.extend(['mC']) 

    def remove_marketCap(self): 
         if 'mC' in self.field: self.field.remove('mC') 

    def add_marketChange(self): 
         self.field.extend(['regMCh']) 

    def remove_marketChange(self): 
         if 'regMCh' in self.field: self.field.remove('regMCh') 

    def add_marketChangePercent(self): 
         self.field.extend(['regMChP']) 

    def remove_marketChangePercent(self): 
         if 'regMChP' in self.field: self.field.remove('regMChP') 

    def add_marketDayHigh(self): 
         self.field.extend(['regMDyH']) 

    def remove_marketDayHigh(self): 
         if 'regMDyH' in self.field: self.field.remove('regMDyH') 

    def add_marketDayLow(self): 
         self.field.extend(['regMDyL']) 

    def remove_marketDayLow(self): 
         if 'regMDyL' in self.field: self.field.remove('regMDyL') 

    def add_marketOpen(self): 
         self.field.extend(['regMO']) 

    def remove_marketOpen(self): 
         if 'regMO' in self.field: self.field.remove('regMO') 

    def add_marketPreviousClose(self): 
         self.field.extend(['regMPvC']) 

    def remove_marketPreviousClose(self): 
         if 'regMPvC' in self.field: self.field.remove('regMPvC') 

    def add_marketTime(self): 
         self.field.extend(['rmt']) 

    def remove_marketTime(self): 
         if 'rmt' in self.field: self.field.remove('rmt') 

    def add_postMarketChange(self): 
         self.field.extend(['pmCh']) 

    def remove_postMarketChange(self): 
         if 'pmCh' in self.field: self.field.remove('pmCh') 

    def add_postMarketChangePercent(self): 
         self.field.extend(['pmChP']) 

    def remove_postMarketChangePercent(self): 
         if 'pmChP' in self.field: self.field.remove('pmChP') 

    def add_postMarketPrice(self): 
         self.field.extend(['pmP']) 

    def remove_postMarketPrice(self): 
         if 'pmP' in self.field: self.field.remove('pmP') 

    def add_postMarketTime(self): 
         self.field.extend(['pmT']) 

    def remove_postMarketTime(self): 
         if 'pmT' in self.field: self.field.remove('pmT') 

    def add_priceHint(self): 
         self.field.extend(['pH']) 

    def remove_priceHint(self): 
         if 'pH' in self.field: self.field.remove('pH') 

    def add_priceToBook(self): 
         self.field.extend(['p2B']) 

    def remove_priceToBook(self): 
         if 'p2B' in self.field: self.field.remove('p2B') 

    def add_sharesOutstanding(self): 
         self.field.extend(['sho']) 

    def remove_sharesOutstanding(self): 
         if 'sho' in self.field: self.field.remove('sho') 

    def add_shortName(self): 
         self.field.extend(['shN']) 

    def remove_shortName(self): 
         if 'shN' in self.field: self.field.remove('shN') 

    def add_symbol(self): 
         self.field.extend(['sym']) 

    def remove_symbol(self): 
         if 'sym' in self.field: self.field.remove('sym') 

    def add_tradeable(self): 
         self.field.extend(['tdbl']) 

    def remove_tradeable(self): 
         if 'tdbl' in self.field: self.field.remove('tdbl') 

    def add_trailingPE(self): 
         self.field.extend(['tPE']) 

    def remove_trailingPE(self): 
         if 'tPE' in self.field: self.field.remove('tPE') 

    def add_twoHundredDayAverage(self): 
         self.field.extend(['tHdDyAv']) 

    def remove_twoHundredDayAverage(self): 
         if 'tHdDyAv' in self.field: self.field.remove('tHdDyAv') 

    def add_twoHundredDayAverageChange(self): 
         self.field.extend(['tHdDyAvCh']) 

    def remove_twoHundredDayAverageChange(self): 
         if 'tHdDyAvCh' in self.field: self.field.remove('tHdDyAvCh') 

    def add_twoHundredDayAverageChangePercent(self): 
         self.field.extend(['tHdDyAvChP']) 

    def remove_twoHundredDayAverageChangePercent(self): 
         if 'tHdDyAvChP' in self.field: self.field.remove('tHdDyAvChP') 


#           Custom Data 
##############################################################
    def get_customData(self):
        try:
            if self.field :
                data = quote(self.ticker,self.field)
            else: raise ValueError('InVaIN.Advanced() Missing fields for customData.')
        
        except ValueError as err:
            print(err.args,"\n Abortting Script")
            sys.exit(1)
        return data
