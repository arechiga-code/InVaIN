# InVaIN

Python module to get stock data from YAHOO! Finance

### Install

From PyPI with pip:

```bash
$ pip install InVaIN
```
Code Examples
--------------

Example: Apple Inc. (``AAPL``)

``` python   
from InVaIN import InVaIN   
api = InVaIN('AAPL')        
print api.get_price_string()
*'173.07'*
```
Example: Apple Inc. (``AAPL``), Alphabet Inc. (``GOOG``), Microsoft Inc. (``MSFT``), 

```python
from InVaIN import InVaIN
api = InVaIN()
api.add_tickers(['AAPL','GOOG', 'MSFT']);
prices = api.get_prices();
for stock in prices:
   print (stock, prices[stock]);
*'AAPL 173.07'
*'GOOG 1047.41'*
*'MSFT 84.88'*
```

Available methods

- ``get_prices()``
- ``get_price_string()``
- ``add_ticker()``
- ``add_tickers()``
- ``remove_ticker()``
- ``get_tickers()``

**More to Come**

## Requirements

    requests
