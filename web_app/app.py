import streamlit as st
import pickle
import numpy as np
import pandas as pd
import xgboost as xgb
#import shap
#import matplotlib.pyplot as plt
from utils import preprocess_df, analytes_nclp_mapping, values_dict, column_means
from constants import MODEL, FEATURE_COLUMNS, USED_COLUMNS, USES_DIFF_FROM_LAST

with open("/app/loopofhenle/web_app/"+MODEL,"rb") as f:
    model=pickle.load(f)

def main():
    #st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Kidney in Check</h1>", unsafe_allow_html=True)
    st.sidebar.header("What does this app do?")
    st.sidebar.text(
        """
        This app is has been create based on collaboration
        with doctors. We have used historical diagnoses
        written by doctors to create early warning
        for possible kidney diasease. Combining expert
        knowledge of doctors and improvement in machine
        learning we are now able to predict kidney diasease
        years earlier then it reaches first stage.
        """)
    st.sidebar.header("Disclaimer")
    st.sidebar.text(
        """
        No medical adivce.
        Not validated for clinical practice.
        """)

    tab1, tab2= st.tabs(
        ["Predict CDK for patients from excel file",
        "Predict manually adding values"]
        )

    with tab1:
        st.header("Add excel file with lab test of patients:")

        option = st.selectbox(
            'What is your input?',
            ('Examplary CKD patient',"Examplary non-CKD patient","Examplary possible-CKD patient"))

        # TODO: make it work with excel
        # if option =="Excel":
        #     df = st.file_uploader("Choose a XLSX file", type="xlsx")
        if option == 'Examplary CKD patient':
            with open("/app/loopofhenle/web_app/test_ckd_patient.csv","rb") as f:
                df = pd.read_csv(f)
        elif option == 'Examplary non-CKD patient':
            with open("/app/loopofhenle/web_app/test_non_ckd_patient.csv","rb") as f:
                df = pd.read_csv(f)
        elif option == 'Examplary possible-CKD patient':
            with open("/app/loopofhenle/web_app/test_possible_ckd_patient.csv","rb") as f:
                df = pd.read_csv(f)

        if len(df)>0:
            st.header("Your file:")
            st.dataframe(df)

            data = preprocess_df(df)

            st.header("Prepared data for model:")
            st.dataframe(data)

        if st.button('Predict', key="tab1"):
            prediction = model.predict(data[FEATURE_COLUMNS])
            proba = model.predict_proba(data[FEATURE_COLUMNS])
            prediction = np.mean(prediction)
            if prediction > 0.5:
                proba = np.mean(proba[:,1])
                proba = np.round(proba,decimals=2)
                st.success(f"POSITIVE: Patient is on his way to CKD (with probability {proba:.2f}), please act now.")
            else:
                proba = np.mean(proba[:,0])
                proba = np.round(proba,decimals=2)
                st.success(f"NEGATIVE: This patient doesn't seem to be on his way to CKD (with probability {proba:.2f}).")

            # TODO: add shap dependency
            #??create shapley explanation
            # explainer = shap.TreeExplainer(model)

            # shap_values = explainer.shap_values(data[FEATURE_COLUMNS])

            # # visualize the first prediction's explanation (use matplotlib=True to avoid Javascript)
            # st.write(shap.force_plot(explainer.expected_value, shap_values[-1,:], data[FEATURE_COLUMNS].iloc[-1,:], matplotlib=True), unsafe_allow_html=True)
            # st.pyplot(bbox_inches='tight')
            # plt.clf()

    with tab2:
        st.header("Fill in form below as input:")


        options = st.multiselect(
            'What test about patient do you currently have?',
            list(values_dict.keys()),
            ["s_kreatinin","B_Trombocyty","B_Hemoglobin","B_Erytrocyty","B_Leukocyty"])

        inputs=[]
        index=[]
        for option in options:
            high, low, unit = values_dict[option]
            inputs.append(st.slider(min_value=low, max_value=high, label=f"{option} [{unit}]"),)
            index.append(option)

        data = pd.DataFrame(inputs,index=index).T
        st.dataframe(data)

        new_columns = []
        for col in data.columns:
            if col in analytes_nclp_mapping:
                col = analytes_nclp_mapping[col]

            new_columns.append(str(col))

        data.columns = new_columns

        for col in FEATURE_COLUMNS:
            if not col in data.columns:
                data[col] = column_means[col]

        if st.button('Predict', key="tab2"):
                prediction = model.predict(data[FEATURE_COLUMNS])
                proba = model.predict_proba(data[FEATURE_COLUMNS])
                if prediction[0]:
                    proba = np.round(proba[0][1],decimals=2)
                    st.success(f"POSITIVE: Patient is on his way to CKD (with probability {proba:.2f}), please act now.")
                else:
                    proba = np.round(proba[0][0],decimals=2)
                    st.success(f"NEGATIVE: This patient doesn't seem to be on his way to CKD (with probability {proba:.2f}).")

                #??create shapley explanation

        #??create shapley explanation

    

if __name__ =='__main__':
    main()
