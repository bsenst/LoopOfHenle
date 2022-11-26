import streamlit as st
import pickle
import numpy as np
import pandas as pd
import xgboost as xgb
from utils import preprocess_df, analytes_nclp_mapping
from constants import MODEL, FEATURE_COLUMNS, USED_COLUMNS, USES_DIFF_FROM_LAST

with open("/app/loopofhenle/web_app/" + MODEL,"rb") as f:
    model=pickle.load(f)

def main():
    st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>Kidney in Check</h1>", unsafe_allow_html=True)
    st.sidebar.header("What does this app do?")
    st.sidebar.text(
        """This app is has been create based on collaboration with doctors.
        We have used historical diagnoses written by doctors based to improve early warning for possible kidney diasease.
        Combining expert knowledge of doctors and improvement in machine learning we are know able to predict kidney diasease years earlier then it reaaches first stage.
        """)

    tab0, tab1, tab2, tab3 = st.tabs(
        ["Debug tab",
        "Predict CDK for patients from excel file",
        "Predict manually adding values",
        "Test application on exemplary patients"]
        )

    with tab0:
        inputs = np.random.random(size=(1,34))
        data = pd.DataFrame(inputs, columns=FEATURE_COLUMNS)

        if st.button('Predict'):
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
        # data = preprocess_file

        # skips p_id, entry_data
        # model.predict(data)

        # create shapley explanation

    with tab2:
        st.header("Fill in form below as input:")

        #inputs = preprocess_inputs

        # create shapley explanation
        
    with tab3:
        st.header("Test")

        # load local data


        # display them

        # preprocess input


        # create shapley explanation

    

if __name__ =='__main__':
    main()
