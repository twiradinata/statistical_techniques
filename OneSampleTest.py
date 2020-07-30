from scipy.stats import ttest_1samp
import numpy as np

ages = np.genfromtxt('ages.csv',delimiter=',')
print(ages)
ages_mean = np.mean(ages)
print('Rata-rata usia: %0.2f' % ages_mean)

ttest, pval = ttest_1samp(ages, 30)
print('t-hitung: %0.4f' % ttest)
print('p-values: %0.4f' % pval)

if pval <= 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
    print("fail to reject null hypothesis")