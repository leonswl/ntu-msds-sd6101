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

        
    path_filename = f"{artifacts_path}/{middle_student_artifact}"
    df = load_file(path_filename=path_filename).iloc[:,1:]

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

        xaxis_selection = st.selectbox(
            label="Select field for x-axis:",
            options=x_vars
        )

        yaxis_selection = st.selectbox(
            label="Select field for y-axis:",
            options=y_vars
        )

        st.write("Source code for the project repository is located at [GitHub](https://github.com/leonswl/ntu-msds-sd6101/tree/main)")

    ## MAIN PAGE
    st.markdown(
        """
        # EDA Dashboard of Secondary Education Students in Portugal
        
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