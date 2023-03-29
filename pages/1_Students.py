import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px


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
    if "df" not in st.session_state:
        switch_page("Main")

    with st.sidebar:

        # xaxis_selection = st.multiselect(
        #     label="Select field for x-axis:",
        #     options=x_vars
        # )

        # yaxis_selection = st.multiselect(
        #     label="Select field for y-axis:",
        #     options=y_vars
        # )

        st.write("Source code for the project repository is located at [GitHub](https://github.com/leonswl/ntu-msds-sd6101/tree/main)")
    
if __name__ == "__main__":
    students()