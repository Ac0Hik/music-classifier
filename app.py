import streamlit as st
from predict import show_predict_page



page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))


show_predict_page()