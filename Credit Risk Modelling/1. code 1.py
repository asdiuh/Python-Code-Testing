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

# up to page 56 now