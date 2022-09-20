from git import Object
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle



#text/title
st.title("====CAR PRICE PREDICTION====")

# images
from PIL import Image
im = Image.open("car.png")
st.image(im, width=500)

st.subheader("*Enter the Features of Your Car*")
st.text("    ")

final_scaler = pickle.load(open("final_auto", 'rb'))
model = pickle.load(open('final_as', 'rb'))
columns_name = pickle.load(open("columns", 'rb'))


#select box
make_model = st.selectbox('make_model', ('Audi A1', 'Audi A2', 'Audi A3', 'Opel Astra', 'Opel Corsa','Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))
Gearing_Type=st.selectbox('Gearing_Type', ('Automatic', 'Manual', 'Semi-automatic'))
hp_kW = st.number_input("hp_kW:", step=1)
age = st.number_input("age:", step=1)
km = st.number_input("km:", step=1)
my_dict = {
    "hp_kW": hp_kW,
    "age": age,
    "km": km,
    "make_model": make_model,
    "Gearing_Type": Gearing_Type
}
df=pd.DataFrame([my_dict])

my_dict = pd.get_dummies(df).reindex(columns=columns_name, fill_value=0)

my_dict = final_scaler.transform(my_dict)

if st.button("Predict"):
    pred = model.predict(my_dict)
    st.success("The estimated price of your car is €{}. ".format(int(pred)))


