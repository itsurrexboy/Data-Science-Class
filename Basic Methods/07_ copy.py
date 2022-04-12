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
i = list(math).index(maxMark)
x_ar = np.arange(i)
w = 0.2
m1 = cds[i]
m2 = math[i]
m3 = os[i]
m4 = csa[i]
m5 = dbe[i]
plt.bar(x_ar,m1, width=w, label = 'CDS')
plt.bar(x_ar+w,m2, width=w,label = 'MATH')
plt.bar(x_ar+w*2, m3, width=w, label = 'OS')
plt.bar(x_ar+w*3, m4, width=w, label ='CSA') 
plt.bar(x_ar+w*4, m5, width=w, label = 'DBE')
plt.xticks(x_ar)
plt.xlabel('Name')
plt.ylabel('Marks')
plt.legend()
plt.show()