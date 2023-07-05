import streamlit as st
from page_predict import show_predict
from page_insight import show_insight

page = st.sidebar.selectbox("Predict Or Insight", ("Predict", "Insight"))

if page == 'Predict':
    show_predict()
elif page == 'Insight':
    show_insight()

