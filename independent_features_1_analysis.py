### Independent Features Group 1 - Math ###

#import os

#os.chdir("C:/Users/geneh/ntu-msds-sd6101/artifacts")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy.stats import chi2_contingency
from itertools import combinations
import networkx as nx
import matplotlib.patches as mpatches
from statsmodels.formula.api import ols
import statsmodels.api as sm

### Categorical against Categorical ###

#ref : https://www.scribbr.com/statistics/chi-square-distribution-table/

#Load Dataset 
data = pd.read_csv('middle_students_new.csv')

#Select Indepdentdent Feature 1
data_if1 = data[['school', 'sex','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','nursery','internet','guardian_mat','traveltime_mat',
      'famsup_mat','paid_mat', 'age']]

#Drop empty entries and reset index
data_if1 = data_if1.dropna()
data_if1 = data_if1.reset_index(drop=True)

#Set alpha
alpha = 0.05

#create variable pair generator
variable_names = data_if1.columns.drop('age')
variable_pairs = combinations(variable_names,2)
variable_pair_storage = [i for i in variable_pairs]


#to store associated or not_associated
associated = [] #reject null hypothesis
not_associated = [] #cannot reject null hypothesis

#run chi2 through all the variable pairs, left tail test
for pair in variable_pair_storage:
    var_1 = data_if1[pair[0]].unique()
    var_2 = data_if1[pair[1]].unique()
    table = np.zeros((len(var_1), len(var_2)))
    for i in range(data_if1.shape[0]):
        row = np.where(var_1 == data_if1.loc[i, pair[0]])[0][0]
        col = np.where(var_2 == data_if1.loc[i, pair[1]])[0][0]
        table[row, col] += 1

    chi2, p, dof, expected = chi2_contingency(table)
    
    critical_value = scipy.stats.chi2.ppf(1-alpha,dof)
    
    if chi2 > critical_value:
        print(f"{pair[0]} & {pair[1]} are associated, chi2: {chi2:.2f}, p_value: {p:.4f}, critical_value: {critical_value:.2f}")
        associated.append([(pair[0], pair[1]), chi2, p])
    else:
        print(f"{pair[0]} & {pair[1]} are not associated, chi2: {chi2:.2f}, p_value: {p:.4f}, critical_value: {critical_value:.2f}")
        not_associated.append([(pair[0], pair[1]), chi2, p])

### Categorical and Continuous, AGE only ###

### ANOVA ###

#to store associated or not_associated with age
age_associated = []
age_not_associated = []

#create age-variable pair generator
variable2_pair_storage = []
for categorical in data_if1.columns:
    variable2_pair_storage.append(('age',categorical))

#run ANOVA through age-variable pair
for pair in variable2_pair_storage[:-1]:
    model = ols(str(pair[0]) + '~' + str(pair[1]), data=data_if1).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    if anova_table['PR(>F)'][0] < alpha:
        age_associated.append([pair[0], pair[1], anova_table['PR(>F)'][0]])
        print(f"({pair[0]},{pair[1]}) varies significantly, p_value: {anova_table['PR(>F)'][0]:.7f}")
    else:
        age_not_associated.append([pair[0], pair[1], anova_table['PR(>F)'][0]])
        print(f"({pair[0]},{pair[1]}) varies insignificantly, p_value: {anova_table['PR(>F)'][0]:.7f}")

'''
### Visualise as Grade, represented by node and edges ###

#merge chi2 outcome with anova outcome, that are associated
merged_associated = associated | age_associated

#Initialise graph
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
'''