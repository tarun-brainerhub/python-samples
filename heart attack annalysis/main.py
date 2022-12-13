import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
from functions import *
plt.style.use('seaborn-dark')
plt.style.context('grayscale')
import streamlit as st

from wordcloud import WordCloud, STOPWORDS

df1 = pd.read_csv("heart.csv")
df2 = pd.read_csv("o2Saturation.csv")

df = pd.merge(df1, df2, left_index= True, right_index = True)

df.rename(columns={"98.6":"o2Saturation",
                   "trtbps":"blood_pressure",
                   "chol":"Cholestoral",
                   "fbs":"fasting_blood_sugar",
                   "thalachh":"max_heart_rate",
                   "exng":"exercise"},inplace=True)

df.loc[(df['sex'] ==1), 'sex'] = "Man"
df.loc[(df["sex"] ==0), 'sex'] = "Woman"

df.loc[(df["output"] ==1), 'output'] = "High"
df.loc[(df['output'] ==0), 'output'] = 'Low'



#plot Count plot for various categorical features
st.title("Heart Attack Data EDA")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Count plot for various categorical features")
fig  =  count_plots(df)
st.plotly_chart( fig , use_container_width=False)

# plot density charts 
st.title("Density plots")
fig = density_plots(df)
st.pyplot(fig)

# plot Chest pain 
st.title( 'CP Count')
st.markdown("""
              ### cp : Chest Pain\n
              ###### value 1 = typical angina\n
              ###### value 2 = atypical angina\n
              ###### value 3 = non-anginal pain\n
              ###### value 4 = asymtomatic\n
""")
fig  = cp_count(df)
st.pyplot(fig)

# plot thall count
st.title('Thall Count')
fig =  thall_count(df)
st.pyplot(fig)

# plot slp count
st.title('slp Count')
fig = slp_count(df)
st.pyplot(fig)

# plot age count
st.title("Age Count")
fig = age_count(df)
st.pyplot(fig)

#plot correlation matrix
st.title("correlation matrix")
fig = correlation_matrix(df)
st.pyplot(fig)

#plot male and female counts
st.title("male and female numbers")
fig, fig2 = male_and_female_count(df)
st.plotly_chart(fig)
st.plotly_chart(fig2)

#plot chance of heart attack with respect to chest pain
st.title("Low Chance of heatattack with respect to chest pain")
low = low_chance_of_heart_attack(df)
st.pyplot(low)
st.title("High Chance of heatattack with respect to chest pain")
high = high_chance_of_heart_attack(df)
st.pyplot(high)

#plot boxplot of heart rate by gender
st.title("Heart rates by gender")
fig,fig2 = heart_rate_by_gender(df)
st.plotly_chart(fig)
st.title('Heart rates by gender')
st.plotly_chart(fig2)

#plot blood pressure by Age
st.title("Blood pressure by Age")
fig = blood_pressure_by_age(df)
st.pyplot(fig)

#plot O2 saturation
st.title('O2 Saturation')
fig,fig2,fig3 =  o2_saturation(df)
st.plotly_chart(fig)
st.plotly_chart(fig2)
st.plotly_chart(fig3)


st.title("Count of Heart attack chance with respect to blood presure value ")
fig = blood_presure_count(df)
st.pyplot(fig)
sns.displot(df, x="caa", col = "output", kde= True, color="red")
fig=plt.show()
st.pyplot(fig)


#plot cahrts
fig = charts(df)  
st.pyplot(fig)


st.title("Exercise rate")
fig =  exercise_rate(df)
st.pyplot(fig)


st.markdown(
        '''### GitHub Repository: [heart attack analysis](https://github.com/rishibrainerhub/heart_attack_analysis)''')