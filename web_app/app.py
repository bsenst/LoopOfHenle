import streamlit as st
import pickle
import numpy as np
import pandas as pd
import xgboost as xgb
from utils import preprocess_df, analytes_nclp_mapping, values_dict, column_means
from constants import MODEL, FEATURE_COLUMNS, USED_COLUMNS, USES_DIFF_FROM_LAST

with open("/app/loopofhenle/web_app/" +MODEL,"rb") as f:
    model=pickle.load(f)

def main():
    st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Kidney in Check</h1>", unsafe_allow_html=True)
    st.sidebar.header("What does this app do?")
    st.sidebar.text(
        """This app is has been create based on collaboration with doctors.
        We have used historical diagnoses written by doctors based to improve early warning for possible kidney diasease.
        Combining expert knowledge of doctors and improvement in machine learning we are know able to predict kidney diasease years earlier then it reaaches first stage.
        """)

    tab1, tab2, tab3 = st.tabs(
        ["Predict CDK for patients from excel file",
        "Predict manually adding values",
        "Test application on exemplary patients"]
        )

    with tab0:
        inputs = np.random.random(size=(1,34))
        data = pd.DataFrame(inputs, columns=FEATURE_COLUMNS)

        if st.button('Predict', key="predict_excel"):
            prediction = model.predict(data)
            proba = model.predict_proba(data)
            if prediction[0]:
                proba = np.round(proba[0][1],decimals=2)
                st.success(f"Patient is on his way to CKD (with probability {proba:.2f}), please act now.")
            else:
                proba = np.round(proba[0][0],decimals=2)
                st.success(f"This patient doesn't seem to be on his way to CKD (with probability {proba:.2f}).")

            # create shapley explanation

    with tab1:
        st.header("Add excel file with lab test of patients:")

        uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")

        # TODO: remove this debug data
        with open("test_ckd_patient.xlsx","rb") as uploaded_file:

            if uploaded_file:
                df = pd.read_excel(uploaded_file)

                st.header("Your file:")
                st.dataframe(df)

                data = preprocess_df(df)

                st.header("Prepared data for model:")
                st.dataframe(data)

            if st.button('Predict', key="tab1"):
                prediction = model.predict(data)
                proba = model.predict_proba(data)
                if prediction[0]:
                    proba = np.round(proba[0][1],decimals=2)
                    st.success(f"Patient is on his way to CKD (with probability {proba:.2f}), please act now.")
                else:
                    proba = np.round(proba[0][0],decimals=2)
                    st.success(f"This patient doesn't seem to be on his way to CKD (with probability {proba:.2f}).")

                # create shapley explanation


        # skips p_id, entry_data
        # model.predict(data)

        # create shapley explanation

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
        st.dataframe(data)

        for col in FEATURE_COLUMNS:
            if not col in data.columns:
                data[col] = column_means[col]

        st.dataframe(data)

        if st.button('Predict', key="tab2"):
                prediction = model.predict(data[FEATURE_COLUMNS])
                proba = model.predict_proba(data[FEATURE_COLUMNS])
                if prediction[0]:
                    proba = np.round(proba[0][1],decimals=2)
                    st.success(f"Patient is on his way to CKD (with probability {proba:.2f}), please act now.")
                else:
                    proba = np.round(proba[0][0],decimals=2)
                    st.success(f"This patient doesn't seem to be on his way to CKD (with probability {proba:.2f}).")

                # create shapley explanation

        # create shapley explanation

    

if __name__ =='__main__':
    main()
