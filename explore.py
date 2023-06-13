import streamlit as st
from utils import add_bg_from_local



def show_explore():

    add_bg_from_local('assets/img/bg1.png') 
    st.title("Welcome to MMC")
    st.write("""**Discover Moroccan music genres with our web app. Experience the rhythms 
                   and melodies that define this rich musical heritage. Browse, listen, and classify tracks effortlessly.
                   Immerse yourself in the magic of Moroccan music.**""")

    st.write("**This is a web app that classifies Moroccan music to _:red[6 genres]_ all you have**")

    st.header("Genres")
    st.write("**These are the 6 genres that model can predict:**")
    st.markdown("**Gnawa**")
    st.markdown("**Chaabi**")
    st.markdown("**Andalusian**")
    st.markdown("**Imazighn**")
    st.markdown("**Rai**")
    st.markdown("**Rap**")


    st.subheader("Tutorial")
    st.write("**Please head to predict page using the navigation menu**")
    st.write("**Upload your :red[.wav] file and hit :red[predict]**")
    st.write("**If the predict button doesn't show up please be patient**")
    st.write("**Click predict and the corresponding class will show up based on the model's classfication**")
    st.write("**You will also be able to play the audio you uploaded make sure you vibe to it if the model made an accurate prediction 😊**")



    st.write("**Made with 🧡 by  MMC dev team**")
