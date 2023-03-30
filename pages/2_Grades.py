import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
import pandas as pd



def grades():

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

    ## SIDEBAR
    
    with st.sidebar:

        yaxis_selection = st.selectbox(
            label="Select field for y-axis:",
            options=st.session_state.y_vars
        )
    
    with st.expander("Expand to view dataset of grades"):
        st.dataframe(st.session_state.df.iloc[:,-3:])


    st.markdown(
        """
        These grades are related with the course subject, Math or Portuguese:
        - G1: first period grade (numeric: from 0 to 20)
        - G2: second period grade (numeric: from 0 to 20)
        - G3: final grade (numeric: from 0 to 20, output target)
        """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        # SLIDER - BIN WIDTH
        bin_width = st.slider(
            "Select bin width",
            min_value=10,
            max_value=100,
            step=10,
            value=50
        )
        st.write('You select a bin width of', bin_width)

    

    # PLOTLY CHART - Histograms of Grades
    fig = px.histogram(
        st.session_state.df,
        x=yaxis_selection,
        nbins=bin_width,
        text_auto=True
    ).update_layout(
        xaxis_title= yaxis_selection,
        yaxis_title= "Number of Students"
    )

    st.plotly_chart(fig, use_container_width=True)



if __name__ == "__main__":
    grades()