import pickle
import streamlit as st

model = pickle.load(open("housePrice.pkl", "rb"))

def deployModel():
    st.title("House Price Predictor")

    area = st.number_input("Enter the area:")
    bedrooms = st.number_input("Enter the number of bedrooms:")
    age = st.number_input("Enter age:")

    predict = st.button("Predict Price")
    if predict:
        price = model.predict([[area, bedrooms, age]])[0]
        st.write(f"The predicted price of the house is: {price:.2f}")


deployModel()