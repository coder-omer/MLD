import streamlit as st
import pickle
import pandas as pd
from sklearn.linear_model import Lasso

st.title('Car Price Prediction')
html_temp = """
<div style="background-color:green;padding:10px">
<h2 style="color:white;text-align:center;">App with Streamlit</h2>
</div>"""

st.markdown(html_temp,unsafe_allow_html=True)

model = pickle.load(open("final_model.pkl","rb"))

columns = pickle.load(open("columns.pkl", 'rb'))

final_scale = pickle.load(open("final_scale.pkl", 'rb'))


hp = st.slider("What is the horsepower of your car",60,200,step=5)
age = st.selectbox("What is the age of your car?",(1,2,3))
km=st.slider("What is the km of your car?",0,100000,step=500)
make_model=st.selectbox("Select model of your car", ('Audi A1', 'Audi A2', 'Audi A3','Astra','Clio','Corsa','Espace','Insignia'))
gearing_type=st.selectbox("Select gearing type of your car", ('Automatic', 'Manual', 'Semi-automatic'))
gears= st.selectbox("What is the gear of your car?",(1,2,3,4,5,6,7)) 



my_dict = {
	"hp": hp,	
    	"age": age,
    	"km": km,
    	"model": make_model
	"Gearing_Type": gearing_type,
	"Gears": gears
}

df = pd.DataFrame.from_dict([my_dict])

df = pd.get_dummies(df)

df = df.reindex(columns=columns, fill_value=0)

df = final_scale.transform(df)

prediction = model.predict(df)

st.success("your car's estimated price is €{}. ".format(int(prediction[0])))

pressed = mid_column.button('Predict Car Price')

if pressed:
  st.subheader(f"This Car is predicted to cost around ₹ {prediction:,.0f}")
  st.balloons()

