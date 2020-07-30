import pandas as pd
from scipy import stats

df = pd.read_csv('blood_pressure.csv', delimiter=';')
df[['bp_before', 'bp_after']].describe()

ttest, pval = stats.ttest_rel(df['bp_before'], df['bp_after'])
print('t-hitung: %0.4f, p-value: %0.4f' % (ttest, pval))

if pval <= 0.05:
    print('reject null hypothesis')
else:
    print('fail to reject null hypothesis')