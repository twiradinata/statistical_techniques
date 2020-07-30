'''
Contoh Solusi menggunakan Python untuk Regresi Linier
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Tabulate the data
#sales_call = [20, 40, 20, 30, 10, 10, 20, 20, 20, 30]
#copier_sold = [30, 60, 40, 60, 30, 40, 40, 50, 30, 70]
sales_call = [17, 24, 25, 27, 19, 22, 25, 17, 23, 21, 20, 28]
copier_sold = [28, 25, 22, 21, 25, 23, 24, 26, 22, 27, 24, 21]

# Descriptive Statistics
print('Rata-rata sales call:', np.mean(sales_call))
print('Rata-rata copier sold:', np.mean(copier_sold))

# Linear Regression: slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
result = linregress(sales_call, copier_sold)
print('Slope = %0.4f' % result.slope)
print('Intercept = %0.4f' % result.intercept) 
print('Koefisien Korelasi (r) = %0.4f' % result.rvalue)
print('Koefisien Determinasi (r^2) = %0.4f' % result.rvalue**2)
print('P-Value = %0.4f' % result.pvalue)

# Plotting Data Points and Regression Line
line = f'Regression line: y={result.intercept:.2f}+{result.slope:.2f}x, r={result.rvalue:.2f}'
line_value = [i * result.slope for i in sales_call]

fig, ax = plt.subplots()
ax.plot(sales_call, copier_sold, linewidth=0, marker='s', label='Data points')
ax.plot(sales_call, result.intercept + line_value, label=line)
ax.set_xlabel('sales_call')
ax.set_ylabel('copier_sold')
ax.legend(facecolor='white')
plt.show()