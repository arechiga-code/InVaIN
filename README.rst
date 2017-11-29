=============
InVaIN
=============

Python module to get stock data from YAHOO! Finance


Install
-------

From PyPI with pip:

.. code:: bash

    $ pip install InVaIN

Usage examples
--------------

Get shares data
^^^^^^^^^^^^^^^

Example: Yahoo! Inc. (``YHOO``)

.. code:: python

    >>> import InVaIN import Share
    >>> tickers = ['AAPL','GOOG','MSFT']
    >>> api = InVain(tickers)
    >>> print api.get_price_string()
    '173.07, 1047.41, 84.88'

.. code:: python 

    >>> api = InVaIN()
    >>> api.add_tickers(['AAPL','GOOG', 'MSFT']);
    >>> prices = api.get_prices();
    >>> for stock in prices:
    >>>   print (stock, prices[stock]);
    'AAPL 173.07'
    'GOOG 1047.41'
    'MSFT 84.88'
Available methods

- ``get_prices()``
- ``get_price_string()``
- ``add_ticker()``
- ``add_tickers()``
- ``remove_ticker()``
- ``get_tickers()``

Requirements
------------
requests