#### WIP ####

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy.stats import chi2_contingency
from itertools import combinations


#Load Dataset 
data = pd.read_csv('middle_students_new.csv')

data_if1 = data[['school', 'sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','nursery','internet','guardian_por','traveltime_por',
      'famsup_por','paid_por']]

data_if1 = data_if1.dropna()

alpha = 0.05

#create variable pair generator
variable_names = data_if1.columns
variable_pairs = combinations(variable_names,2)
variable_pair_storage = [i for i in variable_pairs]
#print(variable_pair_storage)

#restart generator
variable_pairs = combinations(variable_names,2)

#to store associated or not_associated
associated = {}
not_associated = {}

#run chi2 through all the variable pairs
for pair in variable_pairs:
    # create a contingency table for the variable pair
    var_1 = data_if1[pair[0]].unique()
    var_2 = data_if1[pair[1]].unique()
    table = np.zeros((len(var_1), len(var_2)))
    for i in range(data_if1.shape[0]):
        row = np.where(var_1 == data_if1.loc[i, pair[0]])[0][0]
        col = np.where(var_2 == data_if1.loc[i, pair[1]])[0][0]
        table[row, col] += 1
    # perform chi-square test
    chi2, p, dof, expected = chi2_contingency(table)
    
    critical_value = scipy.stats.chi2.ppf(1-alpha,dof)
    
    if chi2 > critical_value:
        print(f"{pair[0]} and {pair[1]} are associated")
        if pair[0] not in associated:
            associated[pair[0]] = [pair[1]]
        else:
            associated[pair[0]].append(pair[1])
    else:
        print(f"{pair[0]} and {pair[1]} are not associated")
        if pair[0] not in not_associated:
            not_associated[pair[0]] = [pair[1]]
        else:
            not_associated[pair[0]].append(pair[1])



