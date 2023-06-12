import streamlit as st
from predict import show_predict_page



page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

# LINK TO THE CSS FILE
with open("style.css")as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

show_predict_page()
