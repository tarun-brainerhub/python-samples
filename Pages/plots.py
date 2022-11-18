import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def app():
    try:
        df = st.session_state.get("df")
        df_addded = st.session_state.get("df_added")
        if df_addded:
            st.write("Correlation matrix")
            corr = df.corr()
            fig = px.imshow(corr)
            st.plotly_chart(fig)

            columns = df.columns
            n = st.selectbox("Histogram",options=columns, key="a")
            fig = px.histogram(df, x=n, )
            st.plotly_chart(fig)

            m = st.selectbox("Bar plot",options=columns, key="c")
            fig = px.box(df, y=m, points="all")
            st.plotly_chart(fig)

            m = st.selectbox("violine plot",options=columns, key="b")
            fig = px.violin(df, y=m, points='all',box=True)
            st.plotly_chart(fig)
        else:
            st.write("Please upload your data in home page")
    except :
        st.write("Please upload your data in home page")