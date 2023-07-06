import streamlit as st
from page_predict import show_predict
from page_insight import show_insight
from page_model_information import show_model_information

page = st.sidebar.selectbox("Choose Option", ("Predict", "Insight", "Model Information"))

if page == 'Predict':
    show_predict()
elif page == 'Insight':
    show_insight()
elif page == 'Model Information':
    show_model_information()
