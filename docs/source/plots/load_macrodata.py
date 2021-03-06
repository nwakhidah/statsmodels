import pandas as pd

import statsmodels.api as sm

dta = sm.datasets.macrodata.load_pandas().data
dates = sm.tsa.datetools.dates_from_range('1959Q1', '2009Q3')
index = pd.DatetimeIndex(dates)
dta.set_index(index, inplace=True)
