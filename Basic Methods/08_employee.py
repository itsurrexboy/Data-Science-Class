#08 Take file for employee and find the number of employees and find the person getting salary more than 20000
import pandas as pd

emps = pd.read_csv('employee.csv')
id = emps['emp_id']
name = emps['emp_name']
sal = emps['salary']
print(emps.shape)
#l = list(emps.info())
#print(l)
#print("Total number of Employees are - ", len(emps))
#print('List of Employees having salary more than 20000\n',emps[sal>=20000])