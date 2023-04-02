#### Independent Features Group 1 ###

import os

os.chdir("C:/Users/geneh/ntu-msds-sd6101/artifacts")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy.stats import chi2_contingency
from itertools import combinations

### Categorical ###
#Load Dataset 
data = pd.read_csv('middle_students_new.csv')

data_if1 = data[['school', 'sex','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','nursery','internet','guardian_por','traveltime_por',
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
associated = {} #reject null hypothesis
not_associated = {} #cannot reject null hypothesis

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

print('ASSOCIATED INDEPENDENT VARIABLE 1')
for i in associated:
    print(i, associated[i])

print('NOT ASSOCIATED INDEPENDENT VARIABLE 1')
for j in not_associated:
    print(j, not_associated[j])

### Categorical and Continuous (AGE) ###

### ANOVA ###

age_associated = {}
age_not_associated = {}

import statsmodels.api as sm
from statsmodels.formula.api import ols

variable2_pair_storage = []
for categorical in data_if1.columns:
    variable2_pair_storage.append(('age',categorical))

for pair in variable2_pair_storage:
    model = ols(str(pair[0]) + '~' + str(pair[1]), data=data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    if anova_table['PR(>F)'][0] < alpha:
        if pair[0] not in age_associated:
            age_associated[pair[0]] = [pair[1]]
        else:
            age_associated[pair[0]].append(pair[1])
        print(f"The {pair[0]} of students varies significantly in the different {pair[1]}.")
    else:
        if pair[0] not in age_not_associated:
            age_not_associated[pair[0]] = [pair[1]]
        else:
            age_not_associated[pair[0]].append(pair[1])
        print(f"The {pair[0]} of students do not varies significantly in the different {pair[1]}.")

print('INDEPENDENT VARIABLE 1 ASSOCIATED WITH AGE')
for i in age_associated:
    print(i, age_associated[i])

print('INDEPENDENT VARIABLE 1 NOT ASSOCIATED WITH AGE')
for j in age_not_associated:
    print(j, age_not_associated[j])
    
### Graph as node and edges ###

merged_associated = associated | age_associated

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

G = nx.Graph()

# add nodes to the graph
for node in merged_associated.keys():
    G.add_node(node)

# add edges to the graph
for node, neighbors in merged_associated.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

# show the graph
plt.show()
