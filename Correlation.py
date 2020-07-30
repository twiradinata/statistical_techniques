'''
Contoh Solusi menggunakan Python untuk Korelasi Pearson
'''
import numpy as np
from scipy.stats import pearsonr

# Tabulate the data
sales_call = [20, 40, 20, 30, 10, 10, 20, 20, 20, 30]
copier_sold = [30, 60, 40, 60, 30, 40, 40, 50, 30, 70]

# Descriptive Statistics
print('Rata-rata sales call:', np.mean(sales_call))
print('Rata-rata copier sold:', np.mean(copier_sold))

# Correlation
corCoef, pvalue = pearsonr(sales_call, copier_sold)
print('Correlation Coefficient = %0.4f' % (corCoef)) 
print('P-Value = %0.4f' % (pvalue))

if pvalue <= 0.05:
    print('Korelasi Signifikan')
else:
    print('Korelasi Tidak Signifikan')