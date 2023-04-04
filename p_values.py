<<<<<<< HEAD
<<<<<<< HEAD
#p-values

import os

os.chdir('C:/Users/geneh/ntu-msds-sd6101/artifacts')

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import statsmodels.api as sm

#Load Dataset - Higher Education Students
data = pd.read_csv('higher_edu_student_new.csv')

#Get X and Y
X = data.drop(['Grade','Unnamed: 0'], axis = 1)
Y = np.array(data['Grade'])

#Norms
scaler = StandardScaler()
X_norms = scaler.fit_transform(X)
#add beta constant
X_norms = sm.add_constant(X_norms)

#model fit
model = sm.OLS(Y, X_norms).fit()
model.summary()

#extract p_values
p_values = model.summary2().tables[1]['P>|t|']
X_name = np.array(X.columns)
X_name = np.insert(X_name, 0, 'Constant')
df_pvalue = pd.DataFrame({"Features": X_name, "P_values": p_values})
df_pvalue = df_pvalue.sort_values('P_values', ascending=False)

'''

The lower then P_values, the more significant and important of the random variable 

              Features      P_values
x7                  Do  9.845181e-01
x19          Reading.1  9.395244e-01
x12         Fathersâ€™  9.380608e-01
x11         Mothersâ€™  9.344085e-01
x15       Mothersâ€™.1  8.447332e-01
x13             Number  8.028995e-01
x23        Preparation  7.772502e-01
x27         Discussion  7.153327e-01
x6             Regular  6.698715e-01
x22       Attendance.1  5.694502e-01
x30           Expected  5.513802e-01
x14           Parental  5.346943e-01
x28    Flip-classroom:  5.224313e-01
x24      Preparation.1  4.891439e-01
x8               Total  4.006258e-01
x17             Weekly  3.329913e-01
x25             Taking  2.743117e-01
x10      Accommodation  2.393702e-01
x4         Scholarship  1.165901e-01
x16       Fathersâ€™.1  1.108635e-01
x26          Listening  9.235711e-02
x20         Attendance  8.880913e-02
x21             Impact  7.531374e-02
x5          Additional  2.439858e-02
x3           Graduated  2.128536e-02
x9      Transportation  1.366272e-02
x1             Student  7.969091e-03
x18            Reading  4.066648e-03
x29         Cumulative  8.322683e-04
x2                 Sex  2.174488e-04
x31          Course_id  9.635829e-06
const         Constant  1.878028e-43
=======
#p-values

import os

os.chdir('C:/Users/geneh/ntu-msds-sd6101/artifacts')

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import statsmodels.api as sm

#Load Dataset - Higher Education Students
data = pd.read_csv('higher_edu_student_new.csv')

#Get X and Y
X = data.drop(['Grade','Unnamed: 0'], axis = 1)
Y = np.array(data['Grade'])

#Norms
scaler = StandardScaler()
X_norms = scaler.fit_transform(X)
#add beta constant
X_norms = sm.add_constant(X_norms)

#model fit
model = sm.OLS(Y, X_norms).fit()
model.summary()

#extract p_values
p_values = model.summary2().tables[1]['P>|t|']
X_name = np.array(X.columns)
X_name = np.insert(X_name, 0, 'Constant')
df_pvalue = pd.DataFrame({"Features": X_name, "P_values": p_values})
df_pvalue = df_pvalue.sort_values('P_values', ascending=False)

'''

The lower then P_values, the more significant and important of the random variable 

              Features      P_values
x7                  Do  9.845181e-01
x19          Reading.1  9.395244e-01
x12         Fathersâ€™  9.380608e-01
x11         Mothersâ€™  9.344085e-01
x15       Mothersâ€™.1  8.447332e-01
x13             Number  8.028995e-01
x23        Preparation  7.772502e-01
x27         Discussion  7.153327e-01
x6             Regular  6.698715e-01
x22       Attendance.1  5.694502e-01
x30           Expected  5.513802e-01
x14           Parental  5.346943e-01
x28    Flip-classroom:  5.224313e-01
x24      Preparation.1  4.891439e-01
x8               Total  4.006258e-01
x17             Weekly  3.329913e-01
x25             Taking  2.743117e-01
x10      Accommodation  2.393702e-01
x4         Scholarship  1.165901e-01
x16       Fathersâ€™.1  1.108635e-01
x26          Listening  9.235711e-02
x20         Attendance  8.880913e-02
x21             Impact  7.531374e-02
x5          Additional  2.439858e-02
x3           Graduated  2.128536e-02
x9      Transportation  1.366272e-02
x1             Student  7.969091e-03
x18            Reading  4.066648e-03
x29         Cumulative  8.322683e-04
x2                 Sex  2.174488e-04
x31          Course_id  9.635829e-06
const         Constant  1.878028e-43
>>>>>>> 85c265b67d24aab3acdeaf089ea6e5cca5d48728
=======
<<<<<<< HEAD
#p-values

