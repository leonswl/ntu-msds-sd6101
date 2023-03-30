import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


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

def relationship():

    yvars_colnames = [col for col in st.session_state.df_mat.columns if col.startswith("G")]
    xvars_colnames = [col for col in st.session_state.df_mat.columns if col not in yvars_colnames]

    # SIDEBAR
    with st.sidebar:

        # RADIO SELECTION - Portugese or math students
        course_selection = st.radio(
            label="Select course type",
            options=("Math","Portugese")
        )

        # RADIO SELECTION - Grade type
        yaxis_selection = st.radio(
            label="Select grade type:",
            options=yvars_colnames
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

    # find discrete columns with only 2 unique values
    discrete_bivals_colnames = []
    for col in df_discrete.columns:
        uniques = df_discrete[col].nunique()
        if uniques == 2:
            discrete_bivals_colnames.append(col)

    # TABS - DISCRETE VS CONTINUOUS
    tab1, tab2 = st.tabs(['Discrete','Continuous'])

    # DISCRETE TAB
    with tab1:
        # COLUMNS - widgets
        col1, col2, col3, col4 = st.columns([1,1,1,1])
        with col1:
            # SELECT BOX - Discrete fields selection
            xaxis_discrete_selection = st.selectbox(
                label="Select discrete fields:",
                options=discrete_field_lst
            )
            st.markdown(f"You selected `{xaxis_discrete_selection}`")

        with col2:
            split_violin_selection = st.radio(
                label="Split violin plots:",
                options=(['No','Yes'])
            )
        if split_violin_selection == 'Yes':
            with col3:
                discrete_bivals_selection = st.selectbox(
                    label="Select additional field for",
                    options=discrete_bivals_colnames
                )
                st.markdown(f"You selected `{discrete_bivals_selection}`")

        if split_violin_selection == 'No':
            fig_discrete = px.violin(
                df_students,
                x=xaxis_discrete_selection,
                y=yaxis_selection,
                points='all',
                box=True,
            ).update_layout(
                xaxis_title= xaxis_discrete_selection,
                yaxis_title= yaxis_selection
            )

            st.plotly_chart(fig_discrete, use_container_width=True)

        else:
            bi_values = df_students[discrete_bivals_selection].unique()
            fig_discrete_split = go.Figure()
            
            fig_discrete_split.add_trace(go.Violin
                                                (x=df_students[xaxis_discrete_selection][df_students[discrete_bivals_selection]==bi_values[0]],
                                                y=df_students[yaxis_selection][df_students[discrete_bivals_selection]==bi_values[0]],
                                                legendgroup='Yes', 
                                                name=bi_values[0],
                                                side='negative',
                                                line_color='lightseagreen',
                                                points='all', 
                                                pointpos=-1.5
                                                )
                                        )
            fig_discrete_split.add_trace(go.Violin
                                                (x=df_students[xaxis_discrete_selection][df_students[discrete_bivals_selection]==bi_values[1]],
                                                y=df_students[yaxis_selection][df_students[discrete_bivals_selection]==bi_values[1]],
                                                legendgroup='Yes', 
                                                name=bi_values[1],
                                                side='positive',
                                                line_color='mediumpurple',
                                                points='all', 
                                                pointpos=1.5
                                                )
                                        )
            fig_discrete_split.update_traces(meanline_visible=True)
            st.plotly_chart(fig_discrete_split, use_container_width=True)

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

        fig_scatter = px.scatter(
            df_students,
            x=xaxis_cont_selection,
            y=yaxis_selection,
            trendline="ols"
        ).update_layout(
            xaxis_title= xaxis_cont_selection,
            yaxis_title= yaxis_selection
        )

        st.plotly_chart(fig_scatter, use_container_width=True)


        results = px.get_trendline_results(fig_scatter)
        st.write(results.px_fit_results.iloc[0].summary())


if __name__ == "__main__":
    relationship()