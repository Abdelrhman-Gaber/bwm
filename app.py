import numpy as np
import pandas as pd
import streamlit as st 
import joblib

regressor=joblib.load('model.pkl')


def welcome():
    return "Welcome All"


def predict_bmwcar(model,	year,	transmission,	mileage	,fuelType,	tax	,mpg,	engineSize):
  prediction=regressor.predict(pd.DataFrame({'model':[model],'year':[year]	,'transmission':[transmission],	'mileage':[mileage],	'fuelType':[fuelType],'tax':[tax],	'mpg':[mpg],	'engineSize':[engineSize]}))
  print(prediction)
  return  prediction
def main():
    st.title("BMW price prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit BMW price prediction App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    model = st.text_input("model","Type Here")
    year = st.text_input("year","Type Here")
    transmission = st.text_input("transmission","Type Here")
    mileage = st.text_input("mileage","Type Here")
    fuelType = st.text_input("fuelType","Type Here")
    tax = st.text_input("tax","Type Here")
    mpg = st.text_input("mpg","Type Here")
    engineSize = st.text_input("engineSize","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_bmwcar(model,	year,	transmission,	mileage	,fuelType,	tax	,mpg,	engineSize)
    st.success('The price is {} USD'.format(result))
    if st.button("About"):
        st.text("our app using streamlit")
        st.text("best of luck in your GP")
if __name__=='__main__':
    main()        
