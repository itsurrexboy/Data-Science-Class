#06 Take some values of student mark using array and plot the total mark of the students
import numpy as np
import matplotlib.pyplot as plt

students = ['Manas', 'Pramod', 'Trishul', 'Sai']
cds = np.array([89, 82, 69, 72])
math = np.array([79, 88, 82, 75])
os = np.array([68, 63, 71, 75])
csa = np.array([80, 81, 79, 85])
dbe = np.array([91, 85, 89, 85])
total_mark = cds + math + os + csa + dbe

#plotting bar graph
plt.bar(students, total_mark,width=0.4)
plt.title("Student's Mark")
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()
