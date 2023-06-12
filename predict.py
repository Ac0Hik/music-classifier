import streamlit as st
import numpy as np
from keras.models import model_from_json
from utils import print_class_name, class_pred


# load json and create model
json_file = open('model/Moroccanmodel.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load weights into new model
model.load_weights("model/Moroccanmodel.h5")
print("Loaded model from disk")



def show_predict_page():
    st.title("Moroccan Music Classifier")


    st.write("""### upload Moroccan Music""")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
      classes_x = class_pred(model, uploaded_file)
      classname = print_class_name(classes_x)
      print(classname)

      ok = st.button("Predict Genre")

      if ok:
        st.subheader(f"The predicted class is {classname}")




    

      






    

