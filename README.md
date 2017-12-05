# InVaIN

Python module to get stock data from YAHOO! Finance <br/>
**CHANGES NOT PUSHED TO PyPI. THESE METHODS WILL NOT WORK CURRENTLY**

## Install

From PyPI with pip:

```bash
$ pip install InVaIN
```

## Brief Overview
InVaIN works either through the **Simple API** or the **Advanced API**. <br />
**Simple API** is only for one ticker. Once created it will get any stock data for that ticker. It returns just the value so no need for parsing data. Simple API allow for ticker to be changed. <br />
**Advanced API** hold a list of tickers that can be added to and modified. Advanced API can use Simple object methods, but also have the ability to add several data fields to gather large data sets quickly. Returns values in a dict object so parsing data is neccesary.  

## Code Examples

### Example: Simple API -- Apple Inc. (``AAPL``)

``` python   
import InVaIN

#Create Simple API object
api = InVaIN.Simple('HD') 
#Get market price
print(api.get_price())
###################
'173.07'
```

### Example: Advanced API Method 1 -- Apple Inc. (``AAPL``), Alphabet Inc. (``GOOG``), Microsoft Inc. (``MSFT``) 

```python
import InVaIN

#Create Advanced API object with all the tickers provided
api = InVaIN.Advanced('AAPL','GOOG', 'MSFT')

#Use Simple API method to get price
prices = api.get_price()

#Returns dict object with stock as the index
for stock in prices:
   print(stock, prices[stock])
###################
'AAPL 173.07'
'GOOG 1047.41'
'MSFT 84.88'
```

### Example: Advanced API Method 2 -- Apple Inc. (``AAPL``), Alphabet Inc. (``GOOG``), Microsoft Inc. (``MSFT``) 

```python
import InVaIN

#Create Advanced API object with all the tickers provided
api = InVaIN.Advanced('AAPL','GOOG', 'MSFT')

#Add price field to data 
api.add_price()

#Fetch custom data set
prices = api.get_customData()

#Returns dict object with stock as the index
for stock in prices:
   print(stock, prices[stock])
###################
'AAPL {'price': 173.07}'
'GOOG {'price': 1047.41}'
'MSFT {'price': 84.88}'
```

## Available methods

### Simple API 
- ``change_ticker(ticker)``
- ``get_price()``
- ``get_volume()``
- ``get_ask()``
- ``get_askSize()``
- ``get_averageDailyVolume3Month()``
- ``get_averageDailyVolume10Day()``
- ``get_bid()``
- ``get_bidSize()``
- ``get_bookValue()``
- ``get_currency()``
- ``get_earningsTimestamp()``
- ``get_earningsTimestampEnd()``
- ``get_earningsTimestampStart()``
- ``get_epsForward()``
- ``get_epsTrailingTwelveMonths()``
- ``get_fiftyDayAverage()``
- ``get_fiftyDayAverageChange()``
- ``get_fiftyDayAverageChangePercent()``
- ``get_fiftyTwoWeekHigh()``
- ``get_fiftyTwoWeekHighChange()``
- ``get_fiftyTwoWeekHighChangePercent()``
- ``get_fiftyTwoWeekLow()``
- ``get_fiftyTwoWeekLowChange()``
- ``get_fiftyTwoWeekLowChangePercent()``
- ``get_financialCurrency()``
- ``get_forwardPE()``
- ``get_fullExchangeName()``
- ``get_gmtOffSetMilliseconds()``
- ``get_longName()``
- ``get_marketCap()``
- ``get_marketChange()``
- ``get_marketChangePercent()``
- ``get_marketDayHigh()``
- ``get_marketDayLow()``
- ``get_marketOpen()``
- ``get_marketPreviousClose()``
- ``get_marketTime()``
- ``get_postMarketChange()``
- ``get_postMarketChangePercent()``
- ``get_postMarketPrice()``
- ``get_postMarketTime()``
- ``get_priceHint()``
- ``get_priceToBook()``
- ``get_sharesOutstanding()``
- ``get_shortName()``
- ``get_symbol()`` -- Returns ticker for stock data being fetched
- ``get_tradeable()``
- ``get_trailingPE()``
- ``get_twoHundredDayAverage()``
- ``get_twoHundredDayAverageChange()``
- ``get_twoHundredDayAverageChangePercent()``

### Advanced API
- ``add_ticker(ticker)``
- ``add_tickers(tickers)`` -- takes list of tickers as argument (or add_tickers(ticker1,ticker2,...))
- ``remove_tickers(tickers)``
- ``add_price()``
- ``add_volume()``
- ``add_ask()``
- ``add_askSize()``
- ``add_averageDailyVolume3Month()``
- ``add_averageDailyVolume10Day()``
- ``add_bid()``
- ``add_bidSize()``
- ``add_bookValue()``
- ``add_currency()``
- ``add_earningsTimestamp()``
- ``add_earningsTimestampEnd()``
- ``add_earningsTimestampStart()``
- ``add_epsForward()``
- ``add_epsTrailingTwelveMonths()``
- ``add_fiftyDayAverage()``
- ``add_fiftyDayAverageChange()``
- ``add_fiftyDayAverageChangePercent()``
- ``add_fiftyTwoWeekHigh()``
- ``add_fiftyTwoWeekHighChange()``
- ``add_fiftyTwoWeekHighChangePercent()``
- ``add_fiftyTwoWeekLow()``
- ``add_fiftyTwoWeekLowChange()``
- ``add_fiftyTwoWeekLowChangePercent()``
- ``add_financialCurrency()``
- ``add_forwardPE()``
- ``add_fullExchangeName()``
- ``add_gmtOffSetMilliseconds()``
- ``add_longName()``
- ``add_marketCap()``
- ``add_marketChange()``
- ``add_marketChangePercent()``
- ``add_marketDayHigh()``
- ``add_marketDayLow()``
- ``add_marketOpen()``
- ``add_marketPreviousClose()``
- ``add_marketTime()``
- ``add_postMarketChange()``
- ``add_postMarketChangePercent()``
- ``add_postMarketPrice()``
- ``add_postMarketTime()``
- ``add_priceHint()``
- ``add_priceToBook()``
- ``add_sharesOutstanding()``
- ``add_shortName()``
- ``add_symbol()``
- ``add_tradeable()``
- ``add_trailingPE()``
- ``add_twoHundredDayAverage()``
- ``add_twoHundredDayAverageChange()``
- ``add_twoHundredDayAverageChangePercent()``
- ``Remove for Above Functions ``

**More to Come**

## Requirements

    requests
