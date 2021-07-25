# -*- coding: utf-8 -*-
"""
Created on Sat May 22 12:55:41 2021

@author: redhw
"""
import os
import pandas as pd
import numpy as np

pd.options.display.max_columns = 10
pd.options.display.max_rows = 10

os.getcwd()

os.chdir('C:/Users/redhw/OneDrive/Documents/GitHub/Python-Code-Testing/Case Study Amsterdam Trading Bank/cup98lrn')

os.getcwd()

LearningData = pd.read_csv('cup98LRN.txt', sep = ',')
TitleMapping = pd.read_csv('TitleMapping.csv', sep = ',')


print(LearningData)

LearningData.describe(include='all')

print(LearningData.columns.values)

LearningData['ODATEDW'].value_counts()

LearningData.to_csv('LearningData.csv')

LearningData.head()

LearningData['MDMAUD']

pd.set_option('display.max_rows',1000)
pd.set_option('display.max_rows',0)

TempData1 = LearningData.MDMAUD.value_counts()
print(TempData1)
TempData2 = LearningData.ETH1.value_counts()
print(TempData2)

LearningData['RedhwanVariable'] = 'Redhwan'

LearningData[['MDMAUD','MDMAUD_R', 'MDMAUD_F', 'MDMAUD_A']]

LearningData.loc[LearningData['MDMAUD_R'] == 'C']

LearningData['RedTest'] = np.where(LearningData['MDMAUD_R'] == 'C',1,0)

