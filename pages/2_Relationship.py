import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


# cache data to avoid reloading data
@st.cache_data(ttl=300, show_spinner=False)
def split_field_types(df, colnames_lst):
    """
    Split the fields in a Pandas DataFrame into two lists: categorical_field_lst and cont_field_lst,

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
        1. categorical_field_lst - list of fields with 'object' data type.
        2. cont_field_lst - list of fields with numerical data type.
    """
    categorical_field_lst = []
    cont_field_lst = ['age','absences']

    for col in df[colnames_lst].columns:
        if col not in cont_field_lst:
            categorical_field_lst.append(col)

    # Return the two lists as a tuple
    return categorical_field_lst, cont_field_lst


@st.cache_data(ttl=300, show_spinner=False)
def split_field_data(df, categorical_field_lst, cont_field_lst):
    """
    Splits a Pandas DataFrame into two DataFrames, one containing the columns specified in the
    categorical_field_lst argument and the other containing the columns specified in the cont_field_lst
    argument.

    Args:
        df (pandas.DataFrame): The DataFrame to split.
        categorical_field_lst (list): A list of column names that should be included in the categorical
                                  DataFrame.
        cont_field_lst (list): A list of column names that should be included in the continuous
                               DataFrame.

    Returns:
        tuple: A tuple containing the categorical DataFrame and the continuous DataFrame.

    """

    # Select the columns specified in the categorical_field_lst argument
    df_categorical = df[categorical_field_lst]

    # Select the columns specified in the cont_field_lst argument
    df_cont = df[cont_field_lst]

    # Return a tuple containing the categorical DataFrame and the continuous DataFrame
    return df_categorical, df_cont

def relationship():

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

     # split x variables dataset into categorical and continuous
    categorical_field_lst, cont_field_lst = split_field_types(st.session_state.df_mat, xvars_colnames)
    df_categorical, df_cont = split_field_data(df_students, categorical_field_lst, cont_field_lst)

    # find categorical columns with only 2 unique values
    categorical_bivals_colnames = []
    for col in df_categorical.columns:
        uniques = df_categorical[col].nunique()
        if uniques == 2:
            categorical_bivals_colnames.append(col)

    # TABS - categorical VS CONTINUOUS
    tab1, tab2 = st.tabs(['Categorical','Continuous'])

    # categorical TAB
    with tab1:
        # COLUMNS - widgets
        col1, col2, col3, col4 = st.columns([1,1,1,1])
        with col1:
            # SELECT BOX - categorical fields selection
            xaxis_categorical_selection = st.selectbox(
                label="Select categorical fields:",
                options=categorical_field_lst
            )
            st.markdown(f"You selected `{xaxis_categorical_selection}`")

        with col2:
            split_violin_selection = st.radio(
                label="Split violin plots:",
                options=(['No','Yes'])
            )
        if split_violin_selection == 'Yes':
            with col3:
                categorical_bivals_selection = st.selectbox(
                    label="Select additional field for",
                    options=categorical_bivals_colnames
                )
                st.markdown(f"You selected `{categorical_bivals_selection}`")

        if split_violin_selection == 'No':
            fig_categorical = px.violin(
                df_students,
                x=xaxis_categorical_selection,
                y=yaxis_selection,
                points='all',
                box=True,
            ).update_layout(
                xaxis_title= xaxis_categorical_selection,
                yaxis_title= yaxis_selection
            )

            st.plotly_chart(fig_categorical, use_container_width=True)

        else:
            bi_values = df_students[categorical_bivals_selection].unique()
            fig_categorical_split = go.Figure()
            
            fig_categorical_split.add_trace(go.Violin
                                                (x=df_students[xaxis_categorical_selection][df_students[categorical_bivals_selection]==bi_values[0]],
                                                y=df_students[yaxis_selection][df_students[categorical_bivals_selection]==bi_values[0]],
                                                legendgroup='Yes', 
                                                name=bi_values[0],
                                                side='negative',
                                                line_color='lightseagreen',
                                                points='all', 
                                                pointpos=-1.5
                                                )
                                        )
            fig_categorical_split.add_trace(go.Violin
                                                (x=df_students[xaxis_categorical_selection][df_students[categorical_bivals_selection]==bi_values[1]],
                                                y=df_students[yaxis_selection][df_students[categorical_bivals_selection]==bi_values[1]],
                                                legendgroup='Yes', 
                                                name=bi_values[1],
                                                side='positive',
                                                line_color='mediumpurple',
                                                points='all', 
                                                pointpos=1.5
                                                )
                                        )
            fig_categorical_split.update_traces(meanline_visible=True)
            st.plotly_chart(fig_categorical_split, use_container_width=True)

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