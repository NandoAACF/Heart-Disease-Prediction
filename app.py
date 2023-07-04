import streamlit as st
from page_predict import show_predict

page = st.sidebar.selectbox("Predict Or Insight", ("Predict", "Insight"))

if page == 'Predict':
    show_predict()

