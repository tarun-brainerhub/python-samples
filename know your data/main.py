import streamlit as st
import pandas as pd
# from Pages.data import data
# from Pages.train import *
st.set_option('deprecation.showPyplotGlobalUse', False)
from Pages import train, plots, data, home, predict



pages = {
    "Home":home,
    "Data": data,
    "Plots": plots,
    "Train": train,
    "Predict": predict
}


st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", list(pages.keys()), key="sidebar")
if page == None:
    home.app()
else:
   pages[page].app()

















# st.write("Enter your csv file here")
# file = st.file_uploader("Uplode here",type=["csv"])
# if file:
#     df = pd.read_csv(file)
#     if df.isna().sum().reset_index()[0].sum() != 0:
#         p1 = st.empty()
#         p2 = st.empty()
#         p1.warning("Looks like your data has some Null value",icon="⚠️")
#         d = p2.button("Drop them")
#         if d:
#             p2.empty()
#             p1.empty()
#             df.dropna(inplace=True)
#     data(df)
#     bt = st.button("Train model")
#     if bt:
#         output = st.radio("select output column", df.columns)
#         bt2 = st.button("enter")
#         if bt2:
#            with st.spinner('Wait for it...'):
#                 X_train, X_test, y_train, y_test = get_training_data(df,output=output, test_size= 0.2)
#                 score = logisticregresion(X_train=X_train, X_test=X_test)
#                 st.write(score)