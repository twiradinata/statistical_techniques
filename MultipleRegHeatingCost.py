'''
Contoh Solusi menggunakan Python untuk Multiple Regression
'''
import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm

heating = {'house_no': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
           'heating_cost': [250,360,165,43,92,200,355,290,230,120,73,205,400,320,72,272,94,190,235,139],
           'temperature': [35,29,36,60,65,30,10,7,21,55,54,48,20,39,60,20,58,40,27,30],
           'insulation': [3,4,7,6,5,5,6,10,9,2,12,5,5,4,8,5,7,8,9,7],
           'age_of_furnace': [6,10,3,9,6,5,7,10,11,5,4,1,15,7,6,8,3,11,8,5]
          }

df = pd.DataFrame(heating,columns=['house_no','heating_cost','temperature','insulation','age_of_furnace'])

independent_var = df[['temperature','insulation','age_of_furnace']]
dependent_var = df['heating_cost']
 
# Using sklearn to generate intercept and regression coefficients
result = linear_model.LinearRegression()
result.fit(independent_var, dependent_var)

intercept = result.intercept_   # float number
reg_coef = result.coef_         # array of regression coefficients, float numbers

print('Intercept: %0.3f' % intercept)
print('Coefficient b1: %0.3f' % reg_coef[0])
print('Coefficient b2: %0.3f' % reg_coef[1])
print('Coefficient b3: %0.3f' % reg_coef[2])

# using statsmodels to display model summary
X = sm.add_constant(independent_var) # adding a constant
 
model = sm.OLS(dependent_var, X).fit()
predictions = model.predict(X) 
 
print_model = model.summary()
print(print_model)