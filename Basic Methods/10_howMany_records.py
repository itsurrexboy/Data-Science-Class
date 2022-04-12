#10 from a file find how many records are available

import pandas as pd

data = pd.read_csv('employee.csv')
print(data)
print('Number of records available - ', len(data))