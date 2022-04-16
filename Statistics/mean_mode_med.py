#Showing Mean, Mode and Median using NumPy and Statistics Module.
import numpy as np
import statistics as stc

data = [1,5,32,52,6,1,3,6,2]
print("Mean - ",np.mean(data)) #mean
print("Mode - ",stc.mode(data)) #mode using statistics module
print("Median - ",np.median(data)) #median