# -*- coding: utf-8 -*-
"""lishaapp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HKR_DY8zese1uRJduBBznGDFIZReFaAH
"""

#Install package
#!pip install streamlit

# Import Libraries
import streamlit as st
import pandas as pd
import pickle

import os
print(os.getcwd())

from google.colab import files
uploaded = files.upload()

#with open('subdirectory/best_rf_model.pkl', 'rb') as file:
#    model = pickle.load(file)

# Load the trained model
with open('best_rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title and description
st.title("Diabetes Prediction App")
st.write("Enter the following features to predict diabetes.")

# Define inputs for each feature (example)
age = st.number_input("Age", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
glucose = st.number_input("Glucose Level", min_value=50, max_value=200, value=100)

# Predict when button is clicked
if st.button("Predict"):
    # Prepare input data as a DataFrame (assuming model was trained on a DataFrame)
    input_data = pd.DataFrame([[age, bmi, glucose]], columns=['age', 'bmi', 'glucose'])
    prediction = model.predict(input_data)

    # Display the prediction
    if prediction[0] == 1:
        st.write("The model predicts diabetes.")
    else:
        st.write("The model predicts no diabetes.")

