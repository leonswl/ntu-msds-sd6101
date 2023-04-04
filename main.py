import streamlit as st
import yaml
import pandas as pd



# cache data to avoid reloading data
@st.cache_data(ttl=300, show_spinner=False)
def load_file(path_filename, sep:str=','):
    """
    Loads a Parquet file located at the given path and filename into a pandas DataFrame.
    Args:
    - path_filename: string containing the path and filename of the Parquet file to be loaded
    Returns:
    - pandas DataFrame containing the contents of the Parquet file
    """

    return pd.read_csv(path_filename, sep=sep)

def main():

    # set configuration
    st.set_page_config(
        page_title="EDA Dashboard of Secondary Education Students in Portugal",
        page_icon="🏢",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Report a bug": "https://github.com/leonswl/ntu-msds-sd6101/issues",
            "About": "Thanks for dropping by!"
            }
        )
    
    # Load configuration details from config.yml file
    with open("config.yml", encoding="utf-8", mode="r") as ymlfile:
        cfg = yaml.load(ymlfile,Loader=yaml.Loader)
        artifacts_path = cfg["eda"]["artifacts_path"]
        middle_student_artifact = cfg["eda"]["middle_student_artifact"]
        middle_student_math = cfg["eda"]["middle_student_math"]
        middle_student_por = cfg["eda"]["middle_student_por"]

    # load datasets
    df = load_file(path_filename=f"{artifacts_path}/{middle_student_artifact}").iloc[:,1:]
    df_mat = load_file(path_filename=f"{artifacts_path}/{middle_student_math}",sep=';')
    df_por = load_file(path_filename=f"{artifacts_path}/{middle_student_por}",sep=';')


    # y variable column names
    y_vars = ['G1_por', 'G2_por', 'G3_por', 'G1_mat', 'G2_mat', 'G3_mat']
    # x variable column names
    x_vars = [col for col in df.columns if col not in y_vars]

    # Declare session states
    if "df" not in st.session_state:
        st.session_state.df = df

    if "df_mat" not in st.session_state:
        st.session_state.df_mat = df_mat

    if "df_por" not in st.session_state:
        st.session_state.df_por = df_por

    if "y_vars" not in st.session_state:
        st.session_state.y_vars = y_vars

    if "x_vars" not in st.session_state:
        st.session_state.x_vars = x_vars


    # SIDEBAR
    with st.sidebar:

        # xaxis_selection = st.selectbox(
        #     label="Select field for x-axis:",
        #     options=x_vars
        # )

        # yaxis_selection = st.selectbox(
        #     label="Select field for y-axis:",
        #     options=y_vars
        # )

        st.write("Source code for the project repository is located at [GitHub](https://github.com/leonswl/ntu-msds-sd6101/tree/main)")

    ## MAIN PAGE
    st.markdown(
        """
        # EDA Dashboard of Secondary Education Students in Portugal

        ## Data Dictionary
        The grades are related with the course subject, Math or Portuguese:
        | No. | Columns | Data Type |
        | --- | ---     | ---       |
        | 1 | school - student's school (binary: "GP" - Gabriel Pereira or "MS" - Mousinho da Silveira) | Nominal (Categorical) |
        | 2 | sex - student's sex (binary: "F" - female or "M" - male) | Nominal (Categorical) |
        | 3 | age - student's age (numeric: from 15 to 22) | Continuous | 
        | 4 | address - student's home address type (binary: "U" - urban or "R" - rural) | Nominal (Categorical) |
        | 5 | famsize - family size (binary: "LE3" - less or equal to 3 or "GT3" - greater than 3) | Ordinal (Categorical) | 
        | 6 | Pstatus - parent's cohabitation status (binary: "T" - living together or "A" - apart) | Nominal (Categorical) | 
        | 7 | Medu - mother's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education) | Ordinal (Categorical) |
        | 8 | Fedu - father's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education) | Ordinal (Categorical) |
        | 9 | Mjob - mother's job (nominal: "teacher", "health" care related, civil "services" (e.g. administrative or police), "at_home" or "other") | Nominal (Categorical) | 
        | 10 | Fjob - father's job (nominal: "teacher", "health" care related, civil "services" (e.g. administrative or police), "at_home" or "other") | Nominal (Categorical) |
        | 11 | reason - reason to choose this school (nominal: close to "home", school "reputation", "course" preference or "other") | Nominal (Categorical) |
        | 12 | guardian - student's guardian (nominal: "mother", "father" or "other") | Nominal (Categorical) |
        | 13 | traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)| Ordinal (Categorical) |
        | 14 | studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours) | Ordinal (Categorical) |
        | 15 | failures - number of past class failures (numeric: n if 1<=n<3, else 4) | Ordinal (Categorical) |
        | 16 | schoolsup - extra educational support (binary: yes or no) | Nominal (Categorical) |
        | 17 | famsup - family educational support (binary: yes or no) | Nominal (Categorical) |
        | 18 | paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no) | Nominal (Categorical) |
        | 19 | activities - extra-curricular activities (binary: yes or no) | Nominal (Categorical) |
        | 20 | nursery - attended nursery school (binary: yes or no) | Nominal (Categorical) |
        | 21 | higher - wants to take higher education (binary: yes or no) | Nominal (Categorical) |
        | 22 | internet - Internet access at home (binary: yes or no) | Nominal (Categorical) |
        | 23 | romantic - with a romantic relationship (binary: yes or no) | Nominal (Categorical) |
        | 24 | famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent) | Ordinal (Categorical) |
        | 25 | freetime - free time after school (numeric: from 1 - very low to 5 - very high) | Ordinal (Categorical) |
        | 26 | goout - going out with friends (numeric: from 1 - very low to 5 - very high) | Ordinal (Categorical) |
        | 27 | Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high) | Ordinal (Categorical) |
        | 28 | Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high) | Ordinal (Categorical) |
        | 29 | health - current health status (numeric: from 1 - very bad to 5 - very good) | Ordinal (Categorical) |
        | 30 | absences - number of school absences (numeric: from 0 to 93) | Continuous |
        | 31 | G1 - first period grade (numeric: from 0 to 20) | Continuous |
        | 31 | G2 - second period grade (numeric: from 0 to 20) | Continuous |
        | 32 | G3 - final grade (numeric: from 0 to 20, output target) | Continuous |
        """
    )

    # TABS
    tab1, tab2, tab3 = st.tabs(["All Students","Math Students",'Portugese Students'])

    with tab1:
        st.dataframe(st.session_state.df)

    with tab2: 
        st.dataframe(st.session_state.df_mat)

    with tab3:
        st.dataframe(st.session_state.df_mat)


if __name__ == "__main__":
    main()