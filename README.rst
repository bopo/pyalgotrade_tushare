PyAlgoTrade tushare module
==============================

.. image:: https://img.shields.io/pypi/v/pyalgotrade_tushare.svg
        :target: https://pypi.python.org/pypi/pyalgotrade_tushare

.. image:: https://img.shields.io/travis/bopo/pyalgotrade_tushare.svg
        :target: https://travis-ci.org/bopo/pyalgotrade_tushare

.. image:: https://readthedocs.org/projects/pyalgotrade_tushare/badge/?version=latest
        :target: https://pyalgotrade_tushare.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/bopo/pyalgotrade_tushare/shield.svg
     :target: https://pyup.io/repos/github/bopo/pyalgotrade_tushare/
     :alt: Updates



* 开源协议: MIT license
* 在线文档: https://pyalgotrade_tushare.readthedocs.io.

安装方法
--------

::

	# PIP 自动安装方法
	pip install pyalgotrade_tushare

	# 手动下载源码安装
	git clone https://github.com/bopo/pyalgotrade_tushare.git 
	cd pyalgotrade_tushare
	python setup.py install


使用说明
--------

不多话，简单一个例子

::

	from pyalgotrade import plotter, strategy
	from pyalgotrade.stratanalyzer import sharpe
	from pyalgotrade.technical import ma

	from pyalgotrade_tushare import tools


	class MyStrategy(strategy.BacktestingStrategy):
	    def __init__(self, feed, instrument):
	        super().__init__(feed)

	        self.__position = None
	        self.__sma = ma.SMA(feed[instrument].getCloseDataSeries(), 150)
	        self.__instrument = instrument
	        self.getBroker()

	    def onEnterOk(self, position):
	        execInfo = position.getEntryOrder().getExecutionInfo()
	        self.info("买入 %.2f" % (execInfo.getPrice()))

	    def onEnterCanceled(self, position):
	        self.__position = None

	    def onExitOk(self, position):
	        execInfo = position.getExitOrder().getExecutionInfo()
	        self.info("卖出 %.2f" % (execInfo.getPrice()))
	        self.__position = None

	    def onExitCanceled(self, position):
	        # If the exit was canceled, re-submit it.
	        self.__position.exitMarket()

	    def getSMA(self):
	        return self.__sma

	    def onBars(self, bars):
	        # 每一个数据都会抵达这里，就像becktest中的next
	        # Wait for enough bars to be available to calculate a SMA.
	        if self.__sma[-1] is None:
	            return

	        # bar.getTyoicalPrice = (bar.getHigh() + bar.getLow() + bar.getClose())/ 3.0
	        bar = bars[self.__instrument]

	        # If a position was not opened, check if we should enter a long position.
	        if self.__position is None:
	            if bar.getPrice() > self.__sma[-1]:
	                # 开多头.
	                self.__position = self.enterLong(self.__instrument, 100, True)

	        # 平掉多头头寸.
	        elif bar.getPrice() < self.__sma[-1] and not self.__position.exitActive():
	            self.__position.exitMarket()


	if __name__ == '__main__':
	    instruments = ["600036"]

	    feeds = tools.build_feed(instruments, 2013, 2018, "histdata")

	    # 3.实例化策略
	    strat = MyStrategy(feeds, instruments[0])

	    # 4.设置指标和绘图
	    ratio = sharpe.SharpeRatio()
	    strat.attachAnalyzer(ratio)
	    plter = plotter.StrategyPlotter(strat)

	    # 5.运行策略
	    strat.run()
	    strat.info("最终收益: %.2f" % strat.getResult())

	    # 6.输出夏普率、绘图
	    strat.info("夏普比率: " + str(ratio.getSharpeRatio(0)))
	    plter.plot()




版本更新
--------
* 修改了 PIP 安装程序问题
* 本程序只支持 python3.

贡献名单
---------

- bopo.wang

