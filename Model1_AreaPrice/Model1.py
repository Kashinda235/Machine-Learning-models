import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open("areaPrice.pkl", "rb"))

def depModel():
    st.title("Area Price Prediction")
    area = st.number_input("Enter the area:")

    if st.button("Predict Price"):
        price = model.predict([[area]])[0]
        st.write(f"The predicted price of the house is: {price:.2f}")

depModel()