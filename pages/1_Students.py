import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
import pandas as pd


# cache data to avoid reloading data
@st.cache_data(ttl=300, show_spinner=False)
def split_field_types(df, colnames_lst):
    """
    Split the fields in a Pandas DataFrame into two lists: discrete_field_lst and cont_field_lst,
    based on the data type of the fields.

    Parameters:
    -----------
    df: pandas.DataFrame
        The input DataFrame with fields to split.
    colnames_lst: list
        Input list of column names

    Returns:
    --------
    tuple
        A tuple containing two lists of field names:
        1. discrete_field_lst - list of fields with 'object' data type.
        2. cont_field_lst - list of fields with numerical data type.
    """
    df_dtypes = pd.DataFrame(df[colnames_lst].dtypes).rename(columns={0:'dtypes'})

    discrete_field_lst = []
    cont_field_lst = []

    # Loop over each field in the DataFrame
    for field, dtype in df_dtypes.iterrows():
        # If the data type of the field is 'object', add it to discrete_field_lst
        if dtype[0] == 'object':
            discrete_field_lst.append(field)
        # Otherwise, add it to cont_field_lst
        else:
            cont_field_lst.append(field)

    # Return the two lists as a tuple
    return discrete_field_lst, cont_field_lst


@st.cache_data(ttl=300, show_spinner=False)
def split_field_data(df, discrete_field_lst, cont_field_lst):
    """
    Splits a Pandas DataFrame into two DataFrames, one containing the columns specified in the
    discrete_field_lst argument and the other containing the columns specified in the cont_field_lst
    argument.

    Args:
        df (pandas.DataFrame): The DataFrame to split.
        discrete_field_lst (list): A list of column names that should be included in the discrete
                                  DataFrame.
        cont_field_lst (list): A list of column names that should be included in the continuous
                               DataFrame.

    Returns:
        tuple: A tuple containing the discrete DataFrame and the continuous DataFrame.

    """

    # Select the columns specified in the discrete_field_lst argument
    df_discrete = df[discrete_field_lst]

    # Select the columns specified in the cont_field_lst argument
    df_cont = df[cont_field_lst]

    # Return a tuple containing the discrete DataFrame and the continuous DataFrame
    return df_discrete, df_cont

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
    if (
        "df" not in st.session_state or 
        "df_mat" not in st.session_state or 
        "df_por" not in st.session_state or 
        "y_vars" not in st.session_state or 
        "x_vars" not in st.session_state
    ):
        switch_page("Main")

    yvars_colnames = [col for col in st.session_state.df_mat.columns if col.startswith("G")]
    xvars_colnames = [col for col in st.session_state.df_mat.columns if col not in yvars_colnames]

    # SIDEBAR
    with st.sidebar:

        # RADIO SELECTION - Portugese or math students
        course_selection = st.radio(
            label="Select course type",
            options=("Math","Portugese")
        )

        st.write("Source code for the project repository is located at [GitHub](https://github.com/leonswl/ntu-msds-sd6101/tree/main)")

    
    if course_selection == "Math":
        df_students = st.session_state.df_mat
    elif course_selection == "Portugese":
        df_students = st.session_state.df_por


    with st.expander(f"Expand to view {course_selection.title()} dataset"):
        st.dataframe(df_students)

     # split x variables dataset into discrete and continuous
    discrete_field_lst, cont_field_lst = split_field_types(st.session_state.df_mat, xvars_colnames)
    df_discrete, df_cont = split_field_data(df_students, discrete_field_lst, cont_field_lst)

    # TABS - DISCRETE VS CONTINUOUS
    tab1, tab2, tab3 = st.tabs(['Discrete','Continuous','Grades'])

    # DISCRETE TAB
    with tab1:
        # COLUMNS - widgets
        col1, col2 = st.columns([1,3])
        with col1:
            # SELECT BOX - Discrete fields selection
            xaxis_discrete_selection = st.selectbox(
                label="Select discrete fields:",
                options=discrete_field_lst
            )
            st.markdown(f"You selected `{xaxis_discrete_selection}`")

        
        fig_discrete = px.histogram(
            df_discrete,
            x=xaxis_discrete_selection,
            # nbins=bin_width,
            text_auto=True
        ).update_layout(
            xaxis_title= xaxis_discrete_selection,
            yaxis_title= "Number of Students"
        )

        st.plotly_chart(fig_discrete, use_container_width=True)

    with tab2:
        # COLUMNS - widgets
        col1, col2, col3 = st.columns([1,1,2])
        with col1:
            # SELECT BOX - Continuous fields selection
            xaxis_cont_selection = st.selectbox(
                label="Select continuous fields:",
                options=cont_field_lst
            )
            st.markdown(f"You selected `{xaxis_cont_selection}`")

        with col3:
            # SLIDER - BIN WIDTH
            bin_width = st.slider(
                "Select bin width",
                min_value=10,
                max_value=100,
                step=10,
                value=30,
                key='cont'
            )
            st.write('You select a bin width of', bin_width)

        fig_cont = px.histogram(
            df_cont,
            x=xaxis_cont_selection,
            nbins=bin_width,
            text_auto=True
        ).update_layout(
            xaxis_title= xaxis_cont_selection,
            yaxis_title= "Number of Students"
        )

        st.plotly_chart(fig_cont, use_container_width=True)

    with tab3:

        st.markdown(
        """
        These grades are related with the course subject, Math or Portuguese:
        - G1: first period grade (numeric: from 0 to 20)
        - G2: second period grade (numeric: from 0 to 20)
        - G3: final grade (numeric: from 0 to 20, output target)
        """
        )

        col1, col2, col3 = st.columns([1,1,2])
        with col1:
            yaxis_selection = st.selectbox(
                label="Select field for y-axis:",
                options=yvars_colnames
            )

        with col3:
            # SLIDER - BIN WIDTH
            bin_width_grades = st.slider(
                "Select bin width",
                min_value=5,
                max_value=50,
                step=5,
                value=25,
                key='grade'
            )
            st.write('You select a bin width of', bin_width)
        # PLOTLY CHART - Histograms of Grades
        fig_grades = px.histogram(
            df_students[yvars_colnames],
            x=yaxis_selection,
            nbins=bin_width_grades,
            text_auto=True
        ).update_layout(
            xaxis_title= yaxis_selection,
            yaxis_title= "Number of Students"
        )

        st.plotly_chart(fig_grades, use_container_width=True)



    
if __name__ == "__main__":
    students()