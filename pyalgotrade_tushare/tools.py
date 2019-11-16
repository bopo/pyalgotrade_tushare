# -*- coding: utf-8 -*-
# PyAlgoTrade tushare module
#
# Copyright 2017 bopo.wang<ibopo@126.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: bopo.wang <ibopo@126.com>
"""

import datetime
import os
from pathlib import Path

import pandas as pd
import pyalgotrade.logger
import tushare as ts
from pyalgotrade import bar
from pyalgotrade_tushare import barfeed


def download_bars(instrument, begin, end):
    return ts.get_k_data(instrument, start=begin, end=end, ktype='D',
                  index=False, retry_count=3, pause=0.001)


def download_daily_bars(instrument, year, csvFile):
    """Download daily bars from Tushare Library for a given year.

    :param instrument: Instrument identifier.
    :type instrument: string.
    :param year: The year.
    :type year: int.
    :param csvFile: The path to the CSV file to write.
    :type csvFile: string.
    """

    begin = datetime.date(year, 1, 1).strftime('%Y-%m-%d')
    end = datetime.date(year, 12, 31).strftime('%Y-%m-%d')
    bars = download_bars(instrument, begin, end)

    if len(bars) > 0:
        bars = bars.drop(['code'], axis=1)
        bars.columns = ['Date', 'Open', 'Close', 'High', 'Low', 'Volume']
        bars.to_csv(csvFile, encoding='utf-8', index=False)


def build_feed(instruments, fromYear, toYear, storage, frequency=bar.Frequency.DAY, skipErrors=False):
    """Build and load a :class:`pyalgotrade.barfeed.tusharefeed.Feed` using CSV files downloaded from Tushare Library.
    CSV files are downloaded if they haven't been downloaded before.

    :param instruments: Instrument identifiers.
    :type instruments: list.
    :param fromYear: The first year.
    :type fromYear: int.
    :param toYear: The last year.
    :type toYear: int.
    :param storage: The path were the files will be loaded from, or downloaded to.
    :type storage: string.
    :param frequency: The frequency of the bars. Only **pyalgotrade.bar.Frequency.DAY** is currently supported.
    :param skipErrors: True to keep on loading/downloading files in case of errors.
    :type skipErrors: boolean.
    :rtype: :class:`pyalgotrade.barfeed.tusharefeed.Feed`.
    """

    logger = pyalgotrade.logger.getLogger("tushare")
    ret = barfeed.Feed(frequency)

    if not os.path.exists(storage):
        logger.info("Creating {dirname} directory".format(dirname=storage))
        os.mkdir(storage)

    for year in range(fromYear, toYear + 1):
        for instrument in instruments:
            filePath = Path(storage) 
            fileName = filePath / "{instrument}-{year}-tushare.csv".format(
                    instrument=instrument, year=year)

            if not os.path.exists(fileName):
                logger.info(
                    "Downloading {instrument} {year} to {filename}".format(
                        instrument=instrument, year=year, filename=fileName))
                try:
                    if frequency == bar.Frequency.DAY:
                        download_daily_bars(instrument, year, fileName)
                    else:
                        raise Exception("Invalid frequency")
                except Exception as e:
                    if skipErrors:
                        logger.error(str(e))
                        continue
                    else:
                        raise e

            ret.addBarsFromCSV(instrument, fileName)

    return ret
