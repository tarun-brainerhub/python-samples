import streamlit as st
import pandas as pd
from Pages import train, plots, data, home

# from main import pages
def app():
    st.markdown("""
    
    # know your DATA

    ### steps:
    1. Upload your CSV file bellow.
    1. Go to DATA section for preprocessing.
    2. Go to PLOTS section and visualise your data.
    3. Go to TRAIN section and get best machine learning model for your data.
    4. Go to PREDICT section and predict some outputs by providing new single data. 


    """)
    st.warning("This app Supports only csv files and numerical data for now")
    st.write("Enter your csv file here")
    file = st.file_uploader("Uplode here",type=["csv"])
    if file:
        df = pd.read_csv(file)
        st.session_state["df"] = df
        st.session_state["df_added"] = True

    st.markdown( '''### GitHub Repository: [KnowYourData](https://github.com/rishibrainerhub/knowyourdata)''')