import os

os.chdir('C:/Users/geneh/ntu-msds-sd6101/artifacts')

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import statsmodels.api as sm

#Load Dataset - Higher Education Students
data = pd.read_csv('higher_edu_student_new.csv')

#Get X and Y
X = data.drop(['Grade','Unnamed: 0'], axis = 1)
Y = np.array(data['Grade'])

#Norms
scaler = StandardScaler()
X_norms = scaler.fit_transform(X)
#add beta constant
X_norms = sm.add_constant(X_norms)

#model fit
model = sm.OLS(Y, X_norms).fit()
model.summary()

#extract p_values
p_values = model.summary2().tables[1]['P>|t|']
X_name = np.array(X.columns)
X_name = np.insert(X_name, 0, 'Constant')
df_pvalue = pd.DataFrame({"Features": X_name, "P_values": p_values})
df_pvalue = df_pvalue.sort_values('P_values', ascending=False)

'''

The lower then P_values, the more significant and important of the random variable 

              Features      P_values
x7                  Do  9.845181e-01
x19          Reading.1  9.395244e-01
x12         Fathersâ€™  9.380608e-01
x11         Mothersâ€™  9.344085e-01
x15       Mothersâ€™.1  8.447332e-01
x13             Number  8.028995e-01
x23        Preparation  7.772502e-01
x27         Discussion  7.153327e-01
x6             Regular  6.698715e-01
x22       Attendance.1  5.694502e-01
x30           Expected  5.513802e-01
x14           Parental  5.346943e-01
x28    Flip-classroom:  5.224313e-01
x24      Preparation.1  4.891439e-01
x8               Total  4.006258e-01
x17             Weekly  3.329913e-01
x25             Taking  2.743117e-01
x10      Accommodation  2.393702e-01
x4         Scholarship  1.165901e-01
x16       Fathersâ€™.1  1.108635e-01
x26          Listening  9.235711e-02
x20         Attendance  8.880913e-02
x21             Impact  7.531374e-02
x5          Additional  2.439858e-02
x3           Graduated  2.128536e-02
x9      Transportation  1.366272e-02
x1             Student  7.969091e-03
x18            Reading  4.066648e-03
x29         Cumulative  8.322683e-04
x2                 Sex  2.174488e-04
x31          Course_id  9.635829e-06
const         Constant  1.878028e-43
=======
#p-values

import os

os.chdir('C:/Users/geneh/ntu-msds-sd6101/artifacts')

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import statsmodels.api as sm

#Load Dataset - Higher Education Students
data = pd.read_csv('higher_edu_student_new.csv')

#Get X and Y
X = data.drop(['Grade','Unnamed: 0'], axis = 1)
Y = np.array(data['Grade'])

#Norms
scaler = StandardScaler()
X_norms = scaler.fit_transform(X)
#add beta constant
X_norms = sm.add_constant(X_norms)

#model fit
model = sm.OLS(Y, X_norms).fit()
model.summary()

#extract p_values
p_values = model.summary2().tables[1]['P>|t|']
X_name = np.array(X.columns)
X_name = np.insert(X_name, 0, 'Constant')
df_pvalue = pd.DataFrame({"Features": X_name, "P_values": p_values})
df_pvalue = df_pvalue.sort_values('P_values', ascending=False)

'''

The lower then P_values, the more significant and important of the random variable 

              Features      P_values
x7                  Do  9.845181e-01
x19          Reading.1  9.395244e-01
x12         Fathersâ€™  9.380608e-01
x11         Mothersâ€™  9.344085e-01
x15       Mothersâ€™.1  8.447332e-01
x13             Number  8.028995e-01
x23        Preparation  7.772502e-01
x27         Discussion  7.153327e-01
x6             Regular  6.698715e-01
x22       Attendance.1  5.694502e-01
x30           Expected  5.513802e-01
x14           Parental  5.346943e-01
x28    Flip-classroom:  5.224313e-01
x24      Preparation.1  4.891439e-01
x8               Total  4.006258e-01
x17             Weekly  3.329913e-01
x25             Taking  2.743117e-01
x10      Accommodation  2.393702e-01
x4         Scholarship  1.165901e-01
x16       Fathersâ€™.1  1.108635e-01
x26          Listening  9.235711e-02
x20         Attendance  8.880913e-02
x21             Impact  7.531374e-02
x5          Additional  2.439858e-02
x3           Graduated  2.128536e-02
x9      Transportation  1.366272e-02
x1             Student  7.969091e-03
x18            Reading  4.066648e-03
x29         Cumulative  8.322683e-04
x2                 Sex  2.174488e-04
x31          Course_id  9.635829e-06
const         Constant  1.878028e-43
>>>>>>> 85c265b67d24aab3acdeaf089ea6e5cca5d48728
>>>>>>> main
'''