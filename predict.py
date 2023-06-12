import streamlit as st
import numpy as np
from keras.models import model_from_json
from utils import print_class_name, class_pred
import base64

# load json and create model
json_file = open('model/Moroccanmodel.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("model/Moroccanmodel.h5")
print("Loaded model from disk")


# def autoplay_audio(file_path: str):
#     with open(file_path, "rb") as f:
#         data = f.read()
#         b64 = base64.b64encode(data).decode()
#         md = f"""
#             <audio controls autoplay="true">
#             <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
#             </audio>
#             """
#         st.markdown(
#             md,
#             unsafe_allow_html=True,
#         )
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        
        
      }}
    </style>
    """,
    unsafe_allow_html=True
    )
  
    
def show_predict_page():
    
    add_bg_from_local('bg1.png') 
    
    st.title("Moroccan Music Classifier")


    st.write("""### upload your wav file down below""")

    uploaded_file = st.file_uploader("")
    
    
    if uploaded_file is not None:
      classes_x = class_pred(model, uploaded_file)
      classname = print_class_name(classes_x)
      print(classname)

      ok = st.button("Predict Genre")

      if ok:
        st.subheader(f"The predicted class is {classname}")
        st.audio(uploaded_file, format='audio/ogg')

    



    

      






    

