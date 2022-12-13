import streamlit as st
from data_preprosesing import custom_input_prediction

st.header("Type of CyberBully")

text = st.text_area("Enter tweet here", placeholder="Tweet")

b = st.button("Check")

if b:
    if text == "":
        st.info("'LMAO' enter some text dwag")
    else:
        output = custom_input_prediction(text)
        if output == "Not Cyberbullying":
            st.success(output)
        else:
            st.warning(output)


