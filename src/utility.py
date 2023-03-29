# utility scripts 

import pandas as pd

def rename_higher_edu_columns(df, txt_path):
    """
    Renames the columns of a given DataFrame based on a text file
    containing a list of column names.

    Args:
        df (pandas.DataFrame): The DataFrame whose columns need to be renamed.

    Returns:
        pandas.DataFrame: The DataFrame with renamed columns.
    """
    
    # Read the text file with the list of column names
    df_txt = pd.read_fwf(txt_path)
    
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


def merge_middle_students(df_por: pd.DataFrame, df_mat: pd.DataFrame) -> pd.DataFrame:
    """Merges two pandas DataFrames of middle school students based on common attributes.

    Args:
        df_por (pd.DataFrame): DataFrame containing data on middle school students from the Portuguese course.
        df_mat (pd.DataFrame): DataFrame containing data on middle school students from the math course.

    Returns:
        pd.DataFrame: A merged DataFrame containing data on middle school students from both courses.
    """

    # Check that both inputs are pandas DataFrames
    if isinstance(df_por, pd.DataFrame) and isinstance(df_mat, pd.DataFrame):
        # Define the common attributes to use for the merge
        common_attributes = ["school", "sex", "age", "address", "famsize", "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", "reason", "nursery", "internet"]

        # Perform an outer merge of the two DataFrames based on the common attributes
        # Use suffixes to differentiate between columns with the same name in each DataFrame
        df_merged = pd.merge(df_por, df_mat, how='outer', on=common_attributes, suffixes=('_por', '_mat'))

        # Print the number of missing values in each column of the merged DataFrame
        print(df_merged.isna().sum())

    else:
        # Raise an error if either input is not a pandas DataFrame
        print("df_por or df_mat is not a pandas dataframe")
        raise TypeError

    # Return the merged DataFrame
    return df_merged
