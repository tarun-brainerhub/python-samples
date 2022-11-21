import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.svm import SVC ,SVR
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import recall_score, r2_score,  mean_absolute_error
import pandas as pd

def app():
        df_addded = st.session_state.get("df_added")
        df = st.session_state.get("df")

        if df_addded:
            test_size =  st.number_input("select test size (0.2 is ideal test size)", min_value=0.1, max_value=1.0, step=0.1)
            output = st.radio("select output feature", df.columns)
            btn  = st.button("Enter")
            if btn:
                st.session_state["output"] = output
                if len(df[output].value_counts()) == 2:
                    with st.spinner('Models are training.......'):
                        df = st.session_state.get("df")
                        X = df.drop(output, axis =1)
                        y = df[output]
                        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

                        logreg = Pipeline([('scaler', StandardScaler()), ('clf', LogisticRegression(solver='newton-cg'))])
                        logreg.fit(X_train, y_train)
                        logreg_score = logreg.score(X_test,y_test)
                        logreg_recall_score = recall_score(y_test, logreg.predict(X_test)) 
                        
                        svc = Pipeline([('scaler', StandardScaler()), ('clf', SVC())])
                        svc.fit(X_train, y_train)
                        svc_score = svc.score(X_test,y_test)
                        svc_recall_score = recall_score(y_test, svc.predict(X_test))

                        dtree = Pipeline([('scaler', StandardScaler()), ('clf', DecisionTreeClassifier(random_state=0))])
                        dtree.fit(X_train, y_train)
                        dtree_score = dtree.score(X_test,y_test)
                        dtree_recall_score = recall_score(y_test, dtree.predict(X_test))

                        rf = RandomForestClassifier()
                        rforest = Pipeline([('scaler', StandardScaler()), ('clf', rf)])
                        rforest.fit(X_train, y_train)
                        rforest_score =rforest.score(X_test, y_test)
                        rforest_recall_score = recall_score(y_test, rforest.predict(X_test))
    
                        score_dict = {"Model": ["Logisticregression","SVC","DecisionTree","Randomforest"],
                                        "Test size":[test_size,test_size,test_size,test_size,],
                                        "Accurcy":[logreg_score,svc_score,dtree_score,rforest_score],
                                        "Recall":[logreg_recall_score,svc_recall_score,dtree_recall_score,rforest_recall_score]}
                                        
                        score = pd.DataFrame(score_dict)
                        st.dataframe(score)
                        best_model = score.sort_values(by=['Recall'], ascending=False).head(1)['Model'].values[0]
                        st.success(f"best performin model is {best_model}")
                        if best_model == "Logisticregression":
                            st.session_state["best_model"] = logreg
                        if best_model == "SVC":
                            st.session_state["best_model"] = svc
                        if best_model == "DecisionTree":
                            st.session_state["best_model"] = dtree
                        if best_model == "Randomforest":
                            st.session_state["best_model"] = rforest
                else:
                    with st.spinner('Models are training.......'):
                        df = st.session_state.get("df")
                        X = df.drop(output, axis =1)
                        y = df[output]
                        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

                        logreg = Pipeline([('scaler', StandardScaler()), ('clf', LogisticRegression(solver='newton-cg'))])
                        logreg.fit(X_train, y_train)
                        logreg_r2_score = r2_score(y_test, logreg.predict(X_test))
                        logreg_mae = mean_absolute_error(y_test, logreg.predict(X_test))

                        
                        svr = Pipeline([('scaler', StandardScaler()), ('clf', SVR())])
                        svr.fit(X_train, y_train)
                        svr_r2_score = r2_score(y_test, svr.predict(X_test))
                        svr_mae = mean_absolute_error(y_test, svr.predict(X_test))

                        dtree = Pipeline([('scaler', StandardScaler()), ('clf', DecisionTreeRegressor(random_state=0))])
                        dtree.fit(X_train, y_train)
                        dtree_r2_score =r2_score(y_test, dtree.predict(X_test))
                        dtree_mae = mean_absolute_error(y_test, dtree.predict(X_test))

                        rf = RandomForestRegressor()
                        rforest = Pipeline([('scaler', StandardScaler()), ('clf', rf)])
                        rforest.fit(X_train, y_train)
                        rforest_r2_score = r2_score(y_test, rforest.predict(X_test))
                        rforest_mae = mean_absolute_error(y_test, rforest.predict(X_test))

                        score_dict = {"Model": ["Logisticregression","SVC","DecisionTree","Randomforest"],
                                        "Test size":[test_size,test_size,test_size,test_size,],
                                        "r2 score":[logreg_r2_score,svr_r2_score,dtree_r2_score,rforest_r2_score],
                                        "mean absolute error":[logreg_mae, svr_mae,dtree_mae,rforest_mae]}
                        score = pd.DataFrame(score_dict)
                        st.dataframe(score)
                        best_model = score.sort_values(by=['r2 score'], ascending=False).head(1)['Model'].values[0]
                        st.success(f"best performin model is {best_model}")
                        if best_model == "Logisticregression":
                            st.session_state["best_model"] = logreg
                        if best_model == "SVC":
                            st.session_state["best_model"] = svr
                        if best_model == "DecisionTree":
                            st.session_state["best_model"] = dtree
                        if best_model == "Randomforest":
                            st.session_state["best_model"] = rforest                   

        else:
            st.write("Please upload your data in home page")
