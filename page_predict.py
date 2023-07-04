import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('heart_disease_model.pickle', 'rb') as f:
        data = pickle.load(f)
    return data

data = load_model()

def show_predict():
    st.title('Heart Disease Prediction')

    age = st.select_slider('Age', options=[i for i in range(1, 120)])

    sex = st.selectbox('Sex', ("Male", "Female"))
    if sex == 'Male':
        sex = 1
    elif sex == 'Female':
        sex = 2

    chestpain = st.selectbox('Chest Pain Type', ("Asymptomatic", "Non-anginal Pain", "Atypical Angina", "Typical Angina"))
    if chestpain == 'Asymptomatic':
        chestpain = 1
    elif chestpain == 'Non-anginal Pain':
        chestpain = 2
    elif chestpain == 'Atypical Angina':
        chestpain = 3
    elif chestpain == 'Typical Angina':
        chestpain = 4
    
    restingbp = st.select_slider('Resting Blood Pressure', options=[i for i in range(1, 200)])

    cholesterol = st.select_slider('Cholesterol', options=[i for i in range(1, 610)])

    fastingbs = st.selectbox('Fasting Blood Sugar', ("Lower than 120mg/ml", "Greater than 120mg/ml"))
    if fastingbs == 'Lower than 120mg/ml':
        fastingbs = 0
    elif fastingbs == 'Greater than 120mg/ml':
        fastingbs = 1

    restingecg = st.selectbox('Resting Electrocardiographic Results', ("Normal", "Showing probable or definite left ventricular hypertrophy", "Having ST-T wave abnormality"))
    if restingecg == 'Normal':
        restingecg = 0
    elif restingecg == 'Showing probable or definite left ventricular hypertrophy':
        restingecg = 1
    elif restingecg == 'Having ST-T wave abnormality':
        restingecg = 2

    maxhr = st.select_slider('Maximum Heart Rate Achieved', options=[i for i in range(50, 202)])

    exerciseangina = st.selectbox('Exercise Induced Angina', ("Yes", "No"))
    if exerciseangina == 'Yes':
        exerciseangina = 1
    elif exerciseangina == 'No':
        exerciseangina = 0

    oldpeak = st.text_input('Oldpeak')

    st_slope = st.selectbox('ST Slope', ("Upsloping", "Flat", "Downsloping"))
    if st_slope == 'Upsloping':
        st_slope = 1
    elif st_slope == 'Flat':
        st_slope = 2
    elif st_slope == 'Downsloping':
        st_slope = 3

    ok = st.button("Predict")
    if ok:
        X = np.array([[age, sex, chestpain, restingbp, cholesterol, fastingbs, restingecg, maxhr, exerciseangina, oldpeak, st_slope]])
        pred = data.predict(X)
        if pred == 0:
            st.subheader(f'You do not have a heart disease')
        if pred == 1:
            st.subheader(f'You have a heart disease')