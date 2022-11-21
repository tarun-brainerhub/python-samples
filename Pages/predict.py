import streamlit as st
import pandas as pd

def app():
        df_addded = st.session_state.get("df_added")
        best_model = st.session_state.get("best_model")
        df = st.session_state.get("df")
        output = st.session_state.get("output")
        if best_model == None:
            st.write("MODEL IS NOT TRAINED YET PLEASE TRAIN THE MODEL")
            return
        if df_addded == True:
            for col in df.columns:
                if col != output:
                    st.number_input(col,min_value=min(df[col]),max_value=max(df[col]), key=col)


            btn = st.button("predict")  
            if btn: 
                d = {}
                for col in df.columns:
                    if col != output:
                        d[col] = [st.session_state.get(col)]

                data = pd.DataFrame(d)
                pred = best_model.predict(data)

                st.success(f"Prediction : {pred[0]} ")
        else :
            st.write("Please upload your data in home page")
