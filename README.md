# [tushare](https://www.bitfinex.com/) [MooQuant](http://gbeced.github.io/pyalgotrade/) Module

This is a very early version of the module. **Live trading is not yet implemented.** Right now, I have only implemented LiveFeed (extends ```barfeed.BaseBarFeed```). Live data is fetched from the trades and order book API endpoint of tushare. Hopefully in the near future, a live broker class will be implemented.

The LiveFeed class can be plugged just as any other bar feed in MooQuant. To subscribe for bid and ask prices, just call ```getOrderBookUpdateEvent().subscribe(<your_callback_function>)``` from the LiveFeed instance. Kindly see example at sample.py.

Liked my work? **Leave me a tip @ 32dzQMkn4RgChSFzemwdYyKJ85PcsVmP6e**

Sample dump:
```
2015-08-10 07:56:02,672 strategy [INFO] Order book updated. Best bid: 265.83. Best ask: 265.89
2015-08-10 07:56:10,800 strategy [INFO] Order book updated. Best bid: 265.83. Best ask: 265.93
2015-08-10 07:56:24,272 strategy [INFO] Order book updated. Best bid: 265.83. Best ask: 265.94
2015-08-10 07:56:29,269 strategy [INFO] Price: 265.91. Volume: 0.94.
2015-08-10 07:56:33,044 strategy [INFO] Order book updated. Best bid: 265.83. Best ask: 265.92
2015-08-10 07:56:43,051 strategy [INFO] Order book updated. Best bid: 265.65. Best ask: 265.8
2015-08-10 07:56:48,124 strategy [INFO] Price: 265.83. Volume: 2.91549425.
2015-08-10 07:56:48,125 strategy [INFO] Price: 265.83. Volume: 0.419.
2015-08-10 07:56:48,125 strategy [INFO] Price: 265.83. Volume: 0.38.
2015-08-10 07:56:48,125 strategy [INFO] Exit signal. Sell at 265.65
2015-08-10 07:56:48,126 strategy [INFO] Position closed at 265.83
2015-08-10 07:56:48,126 strategy [INFO] Price: 265.83. Volume: 0.634.
2015-08-10 07:56:48,126 strategy [INFO] Price: 265.83. Volume: 0.397.
2015-08-10 07:56:48,127 strategy [INFO] Price: 265.83. Volume: 0.38.
2015-08-10 07:56:48,127 strategy [INFO] Price: 265.83. Volume: 0.424.
2015-08-10 07:56:48,127 strategy [INFO] Price: 265.83. Volume: 7.6751.
2015-08-10 07:56:48,127 strategy [INFO] Price: 265.82. Volume: 0.377.
2015-08-10 07:56:48,127 strategy [INFO] Price: 265.82. Volume: 0.376.
2015-08-10 07:56:48,128 strategy [INFO] Price: 265.78. Volume: 0.07.
2015-08-10 07:56:51,492 strategy [INFO] Order book updated. Best bid: 265.66. Best ask: 265.78
2015-08-10 07:56:59,802 strategy [INFO] Order book updated. Best bid: 265.66. Best ask: 265.79
2015-08-10 07:57:16,524 strategy [INFO] Order book updated. Best bid: 265.68. Best ask: 265.79
2015-08-10 07:57:21,770 strategy [INFO] Price: 265.79. Volume: 0.79.
2015-08-10 07:57:24,932 strategy [INFO] Order book updated. Best bid: 265.71. Best ask: 265.79
2015-08-10 07:57:33,249 strategy [INFO] Order book updated. Best bid: 265.76. Best ask: 265.79
2015-08-10 07:57:41,749 strategy [INFO] Order book updated. Best bid: 265.78. Best ask: 265.79
2015-08-10 07:58:30,414 strategy [INFO] Price: 265.79. Volume: 0.010227.
2015-08-10 07:58:30,415 strategy [INFO] Price: 265.79. Volume: 0.375861.
```

This is based on Bitstamp and Xignite module of MooQuant.
# pyalgotrade_bitfinex
# pyalgotrade_tushare
