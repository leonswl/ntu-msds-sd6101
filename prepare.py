# prepare data for eda

import pandas as pd


# import files as pandas dataframe

df_higher_edu_student = pd.read_csv('artifacts/higher-education-student.csv',sep=';')
df_middle_student_mat = pd.read_csv('artifacts/middle-student-mat.csv',sep=';')
df_middle_student_por = pd.read_csv('artifacts/middle-student-por.csv',sep=';')

# 
import pandas as pd

def rename_higher_edu_columns(df):
    """
    Renames the columns of a given DataFrame based on a text file
    containing a list of column names.

    Args:
        df (pandas.DataFrame): The DataFrame whose columns need to be renamed.

    Returns:
        pandas.DataFrame: The DataFrame with renamed columns.
    """
    
    # Read the text file with the list of column names
    df_txt = pd.read_fwf('artifacts/higher-education-student.txt')
    
    # Make a copy of the DataFrame and drop the first row (which contains the old column names)
    df_txt = df_txt.copy()[1:]
    
    # Create a list of the new column names based on the values in the text file
    column_lst = []
    for index, row in df_txt.iterrows():
        split_str = str(row.values).split(" ")
        column_lst.append(split_str[1])

    # Drop the 'STUDENT ID' column from the DataFrame
    df_dropped = df.drop(['STUDENT ID'], axis=1)

    # Rename the columns of the DataFrame with the new column names
    df_dropped.columns = column_lst

    # Rename specific columns with new names
    df_dropped.rename(columns={'Course': 'Course_id', 'OUTPUT': 'Grade'}, inplace=True)

    return df_dropped


df_higher_edu_student_new = rename_higher_edu_columns(df_higher_edu_student)