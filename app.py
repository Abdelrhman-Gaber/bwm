import pandas as pd
import joblib
import numpy as np
import streamlit as st


regressor = joblib.load('model.pkl')
df = pd.read_csv('bmw.csv')

def predict_bmw_price(model, year, transmission, mileage,fuelType ,tax, mpg, engineSize):
    prediction = regressor.predict(pd.DataFrame({'model':[model],'year':[year]	,'transmission':[transmission],	'mileage':[mileage],'fuelType':[fuelType],'tax':[tax],	'mpg':[mpg],'engineSize':[engineSize]}))
    return prediction

def main():
    st.title('BMW price prediction')
    
    model = st.selectbox("model" , df['model'].unique())
    year = st.text_input('year', 'please enter the year')
    transmission = st.selectbox("transmission" , df['transmission'].unique())
    mileage = st.text_input('mileage', 'please enter the mileage')
    fuelType = st.selectbox("fuelType" , df['fuelType'].unique())
    tax = st.text_input('tax', 'please enter the tax')
    mpg = st.text_input('mpg', 'please enter the mpg')
    engineSize = st.text_input('engineSize', 'please enter the engineSize')
    result = ""
    if st.button('predict'):
        result = predict_bmw_price(model, year, transmission, mileage,fuelType ,tax, mpg, engineSize)
    st.success('the price of the car is {} USD'.format(result))
    
if __name__=='__main__':
    main()
