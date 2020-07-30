from scipy.stats import ttest_ind

schadek = [235, 210, 231, 242, 205, 230, 231, 210, 225, 249]
bowyer = [228, 205, 219, 240, 198, 223, 227, 215, 222, 245]

ttest, pval = ttest_ind(schadek, bowyer)
print('t-hitung: %0.4f, p-value: %0.4f' % (ttest, pval))

if pval <= 0.05:
    print("we reject null hypothesis")
else:
    print("fail to reject null hypothesis")
