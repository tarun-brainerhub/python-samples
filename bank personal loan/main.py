import streamlit as st
import pickle
import pandas as pd

st.title("Bank personal loan eligibility checker")
st.markdown("#### This model is trained using Random Forest	with 0.96% accuracy")

loaded_model = pickle.load(open("model.sav", 'rb'))

Age = st.slider("Age (Customer's age in completed years)", min_value=0, max_value=100)

Experience = st.slider("Experience (Years of professional experience)", min_value=0 , max_value=50)

Income = st.number_input("Income (Annual income of the customer))",min_value=1.0, max_value=20.0)

family = st.slider("Family (Family size of the customer)", min_value=1, max_value=5)

CCAvg = st.slider("CCAvg (Avg. spending on credit cards per month )", min_value=0, max_value=10)

Education = st.radio("Education", ("Undergrad", "Graduate", "Advanced/Professional"))

Mortgage = st.slider("Mortgage (Value of house mortgage if any.)", min_value=0, max_value=650)

Securities_Account = st.radio("Securities Account" ,("Yes", "No"))

CD_Account = st.radio("CD Account" ,("Yes", "No"))

Online = st.radio("Online" ,("Yes", "No"))

CreditCard = st.radio("CreditCard" ,("Yes", "No"))

predict = st.button("Predict")

if predict:
    ed = 1 if Education == "Undergrad" else 3
    ed = 2 if Education == "Graduate" else 3    
    sa = 1 if Securities_Account == "Yes" else 0
    cda = 1 if CD_Account == "Yes" else 0
    online = 1 if Online == "yes" else 0
    ccard = 1 if CreditCard == "Yes" else 0
    input_data = {'Age':[Age], 'Experience':[Experience], 'Income':[Income], 'Family':[family], 'CCAvg':[CCAvg], 'Education':[ed], 'Mortgage':[Mortgage], 'Securities Account':[sa], 'CD Account':[cda], 'Online':[online], 'CreditCard':[ccard],}
    sample = pd.DataFrame(input_data)
    result = loaded_model.predict(sample)
    if result[0] == 0:
        st.warning("Sorry you are not eligible for personal loan")
    else:
        st.success("you are eligible for personal loan")
        st.balloons()