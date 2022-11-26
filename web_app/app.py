import streamlit as st
import pickle
import numpy as np
import pandas as pd
import xgboost as xgb
#from utils import preprocess_file

with open("model_weighted.pkl","rb") as f:
    model=pickle.load(f)

columns_names = ['8574.0', '3086.0', '5254.0', '2688.0', '4769.0', '13808.0', '1675.0', '2419.0', '2099.0', '1991.0', '4726.0', '16263.0', '18895.0', '5272.0', '3078.0', '582.0', '17339.0', '921.0', '1961.0', '3410.0', '5143.0', '12367.0', '12348.0', '12347.0', '12369.0', '12365.0', '18029.0', '18027.0', '12449.0', '12460.0', '12483.0', '12478.0', '12471.0', '543.0']

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

    with tab1:
        inputs = np.random.random(size=(1,34))
        data = pd.DataFrame(inputs, columns=columns_names)
        # inputs = preprocess_file
        # inputs preprocess_inputs
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

    with tab2:
        st.header("A dog")
        
    with tab3:
        st.header("Test")

    

if __name__ =='__main__':
    main()
