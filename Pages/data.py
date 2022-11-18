import streamlit as st
import pandas as pd


def app():
    try:
        df_addded = st.session_state.get("df_added")
    except:
        df_addded = False
    df = st.session_state.get("df")
    
    if df_addded == True:
        ph1 = st.empty()
        ph2 = st.empty()
        if df.isna().sum().reset_index()[0].sum() != 0:
            ph1.warning("There are null vales in your data")
            btn = ph2.button("drop them")
            if btn:
                ph1.empty()
                ph2.empty()
                df.dropna(axis=0,inplace=True)
        st.markdown("#### your data")
        st.dataframe(df, width=1000, height=250)
        features = st.multiselect("drop features", df.columns)
        if features:
            df.drop(features,axis =1, inplace=True)
            st.dataframe(df, width=1000, height=250)  
    else:
        st.write("Please upload your data in home page")
