#07 plot chart of the student having maximum mark in math
import numpy as np
import matplotlib.pyplot as plt

students = ['Manas', 'Pramod', 'Trishul', 'Sai']
cds = np.array([89, 82, 69, 72])
math = np.array([79, 88, 82, 75])
os = np.array([68, 63, 71, 75])
csa = np.array([80, 81, 79, 85])
dbe = np.array([91, 85, 89, 85])

maxMark = max(math)
plt.plot(students, math,'o-')
plt.show()
