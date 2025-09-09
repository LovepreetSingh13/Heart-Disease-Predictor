import numpy as np
import pandas as pd
import streamlit as st
import pickle 
import base64
 
st.title("Heart Disease Predictor")
tab1 , tab2= st.tabs(["Predict","Model Information"])

with open('df.pkl','rb') as file:
    df = pickle.load(file)

with tab1:
    age =  st.number_input("Age(in years)",min_value = 0 , max_value = 120)
    sex = st.selectbox("Sex",["Male","Female"])