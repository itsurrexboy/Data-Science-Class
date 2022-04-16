#reading data from csv and finding Mean, Mode and Median

import statistics as stc
import pandas as pd

data = pd.read_csv('Cricket_Data_Set.csv')
name = data['Name']
run = data['Runs']
print('The Data - ')
print(data)
print('\nMean - ',stc.mean(run))
print('Mode - ',stc.mode(run))
print('Median - ',stc.median(run))