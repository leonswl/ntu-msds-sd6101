# prepare data for eda

import pandas as pd
import yaml
from utility import rename_higher_edu_columns, merge_middle_students

def prepare() -> None:
    """
    Load data from CSV files, rename columns and merge DataFrames, and persist new CSV files.

    This function loads configuration details from a YAML file called "config.yml". The configuration file should contain
    information about the file paths for the input data files and the output files to be saved.

    The function reads in the data from the input files as pandas DataFrames, calls two helper functions to rename
    columns and merge DataFrames, and then persists the resulting DataFrames as CSV files.

    Args:
        None

    Returns:
        None
    """
    # Load configuration details from config.yml file
    with open("config.yml", encoding="utf-8", mode="r") as ymlfile:
        cfg = yaml.load(ymlfile,Loader=yaml.Loader)
        higher_edu_student_file = cfg["prepare"]["higher_edu_student_file"]
        middle_student_mat_file = cfg["prepare"]["middle_student_mat_file"]
        middle_student_por_file = cfg["prepare"]["middle_student_por_file"]
        artifacts_path = cfg["prepare"]["artifacts_path"]
        txt_path = cfg["prepare"]["txt_path"]

    # Import data as pandas DataFrames
    df_higher_edu_student = pd.read_csv(f'{artifacts_path}/{higher_edu_student_file}',sep=';')
    df_middle_student_mat = pd.read_csv(f'{artifacts_path}/{middle_student_mat_file}',sep=';')
    df_middle_student_por = pd.read_csv(f'{artifacts_path}/{middle_student_por_file}',sep=';')

    # Rename columns in the higher education student data frame to readable format
    df_higher_edu_student_new = rename_higher_edu_columns(df_higher_edu_student, txt_path)

    # Merge middle school student data frames
    df_middle_students = merge_middle_students(df_middle_student_por, df_middle_student_mat)

    # Persist new CSV files
    df_higher_edu_student_new.to_csv(f"{artifacts_path}/higher_edu_student_new.csv")
    df_middle_students.to_csv(f"{artifacts_path}/middle_students_new.csv")

    print("""
    --------------------------------------------
    Successfully persisted data as new artifacts
    """)

if __name__ == "__main__":
    # Call prepare function when script is run as main
    prepare()