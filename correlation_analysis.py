<<<<<<< HEAD
#Correlation Analysis

import os

os.chdir('C:/Users/geneh/ntu-msds-sd6101/artifacts')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset - Higher Education Students
data = pd.read_csv('higher_edu_student_new.csv')
data = data.drop('Unnamed: 0', axis = 1)

#Correlation
corr_matrix = data.corr()

#Data Viz
fig , ax = plt.subplots(figsize=(30,20))
sns.heatmap(corr_matrix, annot=True, ax=ax)
plt.show()

=======
#Correlation Analysis

import os

os.chdir('C:/Users/geneh/ntu-msds-sd6101/artifacts')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load Dataset - Higher Education Students
data = pd.read_csv('higher_edu_student_new.csv')
data = data.drop('Unnamed: 0', axis = 1)

#Correlation
corr_matrix = data.corr()

#Data Viz
fig , ax = plt.subplots(figsize=(30,20))
sns.heatmap(corr_matrix, annot=True, ax=ax)
plt.show()

>>>>>>> 85c265b67d24aab3acdeaf089ea6e5cca5d48728
