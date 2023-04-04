<<<<<<< HEAD
'''
Reference : https://www.analyticsvidhya.com/blog/2020/10/feature-selection-techniques-in-machine-learning/
'''
#Randomforest 

import os

os.chdir('C:/Users/geneh/ntu-msds-sd6101/artifacts')

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
#from sklearn.preprocessing import StandardScaler, normalize
import matplotlib.pyplot as plt

#Load Dataset - Higher Education Students
data = pd.read_csv('higher_edu_student_new.csv')

#Get X and Y
X = data.drop(['Grade','Unnamed: 0'], axis = 1)
Y = data['Grade']

#Construct Model
model = RandomForestClassifier(n_estimators=300)
model.fit(X,Y)

#Extract important features
importances = model.feature_importances_
df_vis = pd.DataFrame({"Features": pd.DataFrame(X).columns, "Importances": importances * 100})
df_vis.index += 1
df_vis = df_vis.sort_values('Importances')

#Data visualisation
fig = plt.figure(figsize=(40,10))
plt.bar(df_vis['Features'], df_vis['Importances'])
plt.show()


'''
Without Norms; the higher the importances, the more significant and important is the random variable

           Features  Importances
24    Preparation.1     1.122072
14         Parental     1.217101
20       Attendance     1.732602
22     Attendance.1     1.794189
21           Impact     1.870598
5        Additional     1.890526
7                Do     2.385782
9    Transportation     2.420693
6           Regular     2.447586
27       Discussion     2.451982
3         Graduated     2.539096
19        Reading.1     2.607568
23      Preparation     2.619253
15     Mothersâ€™.1     2.692721
25           Taking     2.916493
18          Reading     2.930415
10    Accommodation     2.957740
2               Sex     2.963060
1           Student     3.166728
8             Total     3.178951
4       Scholarship     3.343596
28  Flip-classroom:     3.395741
26        Listening     3.583241
17           Weekly     3.987622
30         Expected     4.017824
12       Fathersâ€™     4.346406
11       Mothersâ€™     4.532409
13           Number     4.698321
16     Fathersâ€™.1     5.015583
29       Cumulative     6.999472
31        Course_id     8.174630
=======
'''
Reference : https://www.analyticsvidhya.com/blog/2020/10/feature-selection-techniques-in-machine-learning/
'''
#Randomforest 

import os

os.chdir('C:/Users/geneh/ntu-msds-sd6101/artifacts')

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
#from sklearn.preprocessing import StandardScaler, normalize
import matplotlib.pyplot as plt

#Load Dataset - Higher Education Students
data = pd.read_csv('higher_edu_student_new.csv')

#Get X and Y
X = data.drop(['Grade','Unnamed: 0'], axis = 1)
Y = data['Grade']

#Construct Model
model = RandomForestClassifier(n_estimators=300)
model.fit(X,Y)

#Extract important features
importances = model.feature_importances_
df_vis = pd.DataFrame({"Features": pd.DataFrame(X).columns, "Importances": importances * 100})
df_vis.index += 1
df_vis = df_vis.sort_values('Importances')

#Data visualisation
fig = plt.figure(figsize=(40,10))
plt.bar(df_vis['Features'], df_vis['Importances'])
plt.show()


'''
Without Norms; the higher the importances, the more significant and important is the random variable

           Features  Importances
24    Preparation.1     1.122072
14         Parental     1.217101
20       Attendance     1.732602
22     Attendance.1     1.794189
21           Impact     1.870598
5        Additional     1.890526
7                Do     2.385782
9    Transportation     2.420693
6           Regular     2.447586
27       Discussion     2.451982
3         Graduated     2.539096
19        Reading.1     2.607568
23      Preparation     2.619253
15     Mothersâ€™.1     2.692721
25           Taking     2.916493
18          Reading     2.930415
10    Accommodation     2.957740
2               Sex     2.963060
1           Student     3.166728
8             Total     3.178951
4       Scholarship     3.343596
28  Flip-classroom:     3.395741
26        Listening     3.583241
17           Weekly     3.987622
30         Expected     4.017824
12       Fathersâ€™     4.346406
11       Mothersâ€™     4.532409
13           Number     4.698321
16     Fathersâ€™.1     5.015583
29       Cumulative     6.999472
31        Course_id     8.174630
>>>>>>> 85c265b67d24aab3acdeaf089ea6e5cca5d48728
'''