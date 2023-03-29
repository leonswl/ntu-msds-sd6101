import streamlit as st
import yaml
import pandas as pd



# cache data to avoid reloading data
@st.cache_data(ttl=300, show_spinner=False)
def load_parquet(path_filename):
    """
    Loads a Parquet file located at the given path and filename into a pandas DataFrame.
    Args:
    - path_filename: string containing the path and filename of the Parquet file to be loaded
    Returns:
    - pandas DataFrame containing the contents of the Parquet file
    """
    
    # Use pandas' read_parquet() function to load the Parquet file into a DataFrame
    
    return pd.read_csv(path_filename)

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
        
    path_filename = f"{artifacts_path}/{middle_student_artifact}"
    df = load_parquet(path_filename=path_filename).iloc[:,1:]

    

    y_vars = ['G1_por', 'G2_por', 'G3_por', 'G1_mat', 'G2_mat', 'G3_mat']
    x_vars = [col for col in st.session_state.df.columns if col not in y_vars]

    if "df" not in st.session_state:
        st.session_state.df = df

    if "y_vars" not in st.session_state:
        st.session_state.y_vars = y_vars

    if "x_vars" not in st.session_state:
        st.session_state.x_vars = x_vars

    with st.sidebar:

        xaxis_selection = st.multiselect(
            label="Select field for x-axis:",
            options=x_vars
        )

        yaxis_selection = st.multiselect(
            label="Select field for y-axis:",
            options=y_vars
        )

        st.write("Source code for the project repository is located at [GitHub](https://github.com/leonswl/ntu-msds-sd6101/tree/main)")


    with st.expander("Expand to view dataset"):
        st.dataframe(st.session_state.df)

    


if __name__ == "__main__":
    main()