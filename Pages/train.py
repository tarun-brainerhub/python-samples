import streamlit as st
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold, cross_val_score, train_test_split, GridSearchCV, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB, ComplementNB, BernoulliNB, CategoricalNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report, jaccard_score, log_loss
import pandas as pd

def app():
        df_addded = st.session_state.get("df_added")
        df = st.session_state.get("df")

        if df_addded:
            score_dict = {}
            test_size =  st.number_input("select test size (0.2 is ideal test size)", min_value=0.1, max_value=1.0, step=0.1)
            output = st.radio("select output feature", df.columns)
            st.session_state["output"] = output
            btn  = st.button("Enter")

            if btn:
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

                xgbc = Pipeline([('scaler', StandardScaler()), ('clf', xgb.XGBClassifier())])
                xgbc.fit(X_train, y_train)
                xgbc_score =xgbc.score(X_test, y_test)
                xgbc_recall_score = recall_score(y_test, xgbc.predict(X_test))



                score_dict = {"Model": ["Logisticregression","SVC","DecisionTree","Randomforest","xgboost"],
                                "Test size":[test_size,test_size,test_size,test_size,test_size],
                                "Accurcy":[logreg_score,svc_score,dtree_score,rforest_score,xgbc_score],
                                "Recall":[logreg_recall_score,svc_recall_score,dtree_recall_score,rforest_recall_score,xgbc_recall_score]}
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
            st.write("Please upload your data in home page")
