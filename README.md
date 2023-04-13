# ntu-msds-sd6101

<p align="center">
    <a href="https://www.python.org/downloads/release/python-3107/" alt="Contributors">
      <img src="https://img.shields.io/badge/python-3.10.7-blue"/></a>
    <a href="https://layonsan-hdb-resale.streamlit.app/" alt="Streamlit App">
      <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg"/></a>
</p>

Project repository for module SD6101 (Data Science Thinking) under Masters of Science in Data Science (NTU).

**Table of Contents**
- [ntu-msds-sd6101](#ntu-msds-sd6101)
  - [Directory](#directory)
  - [Data Source](#data-source)
  - [Data Preparation](#data-preparation)
  - [Data Modelling \& Analysis](#data-modelling--analysis)
  - [Data Visualisation \& Explaination](#data-visualisation--explaination)
  - [Contributing](#contributing)
  - [Installation \& Usage](#installation--usage)

## Directory
- [artifacts](artifacts): raw and persisted data artifacts
- [dependencies](requirements.txt): python dependencies
- [Streamlit main app](main.py): python script to initialise main streamlit app
- [notebooks](notebooks): python notebooks for various exploratory tasks
- [src]: python scripts for modular execution
- [configuration]: config files for modular scripts

## Data Source
-  Student Performance Data Set
   -  Obtained from [UCI Machine Learning - Student Performance](https://archive.ics.uci.edu/ml/datasets/student+performance)
   -  For more details related to column attributes, refer to the [dataset metadata](artifacts/raw/student.txt).
 
- Higher Education Students Performance Evaluation Data Set
  - Obtained from [UCI Machine Learning - Higher Education Students Performance ](https://archive.ics.uci.edu/ml/datasets/Higher+Education+Students+Performance+Evaluation+Dataset)
  - For more details related to column attributes, refer to the [dataset metadata](artifacts/raw/higher-education-student.txt).

## Data Preparation

There are  395 students in the math class, and 647 students in the portuguese class. A student can take both math and portuguese class. Performing a full outer merge on identical attributes give us a total of 382 students enrolled in both classes. 

Identifical attributes: "school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"

After data preparation, data will be persisted in [artifacts](artifacts) as new artifacts.

**However, upon exploring the datasets, math middle school students were selected for analysis. This means that we only used the [raw math student dataset](/Users/leonsun/Documents/GitHub/ntu/ntu-msds-sd6101/artifacts/raw/middle-student-mat.csv).**

## Data Modelling & Analysis

**EDA**
EDA of datasets are visualised in the streamlit web app. The main pages handling the visual rendering are located in [pages](pages)

Due to the huge number of features (dependent variables) available in the dataset, we focused on the following features to narrow the scope of the analysis ['school','sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob', 'Fjob','reason','nursery']

**Statistical Tests**
Using the math dataset, we investigated for differences in students' grades (mean/variance) using statistical tests for the various features. Statistical tests are computed using Scipy library. The features with 2 groups, we employed t-tests. Features with more than 2 groups are tested using ANOVA. 

We validated the Homogeneity of Variance assumption using the Levene test. Results revealed that comparing student grades across the groups have differing variances, and hence do not satisfy the assumption. Non parametric statistical tests were used instead - Welch's t-test and Kruskal-Wallis one-way ANOVA test.

## Data Visualisation & Explaination
We summarised our key findings and visualised our data on a PowerBI Dashboard [PowerBI Dashboard](https://github.com/leonswl/ntu-msds-sd6101/blob/main/Education%20Analysis.pbix) / PDF [PDF] (https://github.com/leonswl/ntu-msds-sd6101/blob/main/Education%20Analysis.pdf)

## Contributing

1. Clone the repository locally
2. Pull main branch to ensure your local main branch is up to date with the remote main branch
3. Create a new branch using `git checkout -b <branch-name>`
4. Merge the main branch to your working branch to keep your branch up to date with the latest changes `git merge main`
5. Once you have saved your changes, add -> commit -> push your changes to remote branch 
    ```
    # add all changes
    git add . 

    # commit your changes with a commit message
    git commit -m "<your commit message>"

    # push your changes to remote
    git push

    # you will be prompted to set a remote upstream if this is your first time pushing changes after creating the new branch
    git push --set-upstream origin <branch-name>
    ```
6. Create a Pull Request to merge your changes to the main branch. 
7. Repeat step 2 to 6 for subsequent contributions


## Installation & Usage

```
# initialise isolated python environment
python -m venv .venv

# initialise environment
source .venv/bin/activate # mac
.venv/Scripts/Activate # windows

# install dependencies
pip install -r requirements.txt


# freeze dependencies
pip freeze > requirements.txt
```

