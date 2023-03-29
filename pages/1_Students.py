import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
import pandas as pd


# cache data to avoid reloading data
@st.cache_data(ttl=300, show_spinner=False)
def split_field_types(df):
    """
    Split the fields in a Pandas DataFrame into two lists: discrete_field_lst and cont_field_lst,
    based on the data type of the fields.

    Parameters:
    -----------
    df: pandas.DataFrame
        The input DataFrame with fields to split.

    Returns:
    --------
    tuple
        A tuple containing two lists of field names:
        1. discrete_field_lst - list of fields with 'object' data type.
        2. cont_field_lst - list of fields with numerical data type.
    """
    discrete_field_lst = []
    cont_field_lst = []

    # Loop over each field in the DataFrame
    for field, dtype in df.iterrows():
        # If the data type of the field is 'object', add it to discrete_field_lst
        if dtype[0] == 'object':
            discrete_field_lst.append(field)
        # Otherwise, add it to cont_field_lst
        else:
            cont_field_lst.append(field)

    # Return the two lists as a tuple
    return discrete_field_lst, cont_field_lst

def students():

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
    
    # return to home to fetch data 
    if "df" not in st.session_state or "y_vars" not in st.session_state or "x_vars" not in st.session_state:
        switch_page("Main")


    xvars_dtypes = pd.DataFrame(st.session_state.df[st.session_state.x_vars].dtypes).rename(columns={0:'dtypes'})
    discrete_field_lst, cont_field_lst = split_field_types(xvars_dtypes)

    with st.sidebar:

        # SELECT BOX - Discrete fields selection
        xaxis_discrete_selection = st.selectbox(
            label="Select field for discrete fields on x-axis:",
            options=discrete_field_lst
        )

        # SELECT BOX - Continuous fields selection
        st.markdown(f"You selected `{xaxis_discrete_selection}`")

        xaxis_cont_selection = st.selectbox(
            label="Select field for continuous fields on x-axis:",
            options=cont_field_lst
        )

        st.markdown(f"You selected `{xaxis_cont_selection}`")

        # SELECT BOX - y variable selection
        yaxis_selection = st.selectbox(
            label="Select field for y-axis:",
            options=st.session_state.y_vars
        )

        st.write("Source code for the project repository is located at [GitHub](https://github.com/leonswl/ntu-msds-sd6101/tree/main)")


    with st.expander("Expand to view dataset"):
        st.dataframe(st.session_state.df[st.session_state.x_vars])

    fig = px.bar(
        st.session_state.df,
        x=xaxis_cont_selection,
        y=yaxis_selection,
    )
    st.plotly_chart(fig)
    
if __name__ == "__main__":
    students()