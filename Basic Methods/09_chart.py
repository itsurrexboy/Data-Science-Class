#09 draw a chart of 5 employee salary
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('employee.csv')
emp_name = data['emp_name']
sal = data['salary']
plt.plot(emp_name, sal,'o-')
plt.xlabel('Employee Name')
plt.ylabel('Salary')
plt.title('Salary of Employees')
plt.show()