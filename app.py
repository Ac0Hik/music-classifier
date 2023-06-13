import streamlit as st
from predict import show_predict_page
from explore import show_explore
from utils import add_logo





my_logo = add_logo(logo_path="assets/img/logo.jpg", width=150, height=150)
st.sidebar.image(my_logo, use_column_width=False, caption=None, output_format="JPEG")

page = st.sidebar.selectbox("Explore Or Predict", ( 'Explore',"Predict"))


# LINK TO THE CSS FILE
with open("assets/css/style.css")as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

if page == "Predict":
    show_predict_page()
else:
    show_explore()
