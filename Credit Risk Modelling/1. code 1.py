# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 13:31:55 2021

@author: redhw
"""


import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from statsmodels.api import OLS


os.getcwd()

os.chdir('C:/Users/redhw/OneDrive/Documents/GitHub/Python-Code-Testing/Credit Risk Modelling')

candy = pd.read_excel('candy-data.xlsx')

candy.columns.values

model = LinearRegression().fit(candy['winpercent'].values.reshape(-1,1), candy['chocolate'])

OLS(candy['winpercent'],candy[['chocolate','fruity']]).fit().summary()

import pandas as pd
import numpy as np


# dummy data as example
age = ['18 to 25','26 to 35','36 to 45','46 to 60','>= 60']
df = pd.DataFrame(age, columns=['Age Group'])
df['counts'] = [31234, 30293, 29384, 30192, 27394]
df['bad'] = [4920, 4123, 3784, 2608, 1479]
df['good'] = df.counts - df.bad

# calculate WOE
df['total_distri'] = df.counts/sum(df.counts)
df['bad_distri'] = df.bad/sum(df.bad)
df['good_distri'] = df.good/sum(df.good)
df['WOE'] = np.log(df.good_distri / df.bad_distri)
df['WOE%'] = df.WOE * 100


# on page 62