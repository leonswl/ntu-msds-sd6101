# ntu-msds-sd6101
Project repository for module SD6101 (Data Science Thinking) under Masters of Science in Data Science (NTU)

<p align="center">
    <a href="https://www.python.org/downloads/release/python-3107/" alt="Contributors">
        <img src="https://img.shields.io/badge/python-3.10.7-blue"/></a>
</p>

**Table of Contents**
- [ntu-msds-sd6101](#ntu-msds-sd6101)
  - [Directory](#directory)
  - [Data Preparation](#data-preparation)
  - [Contributing](#contributing)
  - [Installation \& Usage](#installation--usage)

## Directory
- [artifacts](artifacts/): raw and persisted data artifacts
- [dependencies](requirements.txt): python dependencies
- [python prepare script](prepare.py): python script to perform data preparation on raw datasets

## Data Preparation

There are 647 students in the math class, and 395 students in the portuguese class. A student can take both math and portuguese class. Performing a full outer merge on identical attributes give us a total of 682 students enrolled in both classes. 

Identifical attributes: "school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"


**About the dataset**
For more details related to column attributes, refer to the [dataset metadata](artifacts/student.txt).

## Contributing

1. Clone the repository locally
1. Pull main branch to ensure your local main branch is up to date with the remote main branch
1. Create a new branch using `git checkout -b <branch-name>`
1. Merge the main branch to your working branch to keep your branch up to date with the latest changes `git merge main`
1. Once you have saved your changes, add -> commit -> push your changes to remote branch 
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
1. Create a Pull Request to merge your changes to the main branch. 
1. Repeat step 2 to 6 for subsequent contributions


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

