#### G3 against Independent Features Group 1 Categorical Variables - Math ###

#import os

#os.chdir("C:/Users/geneh/ntu-msds-sd6101/artifacts")

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import pearsonr, t


data = pd.read_csv('middle_students_new.csv')

#Select Indepdentdent Feature 1
data = data[['G3_mat', 'school', 'sex','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','nursery','internet','guardian_por','traveltime_por',
      'famsup_por','paid_por','age']]

#Drop empty entries and reset index
data = data.dropna()
data = data.reset_index(drop=True)


### Anova ###
### - G3 (continous) against Categorical 

### Database to store outcome ###
G3_associated = []
G3_not_associated = []

alpha = 0.05

G3_indep_var_pair_storage = []
for categorical in data.columns.drop(['G3_mat', 'age']):
    G3_indep_var_pair_storage.append(('G3_mat',categorical))

for pair in G3_indep_var_pair_storage:
    model = ols(str(pair[0]) + '~' + str(pair[1]), data=data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    if anova_table['PR(>F)'][0] < alpha:
        G3_associated.append([pair[0], pair[1], anova_table['PR(>F)'][0], alpha])
        print(f"({pair[0]},{pair[1]}) varies significantly, p_value: {anova_table['PR(>F)'][0]:.4f}, alpha: {alpha}")
    else:
        G3_not_associated.append([pair[0], pair[1], anova_table['PR(>F)'][0], alpha])
        print(f"({pair[0]},{pair[1]}) varies insignificantly, p_value: {anova_table['PR(>F)'][0]:.4f}, alpha: {alpha}")

### Pearson correlation coefficient Analaysis ###

### - G3 (continous) against continous (age)

#Reference: https://www.scribbr.com/statistics/pearson-correlation-coefficient/

G3_associated_pearson = []
G3_not_associated_pearson = []

ccoef, p_value = pearsonr(data['G3_mat'], data['age'])
n = len(data)
df_c = n-2
critical_value = t.ppf(1-alpha, df_c)

t_value = ccoef * (n - 2) ** 0.5 / ((1 - ccoef ** 2) ** 0.5)

if abs(t_value) > critical_value:
    G3_associated_pearson.append(['G3_mat', 'age', t_value, critical_value])
    print(f"(G3_mat,age) varies significantly, t_value: {anova_table['PR(>F)'][0]:.4f}, t*: {critical_value:.4f}")
    #print('Reject Null Hypothesis, there is statistical significant correlationship between G3 and Age')
else:
    G3_not_associated_pearson.append(['G3_mat', 'age', t_value, critical_value])
    #print('Accept Null Hypothesis, there is no statistical significant correlationship between G3 and Age')
    print(f"(G3_mat,age) varies insignificantly, t_value: {anova_table['PR(>F)'][0]:.4f}, t*: {critical_value:.4f}")











    
