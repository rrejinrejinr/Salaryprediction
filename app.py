import streamlit as st
import joblib
import numpy as np

model=joblib.load("Salaryprediction")
st.title("Salary Prediction App")
years=st.number_input("Enter the work Experience")
jobrate=st.number_input("Enter the job Rate")

if st.button("Predict"):
  result=model.predict([[years,jobrate]])
  st.write("Predict the Annual Salary",result)
