# InVaIN

Python module to get real time or historical stock data from YAHOO! Finance

## Brief Overview
### Real time stock data works either through the **Simple API** or the **Advanced API**
**Simple API** is only for one ticker. Once created it will get any stock data for that ticker. It returns just the value so no need for parsing data. Simple API allow for ticker to be changed. <br />
**Advanced API** hold a list of tickers that can be added to and modified. Advanced API can use Simple object methods, but also have the ability to add several data fields to gather large data sets quickly. Returns values in a dict object so parsing data is neccesary. 

### Historical data works through the **History API**
**History API** is only for historical data and will **NOT** provide real time data. History API holds a list of tickers that can be added to, a time period to get data for, and the frequency (*daily, weekly, or monthly*) and number of frequency between (*any number >= 1*) of data to return all of which can be modified or retrieved. <br />
When created it will automatically pull data for the tickers passed, using the default values for time period(*30 days from current day to current day*), frequency(*daily*), and number of frequency between (*1*), or the values supplied by you.<br />


## Install

From PyPI with pip:

```bash
$ pip install invain
```

 

## Code Examples

### Example: Simple API -- Apple Inc. (``AAPL``)

``` python   
import invain

#Create Simple API object
api = invain.Simple('HD') 
#Get market price
print(api.get_price())
###################
'173.07'
```

### Example: Advanced API Method 1 -- Apple Inc. (``AAPL``), Alphabet Inc. (``GOOG``), Microsoft Inc. (``MSFT``) 

```python
import invain

#Create Advanced API object with all the tickers provided
api = invain.Advanced('AAPL','GOOG', 'MSFT')

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
import invain

#Create Advanced API object with all the tickers provided
api = invain.Advanced('AAPL','GOOG', 'MSFT')

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

### Example: History API Method 1 -- Apple Inc. (``AAPL``), Alphabet Inc. (``GOOG``), Microsoft Inc. (``MSFT``) 

```python
import invain

#Create History API object with all tickers provided. 
#This will pull stock data for the past 30 days with an interval of 1 day.
#Note that when creating a History object, historical data is automatically pulled. 
#If tickers, start or end dates, or frequency are changed, you will need to run api.update_dataset()
api = invain.History('AAPL','GOOG', 'MSFT')

#Get custom data set
historical_data = api.get_dataset()

#Returns dict object with stock as the index
for stock in historical_data:
   print(stock, historical_data[stock])
###################
AAPL{
  'Adj Close': [...],
  'Close': [...],
  'Date': [...],
  'High': [...],
  'Low': [...],
  'Open': [...],
  'Volume': [...]
}
GOOG{
  'Adj Close': [...],
  'Close': [...],
  'Date': [...],
  'High': [...],
  'Low': [...],
  'Open': [...],
  'Volume': [...]
}
MSFT{
  'Adj Close': [...],
  'Close': [...],
  'Date': [...],
  'High': [...],
  'Low': [...],
  'Open': [...],
  'Volume': [...]
}
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

## TODO/Future Updates
- ``Historical Data - In Progress (install from clone to use pre-alpha version)``
- ``Better Error Handling - After Historical Data is in package release``
- ``Add Documentation - Will attempt to do this periodically untill full docs are complete. Any assistance on this would be great :)``

## Requirements

    requests

## Feedback, Issues, and Features:
### Feedback
I'd love to get some feedback from users. I want to know how you are using InVaIN so I can focus on updating it in ways that improve your experience. If you'd like to do so you can email me at *invainapi@gmail.com* **(NOTE: Email abuse will result in your email address being BLOCKED AND/OR REMOVAL OF YOUR ACCESS to InVaIN's data retrieval services)** <br/>
In that vien, I just wanted to outline some guidelines for submitting issues on github.

### Bugs
If you experience any bugs when running the package please submit an issue with a description of the issue. Bugs will take priority over all other issues. 

### Bad Data
If you experience any problems with returned data please create an issue and include:
- ``Code related to creating, modifiying, and accessing the InVaIN API object``
- ``Data Returned``
- ``Day and Approximate Time of Access``

This will allow me to better identify what is causing the issue. If you'd rather not post this information on github, please email it to the email listed in the feedback section.

### New Features
Please don't hesitate to ask for new features you'd like to see or make suggestions for improvements. You can open an issue here on github and I'll take a look at it as soon as I can.
